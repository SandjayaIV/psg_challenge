#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:47:49 2019

@author: stanislas

source :
https://python-django.dev/page-xml-python-xpath
"""

#%%

import os
import xml.etree.ElementTree as ET


#%% file
path = "/home/stanislas/Documents/Agorize/psg_challenge/fichier test 2.xml"
file = os.path.join(path)

tree = ET.parse(file)
root = tree.getroot()
#%%
root.attrib
root.tag
#%%

for children in root:
    for event in children.iter('Event'):
        print(event.tag,":", event.attrib,"\n")
        """
        for q in event.iter('Q'):
            print(q.tag,":",q.attrib,"\n")
         """   

#%%
event = [[[event.attrib],[q.attrib]] for event in root.iter('Event') for q in event]
#%%
import xmltodict 
import json

xml = open(file)
xml_content = xml.read()
x = xmltodict.parse(xml_content)
j = json.dumps(x)
json_file = j.replace("@",'')
dic = json.loads(json_file)

#%% dataframe
import pandas as pd
df = pd.DataFrame.from_dict(dic,orient='index').rename_axis(['Game'])