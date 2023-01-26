import urllib
from urllib import parse, request
from typing import Optional, Dict


def _request_content(url: str, data: Optional[Dict] = None, decode: bool = False):
    req = request.Request(url, data=data)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with request.urlopen(req) as resp:
        data = resp.read()
        if decode:
            text = data.decode("utf-8")
        else:
            text = data
        return text
