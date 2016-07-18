from ctypes import *

PIPE_ACCESS_INBOUND = 0x00000001
PIPE_ACCESS_OUTBOUND = 0x00000002
PIPE_ACCESS_DUPLEX = 0x00000003

PIPE_TYPE_BYTE = 0x00000000
PIPE_TYPE_MESSAGE = 0x00000004

PIPE_READMODE_BYTE = 0x00000000
PIPE_READMODE_MESSAGE = 0x00000002

PIPE_WAIT = 0x00000000
PIPE_NOWAIT = 0x00000001

INVALID_HANDLE_VALUE = -1

from pprint import pprint

def CreateNamedPipe(lpName, dwOpenMode, dwPipeMode, nMaxInstances, nOutBufferSize, nInBufferSize, nDefaultTimeOut, lpSecurityAttributes):
    pprint([lpName, dwOpenMode, dwPipeMode,
            nMaxInstances,
            nOutBufferSize, nInBufferSize,
            nDefaultTimeOut, lpSecurityAttributes])

    if isinstance(lpName, unicode):
        h = windll.kernel32.CreateNamedPipeW(
            lpName, dwOpenMode, dwPipeMode,
            nMaxInstances,
            nOutBufferSize, nInBufferSize,
            nDefaultTimeOut, lpSecurityAttributes)
    else:
        h = windll.kernel32.CreateNamedPipeA(
            lpName, dwOpenMode, dwPipeMode,
            nMaxInstances,
            nOutBufferSize, nInBufferSize,
            nDefaultTimeOut, lpSecurityAttributes)
    if h == INVALID_HANDLE_VALUE:
        raise WinError()
    print "Opened pipe", h
    return h

ConnectNamedPipe = windll.kernel32.ConnectNamedPipe
DisconnectNamedPipe = windll.kernel32.DisconnectNamedPipe
