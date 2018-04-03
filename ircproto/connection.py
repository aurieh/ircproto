import re
from collections import deque
from typing import List

from .buffer import BufferImpl
from .errors import MessageInvalidError
from .events import Event
from .parser import arguments_from_group, mask_from_group
from .replies import replies

# thanks python-irclib
_rfc_1459_command_regexp = re.compile(
    "^(:(?P<prefix>[^ ]+) +)?(?P<command>[^ ]+)( *(?P<argument> .+))?")


class Connection(object):
    def __init__(self):
        self._buffer = BufferImpl()
        self._event_queue = deque()

    def send_data(self, *args: List[str]) -> bytes:
        string = ' '.join(filter(None, args))
        if '\n' in string:
            msg = "Newlines not allowed in messages"
            raise MessageInvalidError(msg)
        bytes_ = string.encode('utf-8') + b'\r\n'
        if len(bytes_) > 512:
            msg = "Messages should not go above 512 bytes (encoded in UTF-8)"
            raise MessageInvalidError(msg)
        return bytes_

    def recv_data(self, data: bytes):
        self._buffer.feed(data)
        for line in self._buffer.split(b"\r\n"):
            self._parse_line(line)

    def next_event(self) -> Event:
        try:
            return self._event_queue.pop()
        except IndexError:
            return None

    def _parse_line(self, line):
        grp = _rfc_1459_command_regexp.match(line.decode("utf-8")).group
        source = mask_from_group(grp('prefix'))
        cmd = grp('command').lower()
        cmd = replies.get(cmd, cmd)
        args = arguments_from_group(grp('argument'))
        self._event_queue.append(Event(source, cmd, args))
