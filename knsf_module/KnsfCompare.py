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
# KnsfDbManager1.py

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

from KnsfContainer import *
from copy import deepcopy

# Single!
def KnsfCompare(old_container, new_container):

    updated_list = [] # empty default.

    # 2 by 2 matrix 
    for new_list in new_container.data_title_list:
        # for old_list in old_container.data_title_list:

        if new_list in old_container.data_title_list:
            pass # found

        else:
            updated_list.append(deepcopy(new_list))

    return updated_list
