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

# for debugging
from KnsfParserCaller import *
# functions from KnsfParserCaller returns KnsfContainer type.
# Thus, use the returned value as DAOs.

# Alas!

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
#            } ... and so on.
#        ] # will be list.
#    }
#


# parent
# Author: acoustikue
class KnsfDbManager:

    # 
    # Be careful with class variables

    # type = ''
    form = 'json'
    
    # reloadDb
    def __reloadDb(self, file_addr):
        print('\tDB file reload.')

        # open file!
        with open(self.file_addr, "r", encoding="utf-8",) as db_file:

            self.db = json.load(db_file) # load

            self.db_type = self.db['type']
            # self.db_data : Really necessary?
            self.db_data_list = self.db['data']

            #print('loaded -----------------')
            #print(self.db_data_list)
    

    # constructor
    def __init__(self, file_addr):

        # Database file address,
        # This info is in KnsfConfig.py
        self.type = 'Base'

        self.file_addr = file_addr

        self.db = None
        self.db_type = ''
        self.db_data_list = [] # empty

        # update
        self.__reloadDb(file_addr)



    
    # Util
    def getDb(self):
        return self.db

    def getDbType(self):
        return self.db_type

    def getDbDataList(self):
        return self.db_data_list



    # control db
    #
    def updateDbService(self, knsf_container):

        ordered_dict = self.generateDbJson(knsf_container)

        with open(self.file_addr, 'w', encoding="utf-8") as db_file:
            json.dump(ordered_dict, db_file)


    def generateDbJson(self, knsf_container):

        # Here generates json form which will be saved.
        #
        ordered_dict = OrderedDict()

        ordered_dict['type'] = knsf_container.type
        ordered_dict['data'] = knsf_container.data_json_list

        # print(ordered_dict)

        return ordered_dict






# Hello children!
# Author: acoustikue
class KnsfKensDbManager(KnsfDbManager):

    # 
    # Be careful with class variables

    def __init__(self, file_addr):
        super().__init__(file_addr)

        # Not that important
        # just for distinguishing attributes.
        self.type = 'KENS'
        
    # control db
    def readDbService(self):
        # this function returns container type

        knsf_container = KnsfKensContainer()
        knsf_container.setDataJsonList(self.db_data_list)

        return knsf_container


# Author: acoustikue
class KnsfKnsDbManagerType1(KnsfDbManager):

    # 
    # Be careful with class variables

    def __init__(self, file_addr):
        super().__init__(file_addr)

        self.type = 'KNS_1'

    # control db
    def readDbService(self):
        # this function returns container type

        knsf_container = KnsfKnsContainerType1()
        knsf_container.setDataJsonList(self.db_data_list)

        return knsf_container



# Author: acoustikue
class KnsfKnsDbManagerType2(KnsfDbManager):

    # 
    # Be careful with class variables

    def __init__(self, file_addr):
        super().__init__(file_addr)

    # control db
    def readDbService(self):
        # this function returns container type

        knsf_container = KnsfKnsContainerType2()
        knsf_container.setDataJsonList(self.db_data_list)

        return knsf_container





# 
# main, debug, unit test code
if __name__ == '__main__':

    print(KNSF_PROJECT_BANNER)
    print('\tExecuting KnsfDbManager1 script. Running in debug mode.\n')
    # print('\tExecute KnsfParserCaller script for debug and unit test.')

    knsf_container = KnsfParseKnsHaksa()
    
    db_manager_haksa = KnsfKnsDbManagerType1(KNSF_EX_KNS_HAKSA) # sample

    # print(db_manager_haksa.db)

    #print('db:\n\t' + str(db_manager_haksa.db))
    #print('db_type:\n\t' + str(db_manager_haksa.db_type))
    #print('db_data:\n\t' + str(db_manager_haksa.db_data_list))

    # db_manager_haksa.generateDbJson(knsf_container)

    # db_manager_haksa.updateDbService(knsf_container)

    # print()
    # print(knsf_container)

    print(db_manager_haksa.readDbService())

    


















