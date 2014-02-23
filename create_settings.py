import os
import yaml

from collections import OrderedDict


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: object_pairs_hook(loader.construct_pairs(node)))
    return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


def prompt_user(settings, depth=1, defaults=True):
    if depth is 1:
        print "Enter values for:"
    for key, val in settings.iteritems():
        indent = "  " * depth
        if isinstance(val, dict):
            print "{}{}:".format(indent, key)

            org_len = len(val)
            prompt_user(val, depth+1, defaults)

            # Remove if all values were default.
            if defaults is False and len(val) is 0 and org_len is not 0:
                settings.pop(key)
        else:
            new_val = raw_input("{}{}({}):".format(indent, key, val))
            if new_val:
                settings[key] = new_val
            elif defaults is False:
                settings.pop(key)

if os.path.isfile('settings.yaml'):
    print "Error settings.yaml file already exists"
else:
    settings = ordered_load(open('defaults.yaml'),
                            yaml.SafeLoader,
                            OrderedDict)
    prompt_user(settings, defaults=False)
    if settings:
        with open('settings.yaml', 'w') as f:
            f.write(ordered_dump(settings,
                                 Dumper=yaml.SafeDumper,
                                 default_flow_style=False))
    else:
        print "Nothing entered, file not being saved"
