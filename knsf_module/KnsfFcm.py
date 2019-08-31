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
# $ pip3 install requests

# In initial version, many of original KENS/KNS functions are refactored, 
# since KNSF can be distinguished by only methods of sending notifications to devices.

# KNSF used FCM for push service, and used Flask as a server for getting devices' tokens.
# In this source there is no relation with the Flask server.

# This project is also designed for running consistently on raspberry-pi, 
# a small scale home server.
# But it will also work on any other linux-based OS.

# This is main!!
from KnsfConfig import * # manual
from KnsfContainer import *

from pyfcm import FCMNotification

import os
import copy

import requests



# https://iid.googleapis.com/v1/web/iid/KctODamlM4:CI2k_HHw...3P1
# https://developers.google.com/instance-id/reference/server#manage_registration_tokens_for_push_subscriptions
# DELETE request to delete registered device.
# x = requests.delete('https://w3schools.com/python/demopage.php')
# Syntax
# requests.delete(url, args)




# KnsfFcm class
# This object is used to set registered device information,
# tokens.
class KnsfFcm:
    
    # Parameter: String(file address)
    # Returns: -
    # Author: acoustikue
    def reloadDbDeviceToken(self, db_file_addr):

        if os.path.isfile(db_file_addr):
            with open(db_file_addr, "r", encoding="utf-8") as key_file: # Read file.

                list = key_file.readlines() # Read api key

                # if there are multiple keys, then something is wrong.
                if len(list) is 0: 
                    print('\tNo device token found.')

                else:
                    # print('\tServer API key found.')
                    print('Device:')

                    for user in list:
                        self.device_token_list.append(str(user).rstrip('\n')) # Remove \n 
                        print('\t' + str(user)[0:19] + '...')

        else: # file-does-not-exist case
            print('\tDevice token database file does not exist.')


    # Parameter: String
    # Returns: -
    # Author: acoustikue
    def addToken(self, device_token):
        self.device_token_list.append(str(device_token))


    # Parameter: -
    # Returns: list
    # Author: acoustikue
    def getTokenList(self):
        return self.device_token_list
    

    def __init__(self, db_file_addr):
        
        self.device_token_list = []
        # Device token will be read here.
        # No adding function, since this is not a real-time server.

        self.reloadDbDeviceToken(db_file_addr)




# KnsfFcmServer class
# This object is used to set FCM server information,
# and control(e.g. sending messages)
class KnsfFcmServer(KnsfFcm):

    # Parameter: String(file address)
    # Returns: -
    # Author: acoustikue
    def reloadDbApiKey(self, db_file_addr):

        if os.path.isfile(db_file_addr):
            with open(db_file_addr, "r", encoding="utf-8") as key_file: # Read file.

                list = key_file.readlines() # Read api key

                # if there are multiple keys, then something is wrong.
                if len(list) is 0: print('\tServer API key not found. Key will be set to empty string.')
                if len(list) is not 1: print('\tServer API key is not unique. Key will be set to empty string.')

                else:
                    # print('\tServer API key found.')
                    self.server_api_key = list[0].rstrip('\n') # Remove \n 

                    # Primary.
                    self.fcm_service = FCMNotification(api_key=self.server_api_key)

        else: # file-does-not-exist case
            print('\tServer API database file does not exist. Key will be set to empty string.')
            self.server_api_key = ''

    # Set key manually.

    # Parameter: String
    # Returns: -
    # Author: acoustikue
    def setKey(self, server_api_key):
        self.server_api_key = server_api_key

    # Parameter: -
    # Returns: String(API KEY)
    # Author: acoustikue
    def getKey(self):
        return self.server_api_key


    # Deprecated
    #def notifySingleDevice(self, message, click_action):
    #    pass

    def notifyMultipleDevice(self, m_title, m_body, action):

        print('\tPush:')

        for token in self.device_token_list:
            print('\t' + token[0:19] + '...')
        # send push!
        self.fcm_service.notify_multiple_devices(registration_ids=self.device_token_list, message_title=m_title, message_body=m_body, click_action=action)


    # Parameter: -
    # Returns: -
    # Author: acoustikue
    def deleteTokenFromServer(self, user_token):

        print('\tSending DELETE request to server.')
        requests.delete('https://iid.googleapis.com/v1/web/iid/' + self.server_api_key)

        # This function needs to be tested.
        # tentative.

    # 
    # constructor
    def __init__(self, db_device_token, db_api_key):

        self.server_api_key = ""
        # This key is used to control notification push,
        # the way to connect to FCM server.
        # Make sure to keep it safe to prevent control from others.
        self.fcm_service = None

        super().__init__(db_device_token)

        # Loading db file
        self.reloadDbApiKey(db_api_key) 
            # In this process, we get FCMNotification object set.




# Simple function
def KnsfMakeMessageBody(updated_list):

    message_body = ''

    for title in updated_list:
        message_body += title
        message_body += '\n'

    print(message_body)
    return message_body




#
# Test script.
if __name__ == '__main__':

    print(KNSF_PROJECT_BANNER)
    print('FCM:\tFCM module test.')

    # Object based.
    knsf_server = KnsfFcmServer(KNSF_EX_FCM_USER, KNSF_EX_FCM_SERVER_KEY)
    print('\tServer key set to: ' + knsf_server.getKey()[0:19] + '...')

    knsf_server.notifyMultipleDevice('네이버 링크', '테스트 푸시 입니다.', 'https://m.naver.com/')






