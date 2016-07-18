from ctypes import *

from pprint import pprint

# WriteFile = windll.kernel32.WriteFile
def WriteFile(hFile, MESSAGE):
    cbWritten = c_ulong(0)
    return windll.kernel32.WriteFile(
        hFile,
        c_char_p(MESSAGE),
        len(MESSAGE),
        byref(cbWritten),
        None
    )
