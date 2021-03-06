# Python Security Project (PySec) and its related class files.
#
# PySec is a set of tools for secure application development under Linux
#
# Copyright 2014 PySec development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: ascii -*-
"""PySec is a set of tools for secure application development under Linux"""
from pysec import (alg,
                   core,
                   io,
                   kv,
                   load,
                   log,
                   net,
                   utils,
                   xsplit)


_OPEN_MODES = {
    'r': io.fd.FO_READ,
    'w': io.fd.FO_WRITE,
    'a': io.fd.FO_APPEND
}

def open(path, mode='r'):
    mode = _OPEN_MODES.get(str(mode), None)
    if mode is None:
        raise ValueError("unknown open mode %r" % mode)
    return io.fd.File.open(path, mode)


xrange = utils.xrange
