class BufferImpl(object):
    def __init__(self):
        self._buffer = b""

    def feed(self, bytes_):
        self._buffer += bytes_

    def split(self, delim):
        lines = self._buffer.split(delim)
        self._buffer = lines.pop()
        return lines
