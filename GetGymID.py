#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

__author__ = "x"
__date__ = '1/2018'
__email__ = "x"

href = []
regex_list = []
gymnames = []
gymnames2 = []
gymnames_id_dict = {}

if __name__ == "__main__":
    def getgymid():
        global gymnames_id_dict
        lectio = requests.get('https://www.lectio.dk/lectio/login_list.aspx?forcemobile=1')
        soup = BeautifulSoup(lectio.content, 'lxml')

        # Få fat i gymnasie navnene:
        gyms = soup.find_all('div', id="schoolsdiv")
        [gymnames2.append(gyms[0].contents[x].string.strip()) for x in range(len(gyms[0].contents))]
        gymnames = [x for x in gymnames2 if x]
        if 'Vis alle skoler' in gymnames:
            gymnames.pop(gymnames.index('Vis alle skoler'))

        # Find id:
        [href.append(a['href']) for a in soup.find_all('a', href=True)]
        if 'login_list.aspx?showall=1' in href:
            href.pop(href.index('login_list.aspx?showall=1'))
        [regex_list.append(re.findall(r'\d+', x)) for x in href]
        id_list = [item for sublist in regex_list for item in sublist]
        if len(gymnames) == len(id_list):
            gymnames_id_dict = dict(zip(gymnames, id_list))
        else:
            print('Fejl i længde af listerne')
        return gymnames_id_dict


#id_dict = getgymid()
#print(id_dict)
