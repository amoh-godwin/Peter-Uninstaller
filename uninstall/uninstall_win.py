# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:17:15 2019

@author: Ampofo
"""

import subprocess
import os
import sys

class Uninstaller():


    def __init__(self, parent_folder, passcode, mysql_path):
        super.__init__
        self.install_path = parent_folder + '/bin'
        main_dir = os.path.dirname(sys.argv[0])
        self.passcode = passcode
        self.mysql_path = parent_folder + "/" + mysql_path
        print(self.mysql_path)
        self.main = main_dir.replace('\\install', '')

    def stop_server(self):

        cmd = '"' + self.mysql_path + 'mysqladmin" -u root --password='\
        + self.passcode + ' shutdown'

        subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         shell=True)

    def del_files(self):

        cmd1 = 'RD /S /Q "' + self.install_path + '/php' + '"'
        cmd2 = 'RD /S /Q "' + self.install_path + '/mysql' + '"'
        cmd3 = 'RD /S /Q "' + self.install_path + '"'

        out1 = subprocess.Popen(cmd1, shell=True)
        out2 = subprocess.Popen(cmd2, shell=True)
        out3 = subprocess.Popen(cmd3, shell=True)

    def uninstall_mysql_serv(self):

        cmd = "SC DELETE " + self.service[1]
        out1 = check_output(cmd, shell=True)


#WinUninstall()
