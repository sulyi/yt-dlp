#!/usr/bin/env python3
import os

from yt_dlp import YoutubeDL
from yt_dlp.compat import WINDOWS_VT_MODE

ydl = YoutubeDL()
print('WINDOWS_VT_MODE:', WINDOWS_VT_MODE, '_vt_mode:', ydl._vt_mode)

size = os.get_terminal_size()
for width in range(size.columns - 1, size.columns + 2):
    print('\n', 'width', width)
    ydl.to_screen('\n'.join(
        '{line:=^{fill}}'.format(line=' %s ' % width, fill=width)
        for i in range(3)
    ))
