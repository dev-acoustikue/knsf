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
# Knsf.py

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

from KnsfParser import *

# ###########
# Functions

# 
# Parameter: -
# Returns: KnsfContainer derived class
# Author: acoustikue
def KnsfParseKnsHaksa():
    
    print('Parse:\n\tHaksa page parsing...')
    parser = KnsfKnsParserType1(KNSF_URL_KNS_HAKSA)

    return parser.knsf_container # Returns Type1

# 
# Parameter: -
# Returns: KnsfContainer derived class
# Author: acoustikue
def KnsfParseKnsGuukjae():
    
    print('Parse:\n\tGuukjae page parsing...')
    parser = KnsfKnsParserType1(KNSF_URL_KNS_GUUKJAE)

    return parser.knsf_container # Returns Type1

# 
# Parameter: -
# Returns: KnsfContainer derived class
# Author: acoustikue
def KnsfParseKnsHaksaeng():
    
    print('Parse:\n\tHaksaeng page parsing...')
    parser = KnsfKnsParserType1(KNSF_URL_KNS_HAKSAENG)

    return parser.knsf_container # Returns Type1

# 
# Parameter: -
# Returns: KnsfContainer derived class
# Author: acoustikue
def KnsfParseKnsIlban():
    
    print('Parse:\n\tHaksaeng page parsing...')
    parser = KnsfKnsParserType1(KNSF_URL_KNS_ILBAN)

    return parser.knsf_container # Returns Type1

# 
# Parameter: -
# Returns: KnsfContainer derived class
# Author: acoustikue
def KnsfParseKnsJanghak():
    
    print('Parse:\n\tJanghak page parsing...')
    parser = KnsfKnsParserType2(KNSF_URL_KNS_JANGHAK)

    return parser.knsf_container # Returns Type2

# 
# Parameter: -
# Returns: KnsfContainer derived class
# Author: acoustikue
def KnsfParseKens():
    
    print('Parse:\n\tEE page parsing...')
    parser = KnsfKensParser(KNSF_URL_KENS)

    return parser.knsf_container # Returns Type1



# Note!!
# Type1 - Haksa, Guukjae, Haksaeng, Ilban
# Type2 - Janghak, 
if __name__ == '__main__':
    
    # First print banner
    print(KNSF_PROJECT_BANNER)
    print('\tExecuting KnsfParserCaller script. Running in debug mode.\n')
    
    # How to use?
    # like this!
    knsf_container_haksa = KnsfParseKnsHaksa()
    knsf_container_guukjae = KnsfParseKnsGuukjae()
    knsf_container_Haksaeng = KnsfParseKnsHaksaeng()
    knsf_container_ilban = KnsfParseKnsIlban()
    knsf_container_janghak = KnsfParseKnsJanghak() # Type2

    knsf_container_ee = KnsfParseKens()


    # Debugging
    print('Haksa:')
    for title in knsf_container_haksa.data_title_list:
        print('\t' + title)

    print('Guukjae:')
    for title in knsf_container_guukjae.data_title_list:
        print('\t' + title)

    print('Haksaeng:')
    for title in knsf_container_Haksaeng.data_title_list:
        print('\t' + title)

    print('Ilban:')
    for title in knsf_container_ilban.data_title_list:
        print('\t' + title)

    print('Janghak:')
    for title in knsf_container_janghak.data_title_list:
        print('\t' + title)

    print('EE:')
    for title in knsf_container_ee.data_title_list:
        print('\t' + title)

    #print(knsf_container_haksa.data_json_list)
    pass

