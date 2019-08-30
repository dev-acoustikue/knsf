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


import requests
from bs4 import BeautifulSoup # parser

import copy

# User
from knsf_module.KnsfConfig import *
from knsf_module.KnsfContainer import *

# Explanation:
# html request process is already contained in parser.
# What the parser need is just url.


# 
# Author: acoustikue
class KnsfHtml:

    # This is where html text will be held.
    # html_text = ''

    def __init__(self, url):

        request_obj = requests.get(url)
        print('\tResponse: [' + str(request_obj.status_code) + ']')

        #
        # Individual Var
        self.html_text = request_obj.text


# 
# Author: acoustikue
# Type 1, five attributes
class KnsfKensParser(KnsfHtml):

    # will be held.
    # class variable, shared!!
    # knsf_container = None

    #
    # Parse when constructor is called.
    # type 1
    def __init__(self, url):

        # GET request!!
        super().__init__(url)


        # Returns data in this form
        # literally works as a structure.
        # Deep copy necessary.
        # knsf_container = KnsfKensContainer()

        json_form = {
            'no': '',
            'title': '', 
            'acc': '',
            'date': '',
            'vis': ''
            } # only lends the structure.

        json_list = [] # Push push!!

        # Set first, 
        knsf_soup = BeautifulSoup(self.html_text, 'html.parser')
        knsf_soup = BeautifulSoup(str(knsf_soup.find('table', class_='grid')), 'html.parser') # And set again, 
            # since the text is too long. Hard to debug.
        
        raw_data = knsf_soup.find_all('td')

        # column
        column = 0

        for set_ in raw_data:

            # Reset
            if(column is 5): column = 0

            if column is 0: json_form['no'] = str(set_.text.lstrip()).rstrip() 
            if column is 1: 
                json_form['title'] = str(set_.text.lstrip()).rstrip()
                # json_form['TITLE'] = str(info.text.lstrip().replace('\n', ''))
                # Memo: if parsed, there will be always '\n' at the end of every title.

            if column is 2: json_form['acc'] = str(set_.text.lstrip()).rstrip()
            if column is 3: json_form['date'] = str(set_.text.lstrip()).rstrip()
            if column is 4: 
                json_form['vis'] = set_.text.lstrip().rstrip()
                
                json_list.append(copy.deepcopy(json_form)) # push push!!
            
            column += 1
        
        #
        # Individual Var
        # When done parsing, 
        self.knsf_container = KnsfKensContainer() # call constructor

        self.knsf_container.setDataJsonList(copy.deepcopy(json_list))

        # Done.





# 
# Author: acoustikue
# Type 1, five attributes
class KnsfKnsParserType1(KnsfHtml):

    #
    # Parse when constructor is called.
    # type 1
    def __init__(self, url):

        # GET request!!
        super().__init__(url)


        # Returns data in this form
        # literally works as a structure.
        # Deep copy necessary.
        # knsf_container = KnsfKensContainer()

        json_form = {
            'no': '',
            'div': '', 
            'title': '',
            'date': '',
            'vis': ''
            } # only lends the structure.

        json_list = [] # Push push!!

        # Set first, 
        knsf_soup = BeautifulSoup(self.html_text, 'html.parser')
        knsf_soup = BeautifulSoup(str(knsf_soup.find('table', class_='list')), 'html.parser') # And set again, 
            # since the text is too long. Hard to debug.
        
        raw_data = knsf_soup.find_all('td')
        
        # column
        column = 0

        for set_ in raw_data:

            # Reset
            if(column is 5): column = 0

            if column is 0: 
                if str(set_.text.lstrip()) == '':
                    json_form['no'] = 'NA'

                else: json_form['no'] = str(set_.text.lstrip()).rstrip() 

            if column is 1: json_form['div'] = str(set_.text.lstrip()).rstrip()
            if column is 2: json_form['title'] = str(set_.text.lstrip()).rstrip()
                # json_form['TITLE'] = str(info.text.lstrip().replace('\n', ''))
                # Memo: if parsed, there will be always '\n' at the end of every title.
            if column is 3: json_form['date'] = str(set_.text.lstrip()).rstrip()
            if column is 4: 
                json_form['vis'] = set_.text.lstrip().rstrip()
                json_list.append(copy.deepcopy(json_form)) # push push!!

            column += 1


        # When done parsing, 
        self.knsf_container = KnsfKnsContainerType1() # call constructor

        self.knsf_container.setDataJsonList(copy.deepcopy(json_list))

        # Done.
    


# 
# Author: acoustikue
# Type 2, four attributes
class KnsfKnsParserType2(KnsfHtml):

        # will be held.
    #knsf_container = None

    #
    # Parse when constructor is called.
    # type 1
    def __init__(self, url):

        # GET request!!
        super().__init__(url)


        # Returns data in this form
        # literally works as a structure.
        # Deep copy necessary.
        # knsf_container = KnsfKensContainer()

        json_form = {
            'no': '',
            'title': '',
            'date': '',
            'vis': ''
            } # only lends the structure.

        json_list = [] # Push push!!

        # Set first, 
        knsf_soup = BeautifulSoup(self.html_text, 'html.parser')
        knsf_soup = BeautifulSoup(str(knsf_soup.find('table', class_='list')), 'html.parser') # And set again, 
            # since the text is too long. Hard to debug.
        
        raw_data = knsf_soup.find_all('td')

        # column
        column = 0

        for set_ in raw_data:

            # Reset
            if(column is 4): column = 0

            if column is 0: 
                if str(set_.text.lstrip()) == '':
                    json_form['no'] = 'NA'

                else: json_form['no'] = str(set_.text.lstrip()).rstrip() 

            #if column is 1: json_form['div'] = str(set_.text.lstrip()).rstrip()
            if column is 1: json_form['title'] = str(set_.text.lstrip()).rstrip()
                # json_form['TITLE'] = str(info.text.lstrip().replace('\n', ''))
                # Memo: if parsed, there will be always '\n' at the end of every title.
            if column is 2: json_form['date'] = str(set_.text.lstrip())
            if column is 3: 
                json_form['vis'] = set_.text.lstrip().rstrip()
                
                json_list.append(copy.deepcopy(json_form)) # push push!!
            
            column += 1

        #print(json_list)

        # When done parsing, 
        self.knsf_container = KnsfKnsContainerType2() # call constructor

        self.knsf_container.setDataJsonList(copy.deepcopy(json_list))


# Note!!
# Type1 - Haksa, Guukjae, Haksaeng, Ilban
# Type2 - Janghak, 
if __name__ == '__main__':
    
    # First print banner
    print(KNSF_PROJECT_BANNER)
    print('\tExecuting KnsfParser script. Running in debug mode.\n')
    print('\tExecute KnsfParserCaller script for debug and unit test.')

    pass