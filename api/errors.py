class SkeletonError(Exception):
    """Generic error class."""
    def __init__(self, msg, http_code=500):
        self.msg = msg
        self.http_code = http_code


class HTTPError(SkeletonError):
    def __init__(self, msg, status_code):
        self.msg = msg
        self.status_code = status_code

    def __str__(self):
        return '%s: %s' % (self.status_code, self.msg)
