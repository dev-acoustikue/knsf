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

from KnsfConfig import *
import copy


# parent
# Author: acoustikue
class KnsfContainer:
    
    # This is a base class which holds 'set' of information parsed from the page.
    # In other words, a single class holds list of titles, number of seen, etc.
    # Thus it needs to be implemented like, 
    # 
    # prev_info = KnsfContainer()
    # new_info = KnsfContainer()
    # 
    # Then compare the set.

    # Class variable
    #data_json_list = None
    #data_title_list = [] # will only hold title

    def convertTitleList(self):

        if self.data_json_list is not None:
            for json_form in self.data_json_list:
                self.data_title_list.append(copy.deepcopy(json_form['title']))

    # constructor
    def __init__(self):

        self.data_json_list = None
        self.data_title_list = []
        pass

    #def __str__(self):
    #    return 'KnsfContainer {number} held.'.format(number=len(self.title_list))


# Author: acoustikue
class KnsfKensContainer(KnsfContainer):

    type = 'KENS'
    
    def setDataJsonList(self, data_json):

        self.data_json_list = data_json
        self.convertTitleList()


    # constructor
    def __init__(self):
        super().__init__()

        # make list
        # self.setDataJsonList()


# Author: acoustikue
class KnsfKnsContainerType1(KnsfContainer):

    type = 'KNS_1'
    
    def setDataJsonList(self, data_json):

        self.data_json_list = data_json
        self.convertTitleList()

    # constructor
    def __init__(self):
        super().__init__()


# Author: acoustikue
class KnsfKnsContainerType2(KnsfContainer):

     type = 'KNS_2'
     
     def setDataJsonList(self, data_json):

        self.data_json_list = data_json
        self.convertTitleList()

     # constructor
     def __init__(self):
        super().__init__()














