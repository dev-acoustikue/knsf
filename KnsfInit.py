# [Project KNSF] Konkuk Notification Service with FCM, Project KENS/KNS with FCM
# 0.1.0va, 19.08.30. First launched, last update 19.08.30.
# written by acoustikue(SukJoon Oh)
#                                 __  _ __            
#    ____ __________  __  _______/ /_(_) /____  _____ 
#   / __ `/ ___/ __ \/ / / / ___/ __/ / //_/ / / / _ \
#  / /_/ / /__/ /_/ / /_/ (__  ) /_/ / ,< / /_/ /  __/
#  \__,_/\___/\____/\__,_/____/\__/_/_/|_|\__,_/\___/ 
#                                                     
# Visual Studio 2017 Professional Blank Python Project
# KnsfFcm.py

# This project requires pyfcm library, 
# thus first install it by
# $ pip3 install pyfcm

# In initial version, many of original KENS/KNS functions are refactored, 
# since KNSF can be distinguished by only methods of sending notifications to devices.

# KNSF used FCM for push service, and used Flask as a server for getting devices' tokens.
# In this source there is no relation with the Flask server.

# This project is also designed for running consistently on raspberry-pi, 
# a small scale home server.
# But it will also work on any other linux-based OS.

# This is main!!

from knsf_module.KnsfConfig import *
import os

# This file checks if all necessary files are in the right position.
# If any problem occurred when running upgraded version or 
# any other problem related to files, just run this script.
# It will reset all database files.


print(KNSF_PROJECT_BANNER)

# debug
# KnsfShowConfig()

print('Init:')

#
# Did all files located right?
print('\tChecking FCM database file... ', end='')

if not(os.path.isfile(KNSF_EX_FCM_USER)): print('KNSF_EX_FCM_USER(NOT FOUND)', end=', ')
else: print('KNSF_EX_FCM_USER(FOUND)', end=', ')

if not(os.path.isfile(KNSF_EX_FCM_SERVER_KEY)): print('KNSF_EX_FCM_SERVER_KEY(NOT FOUND)')
else: print('KNSF_EX_FCM_SERVER_KEY(FOUND)')


print('\tChecking notice database file... ', end='')
# Exported file lists.
for FILE in KNSF_EX_KNS_L:
    if os.path.isfile(FILE): pass
    else: print('FILE(NOT FOUND)', end=', ')

if not(os.path.isfile(KNSF_EX_KENS)): print('FILE(NOT FOUND)')
else: print('Done.')


print('\tConfiguration done.')



if __name__ == '__main__':

    pass