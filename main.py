# -*- coding: utf-8 -*-
import sys
from settings import Sets
from uninstall.uninstall_win import Uninstaller

setts = Sets()
Uninst = Uninstaller(setts.parent_folder, setts.passcode, setts.server[1]['path'])


Uninst.stop_server()

Uninst.del_files()

sys.exit(0)
