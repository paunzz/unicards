# Copyright 2013 Luke Macken <lmacken@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Converts strings into unicode playing cards
"""

import sys

if sys.version_info.major == 3:
    unichr = chr

# Input values and their corresponding unicode hex values
FACES = 'A23456789TJCQK', '123456789ABCDE'
SUITS = 'SHDC', 'ABCD'

# ANSI color escape codes
COLORS = ['\x1b[%dm' % c for c in (30, 31, 34, 32, 39)]


def unicard(card, color=False):
    if card[:2] == '10':
        card = 'T' + card[2]
    face, suit = card.upper()
    c = unichr(int("0001f0{}{}".format(
        SUITS[1][SUITS[0].index(suit)],
        FACES[1][FACES[0].index(face)]
    ), base=16))
    if color:
        c = COLORS[SUITS[0].index(suit)] + c + COLORS[-1]
    return c
