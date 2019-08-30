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
# KnsfConfig.py

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


import os
import platform
import copy



# Here the module's base directory will be set to folder where it is located.
# Every config files and other saved files must be in folder below the base directory.

KNSF_PROJECT_CODE = 'knsff_rpi'
KNSF_PROJECT_OS = 'Windows'
KNSF_PROJECT_SYS = ''
KNSF_PROJECT_VERSION = '0.1.0va'

KNSF_CURRENT_CODE = 'knsff_wnd'
KNSF_CURRENT_OS = str(platform.system())
KNSF_CURRENT_SYS = KNSF_CURRENT_OS + ' ' + str(platform.release()) + ' ' + str(platform.version())


KNSF_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNSF_DB_DIR = ''
KNSF_MESSAGE_DIR = ''


if KNSF_CURRENT_OS == 'Windows':
    KNSF_DB_DIR = KNSF_BASE_DIR + '\\db\\'
    KNSF_MESSAGE_DIR = KNSF_BASE_DIR + '\\fcm_message\\'
elif KNSF_CURRENT_OS == 'Linux': 
    KNSF_DB_DIR = KNSF_BASE_DIR + '/db/'
    KNSF_MESSAGE_DIR = KNSF_BASE_DIR + '/fcm_message/'


# First!!
# Make directory if there is no db folder
if not(os.path.isdir(KNSF_DB_DIR)): os.makedirs(os.path.join(KNSF_DB_DIR))
if not(os.path.isdir(KNSF_MESSAGE_DIR)): os.makedirs(os.path.join(KNSF_MESSAGE_DIR))



KNSF_PROJECT_BANNER = '[knsff] ' + KNSF_PROJECT_CODE + ', ' + KNSF_PROJECT_VERSION
KNSF_PROJECT_BANNER += (', ' + KNSF_CURRENT_SYS + '\n\tCopyright (C) 2019 SukJoon Oh')


# Whether to enable KENS service
KENS_ENABLE = True

# Using previous project names.
KNSF_EX_KNS_HAKSA = KNSF_DB_DIR + 'DB_HAKSA.KNSF'
KNSF_EX_KNS_JANGHAK = KNSF_DB_DIR + 'DB_JANGHAK.KNSF'
KNSF_EX_KNS_CHANGUP = KNSF_DB_DIR + 'DB_CHANGUP.KNSF'
KNSF_EX_KNS_GUUKJAE = KNSF_DB_DIR + 'DB_GUUKJAE.KNSF'
KNSF_EX_KNS_HAKSAENG = KNSF_DB_DIR + 'DB_HAKSAENG.KNSF'
KNSF_EX_KNS_SANHAK = KNSF_DB_DIR + 'DB_SANHAK.KNSF'
KNSF_EX_KNS_ILBAN = KNSF_DB_DIR + 'DB_ILBAN.KNSF'

# FCM Related files
KNSF_EX_FCM_USER = KNSF_DB_DIR + 'DB_FCM_USER.KNSF'
# KNSF_EX_FCM_API_KEY = KNSF_DB_DIR + 'DB_FCM_API_KEY.KNSF' # sender
KNSF_EX_FCM_SERVER_KEY = KNSF_DB_DIR + 'DB_FCM_SERVER_KEY.KNSF' # pyfcm

KNSF_EX_KENS = KNSF_DB_DIR + 'DB_EE.KNSF' # Name of the file which will be exported.

#
# Utility folder #1 fcm_message
# Make the folder, and message file names might vary.
KNSF_EX_FCM_MESSAGE = KNSF_DB_DIR + 'FCM_MESSAGE.KNSF'


# Initializing code.
# If files mentioned above does not exist, make them.
if not(os.path.isfile(KNSF_EX_FCM_USER)):
    with open(KNSF_EX_FCM_USER, "w"):
        pass

if not(os.path.isfile(KNSF_EX_FCM_SERVER_KEY)):
    with open(KNSF_EX_FCM_SERVER_KEY, "w"):
        pass

if not(os.path.isfile(KNSF_EX_KENS)):
    with open(KNSF_EX_KENS, "w"):
        pass

if not(os.path.isfile(KNSF_EX_FCM_MESSAGE)):
    with open(KNSF_EX_FCM_MESSAGE, "w"):
        pass


# Exported file lists.
KNSF_EX_KNS_L = [ copy.deepcopy(KNSF_EX_KNS_HAKSA),
                 copy.deepcopy(KNSF_EX_KNS_JANGHAK),
                 copy.deepcopy(KNSF_EX_KNS_CHANGUP),
                 copy.deepcopy(KNSF_EX_KNS_GUUKJAE),
                 copy.deepcopy(KNSF_EX_KNS_HAKSAENG),
                 copy.deepcopy(KNSF_EX_KNS_SANHAK),
                 copy.deepcopy(KNSF_EX_KNS_ILBAN)                
                 ]

for FILE in KNSF_EX_KNS_L:
    if os.path.isfile(FILE): pass
    else: 
        with open(FILE, "w"):
            pass



# 
# This is urls of notice boards.
KNSF_URL_KNS_HAKSA = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300001' # Haksa
KNSF_URL_KNS_JANGHAK = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=11688412' # Janghak
KNSF_URL_KNS_CHANGUP = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=11731332' # Changup
KNSF_URL_KNS_GUUKJAE = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300002' # Guukjae
KNSF_URL_KNS_HAKSAENG = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300003' # Haksaeng
KNSF_URL_KNS_SANHAK = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=65659&cat=0010300001' # Sanhak
KNSF_URL_KNS_ILBAN = 'http://www.konkuk.ac.kr/do/MessageBoard/ArticleList.do?forum=notice&cat=0000300006' # Iilban

KNSF_URL_KENS = 'http://ee.konkuk.ac.kr/noticeList.do?siteId=EE&boardSeq=424&menuSeq=2837' # EE



# lists.
KNSF_REQUEST_URL_L = [ copy.deepcopy(KNSF_URL_KNS_HAKSA),
                 copy.deepcopy(KNSF_URL_KNS_JANGHAK),
                 copy.deepcopy(KNSF_URL_KNS_CHANGUP),
                 copy.deepcopy(KNSF_URL_KNS_GUUKJAE),
                 copy.deepcopy(KNSF_URL_KNS_HAKSAENG),
                 copy.deepcopy(KNSF_URL_KNS_SANHAK),
                 copy.deepcopy(KNSF_URL_KNS_ILBAN)                
                 ]


if KENS_ENABLE is True:
    KNSF_REQUEST_URL_L.append(copy.deepcopy(KNSF_URL_KENS))



# Scripts
# platform

# Make sure to print just necessary information, for simple logs.
# print(KNSF_PROJECT_BANNER)


# 
# Parameter: -
# Returns: -
# Author: acoustikue
def KnsfShowConfig():

    #if KENS_ENABLE is True:
    #    print('\tKENS_ENABLE(1). KENS module will be loaded.')

    print('Config:')

    print('\tKNSF_PROJECT_CODE   \t' + KNSF_PROJECT_CODE)
    print('\tKNSF_PROJECT_OS     \t' + KNSF_PROJECT_OS)
    print('\tKNSF_PROJECT_SYS    \t' + KNSF_PROJECT_SYS)
    print('\tKNSF_PROJECT_VERSION\t' + KNSF_PROJECT_VERSION)

    print('\tKNSF_CURRENT_CODE   \t' + KNSF_CURRENT_CODE)
    print('\tKNSF_CURRENT_OS     \t' + KNSF_CURRENT_OS)
    print('\tKNSF_CURRENT_SYS    \t' + KNSF_CURRENT_SYS)

    print('\tKNSF_BASE_DIR       \t' + KNSF_BASE_DIR)
    print('\tKNSF_DB_DIR         \t' + KNSF_DB_DIR)

    print('\tKENS_ENABLE         \t' + str(KENS_ENABLE))
    print('\tKNSF_EX_KNS_HAKSA   \t' + KNSF_EX_KNS_HAKSA)
    print('\tKNSF_EX_KNS_JANGHAK \t' + KNSF_EX_KNS_JANGHAK)
    print('\tKNSF_EX_KNS_CHANGUP \t' + KNSF_EX_KNS_CHANGUP)
    print('\tKNSF_EX_KNS_GUUKJAE \t' + KNSF_EX_KNS_GUUKJAE)
    print('\tKNSF_EX_KNS_HAKSAENG\t' + KNSF_EX_KNS_HAKSAENG)
    print('\tKNSF_EX_KNS_SANHAK  \t' + KNSF_EX_KNS_SANHAK)
    print('\tKNSF_EX_KNS_ILBAN   \t' + KNSF_EX_KNS_ILBAN)
    print('\tKNSF_EX_FCM_USER    \t' + KNSF_EX_FCM_USER)
    print('\tKNSF_EX_FCM_SERVER_KEY\t' + KNSF_EX_FCM_SERVER_KEY)
    print('\tKNSF_EX_KENS        \t' + KNSF_EX_KENS)

    print('\tKNSF_EX_FCM_MESSAGE \t' + KNSF_EX_FCM_MESSAGE)

    print('\tKNSF_URL_KNS_HAKSA   \t' + KNSF_URL_KNS_HAKSA)
    print('\tKNSF_URL_KNS_JANGHAK \t' + KNSF_URL_KNS_JANGHAK)
    print('\tKNSF_URL_KNS_CHANGUP \t' + KNSF_URL_KNS_CHANGUP)
    print('\tKNSF_URL_KNS_GUUKJAE \t' + KNSF_URL_KNS_GUUKJAE)
    print('\tKNSF_URL_KNS_HAKSAENG\t' + KNSF_URL_KNS_HAKSAENG)
    print('\tKNSF_URL_KNS_SANHAK  \t' + KNSF_URL_KNS_SANHAK)
    print('\tKNSF_URL_KNS_ILBAN   \t' + KNSF_URL_KNS_ILBAN)
    print('\tKNSF_URL_KENS        \t' + KNSF_URL_KENS)




# Executing this script?
if __name__ == '__main__':

    # First print banner
    print(KNSF_PROJECT_BANNER)
    print('\tExecuting KnsfConfig script. Running in debug mode.\n')

    # Show configuration variables
    KnsfShowConfig()



