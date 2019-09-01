# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:17:15 2019

@author: Ampofo
"""

from subprocess import check_output
import os
import sys

class WinUninstall():


    def __init__(self):
        super.__init__
        self.install_path = "C:\\Deuteronomy\\Peter"
        main_dir = os.path.dirname(sys.argv[0])
        self.passcode = 'ampofo1'
        self.main = main_dir.replace('\\install', '')
        self.service = ['PeterWebServer', 'MySQL573']
        self.uninstall_mysql_serv()
        self.del_files()

    def del_files(self):

        cmd1 = 'DEL /Q ' + self.main + '\\php' + "\\*.*"
        cmd2 = 'DEL /Q ' + self.main + '\\mysql' + '\\*.*'

        out1 = check_output(cmd1 + ' /E /Y', shell=True)
        out2 = check_output(cmd2 + ' /E /Y', shell=True)

    def uninstall_mysql_serv(self):

        cmd = "SC DELETE " + self.service[1]
        out1 = check_output(cmd, shell=True)


WinUninstall()
