# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Conditional modemap] Swap Ctrl and Cmd except for terminal
#define_conditional_modmap(lambda wm_class: wm_class in ("firefox"), {
#    Key.LEFT_META: Key.LEFT_CTRL,
#    Key.LEFT_CTRL: Key.LEFT_META,
#    Key.RIGHT_META: Key.RIGHT_CTRL
#})

# [Conditional keybindings] Terminal
define_keymap(re.compile("firefox"), {
    # Keep Ctrl terminal controls and add Cmd as Ctrl+Shift
    K("Super-q"): K("Ctrl-q"),
    K("Super-w"): K("Ctrl-w"),
    K("Super-e"): K("Ctrl-e"),
    K("Super-r"): K("Ctrl-r"),
    K("Super-t"): K("Ctrl-t"),
    K("Super-z"): K("Ctrl-z"),
    K("Super-u"): K("Ctrl-u"),
    K("Super-i"): K("Ctrl-i"),
    K("Super-o"): K("Ctrl-o"),
    K("Super-p"): K("Ctrl-p"),
    K("Super-a"): K("Ctrl-a"),
    K("Super-s"): K("Ctrl-s"),
    K("Super-d"): K("Ctrl-d"),
    K("Super-f"): K("Ctrl-f"),
    K("Super-g"): K("Ctrl-g"),
    K("Super-h"): K("Ctrl-h"),
    K("Super-j"): K("Ctrl-j"),
    K("Super-k"): K("Ctrl-k"),
    K("Super-l"): K("Ctrl-l"),
    K("Super-y"): K("Ctrl-y"),
    K("Super-x"): K("Ctrl-x"),
    K("Super-c"): K("Ctrl-c"),
    K("Super-v"): K("Ctrl-v"),
    K("Super-b"): K("Ctrl-b"),
    K("Super-n"): K("Ctrl-n"),
    K("Super-m"): K("Ctrl-m"),
    K("Super-minus"): K("Ctrl-minus"),	
    K("Super-key_0"): K("Ctrl-key_0"),
    K("Super-key_1"): K("Alt-key_1"),
    K("Super-key_2"): K("Alt-key_2"),
    K("Super-key_3"): K("Alt-key_3"),
    K("Super-key_4"): K("Alt-key_4"),
    K("Super-key_5"): K("Alt-key_5"),
    K("Super-key_6"): K("Alt-key_6"),
    K("Super-key_7"): K("Alt-key_7"),
    K("Super-key_8"): K("Alt-key_8"),
    K("Super-key_9"): K("Alt-key_9"),
    K("Super-Space"): K("Ctrl-Space")
}, "Terminal")
