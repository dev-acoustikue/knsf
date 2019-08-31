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
from KnsfParserCaller import KnsfParseKnsHaksa
# Rest? maybe later.
# 

# Run single script
# 
# practical main

print(KNSF_PROJECT_BANNER)

# so this is how we do it.
# 
# first, read database
db_manager = KnsfKnsDbManagerType1(KNSF_EX_KNS_HAKSA)

# parse necessary information
new_knsf_container = KnsfParseKnsHaksa() 
old_knsf_container = db_manager.readDbService()

# Comparing process









