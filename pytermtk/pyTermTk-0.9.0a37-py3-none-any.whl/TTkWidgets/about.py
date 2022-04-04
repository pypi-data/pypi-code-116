#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Eugenio Parodi <ceccopierangiolieugenio AT googlemail DOT com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from TermTk.TTkCore.log import TTkLog
from TermTk.TTkCore.cfg import TTkCfg
from TermTk.TTkCore.color import TTkColor
from TermTk.TTkCore.string import TTkString
from TermTk.TTkWidgets.window import TTkWindow
from TermTk.TTkWidgets.image import TTkImage

class TTkAbout(TTkWindow):
    peppered=[
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x01,0x00),(0x39,0x61,0x00),(0x76,0x9e,0x17),(0x87,0x9f,0x3a),(0x3d,0x4c,0x14),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x02,0x11,0x00),(0x21,0x44,0x01),(0x99,0xc1,0x33),(0x4e,0x71,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x30,0x5e,0x0f),(0x71,0x9e,0x47),(0x69,0xa2,0x32),(0x8b,0xa8,0x65),(0xb0,0xc4,0x91),(0x97,0xb6,0x66),(0xa0,0xad,0x81),(0x5f,0x8e,0x38),(0x42,0x77,0x19),(0x08,0x21,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x1b,0x00,0x00),(0x5b,0x00,0x00),(0x80,0x00,0x00),(0x6c,0x07,0x00),(0x35,0x29,0x00),(0x26,0x61,0x01),(0x5c,0x89,0x25),(0x76,0x73,0x28),(0x7e,0x67,0x1d),(0x54,0x6a,0x19),(0x3e,0x48,0x05),(0x9e,0x1b,0x18),(0xbe,0x40,0x40),(0xc7,0x3f,0x3f),(0xcc,0x1a,0x1b),(0xb1,0x00,0x00),(0x47,0x00,0x00)],
        [(0x00,0x00,0x00),(0x83,0x00,0x00),(0xd6,0x43,0x43),(0xf5,0x94,0x93),(0xff,0x7f,0x7f),(0xfc,0x42,0x43),(0xc9,0x02,0x03),(0xb4,0x02,0x02),(0xdb,0x41,0x41),(0xf9,0x90,0x91),(0xff,0xce,0xd0),(0xff,0xc2,0xc2),(0xfd,0x7d,0x7d),(0xd8,0x28,0x2a),(0xab,0x4c,0x4d),(0xf4,0xcd,0xce),(0xff,0xad,0xae),(0xff,0x47,0x47),(0xef,0x00,0x00),(0x81,0x00,0x00)],
        [(0x40,0x00,0x00),(0xf6,0x03,0x03),(0xff,0x6d,0x6d),(0xff,0xa5,0xa6),(0xfc,0x87,0x87),(0x8d,0x2d,0x2f),(0xe6,0x00,0x00),(0xff,0x0b,0x0d),(0xff,0x4a,0x49),(0xff,0x79,0x7a),(0xff,0x93,0x93),(0xff,0x8d,0x8d),(0xff,0x6b,0x6c),(0xff,0x34,0x34),(0xe5,0x00,0x00),(0x94,0x3d,0x3f),(0xff,0x41,0x42),(0xcd,0x02,0x01),(0x36,0x00,0x00),(0x00,0x00,0x00)],
        [(0x5b,0x00,0x00),(0xe8,0x00,0x00),(0xfe,0x05,0x05),(0xff,0x10,0x10),(0xed,0x0f,0x0e),(0x66,0x00,0x00),(0xec,0x00,0x00),(0xff,0x00,0x00),(0xff,0x08,0x08),(0xff,0x21,0x21),(0xff,0x2f,0x30),(0xff,0x2e,0x2e),(0xff,0x1b,0x1b),(0xff,0x03,0x03),(0xfa,0x00,0x00),(0x5b,0x00,0x00),(0xd0,0x00,0x00),(0x24,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x07,0x00,0x00),(0x56,0x00,0x00),(0x93,0x00,0x00),(0xb5,0x00,0x00),(0xca,0x00,0x00),(0x35,0x00,0x00),(0xa5,0x00,0x00),(0xeb,0x00,0x00),(0xfe,0x00,0x00),(0xff,0x00,0x00),(0xff,0x00,0x00),(0xff,0x00,0x00),(0xff,0x00,0x00),(0xfe,0x00,0x00),(0xd5,0x00,0x00),(0x3d,0x00,0x00),(0x6c,0x00,0x00),(0x02,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x04,0x00,0x00),(0x40,0x00,0x00),(0x4d,0x00,0x00),(0x30,0x00,0x00),(0x84,0x00,0x00),(0xc3,0x00,0x00),(0xe7,0x00,0x00),(0xf3,0x00,0x00),(0xf5,0x00,0x00),(0xe6,0x00,0x00),(0xbb,0x00,0x00),(0x54,0x00,0x00),(0x8c,0x00,0x00),(0x6a,0x00,0x00),(0x06,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x0c,0x00,0x00),(0x4e,0x00,0x00),(0x92,0x00,0x00),(0x8a,0x00,0x00),(0x41,0x00,0x00),(0x8a,0x00,0x00),(0xb9,0x00,0x00),(0xd5,0x00,0x00),(0xdf,0x00,0x00),(0xd2,0x00,0x00),(0x9d,0x00,0x00),(0x7e,0x00,0x00),(0xf7,0x00,0x00),(0xb8,0x00,0x00),(0x47,0x00,0x00),(0x03,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x05,0x00,0x00),(0x50,0x00,0x00),(0xa1,0x00,0x00),(0xe7,0x00,0x00),(0xb0,0x00,0x00),(0x7e,0x00,0x00),(0xd4,0x00,0x00),(0xfa,0x00,0x00),(0xfe,0x00,0x00),(0xf6,0x00,0x00),(0x9f,0x00,0x00),(0xcd,0x00,0x00),(0xff,0x00,0x00),(0xeb,0x00,0x00),(0x9a,0x00,0x00),(0x35,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x3c,0x00,0x00),(0xa0,0x00,0x00),(0xec,0x00,0x00),(0xfe,0x00,0x00),(0xbf,0x00,0x01),(0xb7,0x00,0x00),(0xfe,0x00,0x00),(0xff,0x00,0x00),(0xfb,0x00,0x00),(0x9d,0x02,0x02),(0xf8,0x12,0x13),(0xff,0x00,0x00),(0xf6,0x00,0x00),(0xb0,0x00,0x00),(0x43,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x1d,0x00,0x00),(0x8b,0x00,0x00),(0xe7,0x00,0x00),(0xff,0x00,0x00),(0xff,0x06,0x08),(0xb4,0x0b,0x0d),(0xf4,0x00,0x00),(0xff,0x00,0x00),(0xfc,0x00,0x00),(0xb5,0x0d,0x0d),(0xff,0x1a,0x1b),(0xff,0x00,0x00),(0xf8,0x00,0x00),(0xaf,0x00,0x00),(0x3b,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x04,0x00,0x00),(0x65,0x00,0x00),(0xd4,0x00,0x00),(0xff,0x00,0x00),(0xff,0x01,0x01),(0xd6,0x0c,0x0c),(0xe4,0x00,0x00),(0xff,0x1f,0x20),(0xff,0x0e,0x0e),(0xb8,0x02,0x02),(0xff,0x0a,0x0a),(0xff,0x00,0x00),(0xf4,0x00,0x00),(0xa3,0x00,0x00),(0x31,0x00,0x00),(0x01,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x40,0x00,0x00),(0xb3,0x00,0x00),(0xf7,0x00,0x00),(0xff,0x00,0x00),(0xea,0x00,0x01),(0xe4,0x00,0x00),(0xff,0x55,0x55),(0xff,0x49,0x49),(0xd2,0x00,0x00),(0xfc,0x00,0x00),(0xff,0x00,0x00),(0xe5,0x00,0x00),(0x94,0x00,0x00),(0x28,0x00,0x00),(0x01,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x1e,0x00,0x00),(0x88,0x00,0x00),(0xda,0x00,0x00),(0xfd,0x00,0x00),(0xea,0x00,0x00),(0xee,0x0a,0x0a),(0xff,0x97,0x98),(0xff,0xa0,0xa0),(0xee,0x11,0x11),(0xef,0x00,0x00),(0xf7,0x00,0x00),(0xc7,0x00,0x00),(0x7e,0x00,0x00),(0x1e,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x04,0x00,0x00),(0x57,0x00,0x00),(0xaa,0x00,0x00),(0xde,0x00,0x00),(0xc9,0x00,0x00),(0xf8,0x19,0x19),(0xff,0xa9,0xa9),(0xff,0xbf,0xbf),(0xfb,0x29,0x2a),(0xcd,0x00,0x00),(0xd4,0x00,0x00),(0xa0,0x00,0x00),(0x5e,0x00,0x00),(0x0e,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x21,0x00,0x00),(0x6c,0x00,0x00),(0xa2,0x00,0x00),(0x84,0x00,0x00),(0xe6,0x02,0x02),(0xff,0x3a,0x3a),(0xff,0x43,0x43),(0xec,0x05,0x04),(0x8f,0x00,0x00),(0x93,0x00,0x00),(0x65,0x00,0x00),(0x2b,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x0b,0x00,0x00),(0x29,0x00,0x00),(0x30,0x00,0x00),(0x4c,0x00,0x00),(0x95,0x00,0x00),(0xa0,0x00,0x00),(0x61,0x00,0x00),(0x1a,0x00,0x00),(0x10,0x00,0x00),(0x03,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)],
        [(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00),(0x00,0x00,0x00)]]

    pyTermTk = [
        "         ████████╗            ████████╗    ",
        "         ╚══██╔══╝            ╚══██╔══╝    ",
        "            ██║  ▄▄  ▄ ▄▄ ▄▄▖▄▖  ██║ █ ▗▖  ",
        "    ▞▀▚ ▖▗  ██║ █▄▄█ █▀▘  █ █ █  ██║ █▟▘   ",
        "    ▙▄▞▐▄▟  ██║ ▀▄▄▖ █    █ ▝ █  ██║ █ ▀▄  ",
        "    ▌    ▐  ╚═╝                  ╚═╝       ",
        "      ▚▄▄▘                                 "]

    __slots__=('_image')
    def __init__(self, *args, **kwargs):
        TTkWindow.__init__(self, *args, **kwargs)
        self._name = kwargs.get('name' , 'TTkAbout' )
        self._image = TTkImage(parent=self, pos=(0,0), data=TTkAbout.peppered)
        if not self.getTitle():
            self.setTitle('About...')
        self.resize(55,15)

    def paintEvent(self):
        c = [0xFF,0xFF,0xAA]
        for y, line in enumerate(TTkAbout.pyTermTk):
            self._canvas.drawText(pos=(9,3+y),text=line, color=TTkColor.fg(f'#{c[0]:02X}{c[1]:02X}{c[2]:02X}'))
            c[2]-=0x11
        self._canvas.drawText(pos=(20,9),text=f"  Version: {TTkCfg.version}", color=TTkColor.fg('#AAAAFF'))
        self._canvas.drawText(pos=(12,11),text=f"Powered By, Eugenio Parodi")
        self._canvas.drawText(pos=(2,13),text=f"https://github.com/ceccopierangiolieugenio/pyTermTk", color=TTkColor.fg('#44FFFF'))

        TTkWindow.paintEvent(self)
