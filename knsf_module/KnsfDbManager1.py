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


from KnsfConfig import *
from KnsfContainer import *

import json
from collections import OrderedDict


# In KNSF project, database extension will be set to .knsf
# but the form is simple json file.
# 
# This is the form
# {
#    "type": "some_type",
#    "data": [
#        {
#            'no': '',
#            'title': '',
#            'date': '',
#            'vis': ''
#            }, # Now this form is from the KnsfParser
#        {
#            'no': '',
#            'title': '',
#            'date': '',
#            'vis': ''
#            }
#        ] # will be list.
#    }
#


# parent
# Author: acoustikue
class KnsfDbManager:

    # 
    # Be careful with class variables

    type = ''

    def __init__(self, file_addr):

        # Database file address,
        # This info is in KnsfConfig.py
        self.file_addr = file_addr

        # open file!
        with open(self.file_addr, "r") as db_file:
            
            # db_data = json.dumps()

            if db_data == '': 
                # Empty data means it was initialized with script.
                pass



            pass
        
        pass


# Author: acoustikue
class KnsfKensDbManager(KnsfDbManager):

    # 
    # Be careful with class variables

    def __init__(self):

        super().__init__()

        # Not that important
        # just for distinguishing attributes.
        self.type = 'KENS'
        

        pass


# Author: acoustikue
class KnsfKnsDbManagerType1(KnsfDbManager):

    # 
    # Be careful with class variables

    def __init__(self):

        super().__init__()

        self.type = 'KNS_1'

        pass

# Author: acoustikue
class KnsfKnsDbManagerType2(KnsfDbManager):

    # 
    # Be careful with class variables

    def __init__(self):

        super().__init__()

        pass
















