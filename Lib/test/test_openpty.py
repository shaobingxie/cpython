# Test to see if openpty works. (But don't worry if it isn't available.)

import os
from test_support import verbose, TestFailed

try:
    if verbose:
        print "Calling os.openpty()"
    master, slave = os.openpty()
    if verbose:
        print "(master, slave) = (%d, %d)"%(master, slave)
except AttributeError:
    raise ImportError, "No openpty() available."

## # Please uncomment these if os.isatty() is added.
## if not os.isatty(master):
##     raise TestFailed, "Master-end of pty is not a terminal."
## if not os.isatty(slave):
##     raise TestFailed, "Slave-end of pty is not a terminal."

os.write(slave, 'Ping!')
print os.read(master, 1024)

