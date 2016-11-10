### ConMan: The Console Manager

[![Build Status](https://travis-ci.org/dun/conman.svg?branch=master)](https://travis-ci.org/dun/conman)

ConMan is a serial console management program designed to support a large
number of console devices and simultaneous users.

It supports:
- local serial devices
- remote terminal servers (via the telnet protocol)
- IPMI Serial-Over-LAN (via [FreeIPMI](https://www.gnu.org/software/freeipmi/))
- Unix domain sockets
- external processes (e.g., using Expect for telnet/ssh/ipmi-sol connections)

Its features include:
- logging (and optionally timestamping) console device output to file
- connecting to consoles in monitor (R/O) or interactive (R/W) mode
- allowing clients to share or steal console write privileges
- broadcasting client output to multiple consoles

#### License:
ConMan is [free software](https://www.gnu.org/philosophy/free-sw.html):
you can redistribute it and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.html)
as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

#### Homepage:
https://dun.github.io/conman/
