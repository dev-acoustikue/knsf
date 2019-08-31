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
# 

# Now finally running script!

import os, sys

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

#
# Every recipe ready?
from KnsfConfig import *
from KnsfContainer import *
from KnsfDbManager1 import KnsfKnsDbManagerType1
from KnsfFcm import *
from KnsfParserCaller import KnsfParseKnsGuukjae
from KnsfCompare import KnsfCompare
# Rest? maybe later.
# 

# Run single script
# 
# practical main

print(KNSF_PROJECT_BANNER)

# so this is how we do it.
# 
# first, read database
db_manager = KnsfKnsDbManagerType1(KNSF_EX_KNS_GUUKJAE)

# parse necessary information
new_knsf_container = KnsfParseKnsGuukjae() 
old_knsf_container = db_manager.readDbService()

# Comparing process
updated_list = KnsfCompare(old_knsf_container, new_knsf_container)

# print(updated_list)

if len(updated_list) is not 0: # this means something has been updated.
    db_manager.updateDbService(new_knsf_container)

    # If there was no db, then 
    # sending alarm is not ideal.
    # This might happen due to update 
    if KNSF_DB_INIT_GUUKJAE is True:
        pass

    else:
        # 
        # and send notification via FCM push
        knsf_server = KnsfFcmServer(KNSF_EX_FCM_USER, KNSF_EX_FCM_SERVER_KEY)
        knsf_server.notifyMultipleDevice('국제 공지 업데이트', 
                                         KnsfMakeMessageBody(updated_list), 
                                         KNSF_URL_KNS_GUUKJAE)

else:
    pass

# done script





