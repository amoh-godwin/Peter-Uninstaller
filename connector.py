# -*- coding: utf-8 -*-
import threading
import platform
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from settings import Setts

if platform.system() == 'Windows':
    from uninstall import uninstall_win as uninstall_mod


class Connector(QObject):

    """
    """

    def __init__(self):
        QObject.__init__(self)
        self.setts = Setts()
        self.Uninst = uninstall_mod.Uninstaller(self.setts.parent_folder,
                                                self.setts.passcode,
                                                self.setts.server[1]['path'])

    def stop_server(self):
        stop_t = threading.Thread(target=self._stop_server)
        stop_t.daemon = True
        stop_t.start()

    def _stop_server(self):
        self.Uninst.stop_server()

    def del_files(self):
        del_t = threading.Thread(target=self._del_files)
        del_t.daemon = True
        del_t.start()

    def _del_files(self):
        self.Uninst.del_files()
