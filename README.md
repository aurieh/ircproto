# ircproto
A protocol-only, bring-your-own-IO IRC (client\*) library for the Python
programming language. Inspired by [h11](https://github.com/njsmith/h11/),
[jaraco/irc](https://github.com/jaraco/irc) and
[wsproto](https://github.com/python-hyper/wsproto).
This library implements IRC as defined in
[RFC 1459](https://tools.ietf.org/html/rfc1459). RFCs 2810, 2811, 2812\*\*, 2813
and 7194 have not been considered (yet). Non standard numerical reply codes are in
an unfinished state, so you might need to handle those yourself.
> \* A server implementation is on the roadmap

> \*\* Reply numericals have been ported over.

## Warning
This library is in a very unfinished state. You probably shouldn't use it.
PRs are welcome!
