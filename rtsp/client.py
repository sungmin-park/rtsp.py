import socket
from io import TextIOWrapper
from typing import List
from urllib.parse import urlparse

__all__ = ['options']

NEWLINE = '\r\n'
EOH = NEWLINE * 2


def readlines(fp: TextIOWrapper):
    while True:
        yield fp.readline().strip()


def parse_status_line(line):
    pairs = line.split(' ')
    assert len(pairs) == 3

    version, status_code, msg = pairs
    assert version == 'RTSP/1.0'
    status_code = int(status_code)
    is_ok = msg == 'OK'
    return version, status_code, is_ok


def parse_headers(lines: List[str]):
    headers = {}
    for line in lines:
        name, value = map(lambda x: x.strip(), line.split(':', maxsplit=1))
        headers[name] = value
    return headers


def read_headers(lines):
    headers = []
    for line in lines:
        if not line:
            break
        headers.append(line)
    return headers


class RtspResponse:
    def __init__(self, lines):
        self.version, self.status_code, self.is_ok = parse_status_line(next(lines))
        self.headers = parse_headers(read_headers(lines))


def options(url: str):
    u = urlparse(url)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((u.hostname, u.port))
    try:
        with s.makefile('rw', newline=NEWLINE) as fp:
            msg = [
                'OPTIONS {url} RTSP/1.0'.format(url=u.geturl()),
                'CSeq: 1',
                ''
            ]
            for m in msg:
                print(m, file=fp)
            fp.flush()

            lines = readlines(fp)

            r = RtspResponse(lines)
            return r.headers['Public'].split(', ')
    finally:
        s.close()
