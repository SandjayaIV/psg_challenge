#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:11:54 2019

@author: stanislas
"""
import xml.etree.ElementTree as ET

tree1 = ET.parse('/home/stanislas/Documents/Agorize/psg_challenge/entrainemen.xml')
tree2 = ET.parse("""/home/stanislas/Documents/Agorize/psg_challenge/Exemple de fichier pour base de test avant modifications précisées dans les règles du jeu - f24-24-2016-853139-eventdetails_test_hackaton_1.xml"""                 )
root1 = tree1.getroot
a =1
root1 = tree1.getroot()
root2 = tree2.getroot()
root1.tag
root2.tag
root1.attrib
root2.attrib
for children in root1:
    print(children.tag, children.attrib)
for children in root1:
    print(children.tag, children.attrib)
for children in root2:
    print(children.tag, children.attrib)
for children in root2:
    print(children.tag)
for children in root2:
    for event in root2.iter('Event'):
        print("Event", event.attrib)
    for q in event.iter('Q'):
        print("Q", q.attrib, "\n")
#%%
[elem.tag for elem in root1.iter()]
[elem.tag for elem in root2]
[elem.tag for elem in root2.iter()]
[elem.tag for elem in root2.iter()][0:5]

ET.tostring(root2)
ET.tostring(root1)

#%% for event in root2.iter('Event'):
root2.attrib
event 
event.attrib

#%%
event = [[[event.attrib],[q.attrib]] for event in root2.iter('Event') for q in event]
#%%
import pandas as pd

df = pd.DataFrame(event, columns = ['event','q'])

#%% entrainement xml vers JSON
import pandas as pd
import json
import pprint
from xml.parsers.expat import ExpatError
file = "/home/stanislas/Documents/Agorize/psg_challenge/Exemple de fichier pour base de test avant modifications précisées dans les règles du jeu - f24-24-2016-853139-eventdetails_test_hackaton_1.xml"


with open('/home/stanislas/Documents/Agorize/psg_challenge/Exemple de fichier pour base de test avant modifications précisées dans les règles du jeu - f24-24-2016-853139-eventdetails_test_hackaton_1.xml') as fd:
    doc = xmltodict.parse(fd.read())
df = pd.DataFrame(doc, columns = doc.keys())
