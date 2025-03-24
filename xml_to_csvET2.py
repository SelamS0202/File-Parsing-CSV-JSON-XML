# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:36:23 2020

@author: selam
"""
import csv 
import xml.etree.ElementTree as ET
'''cols= ["class","native-country","hours-per-week","capital-loss","capital-gain",
       "sex", "race","relationship","occupation", "marital-status","education-num",
       "education","fnlwgt","workclass", "age","id"]'''
xml_tree = ET.parse("F:/LDS/LDS_2020/Data2020_21/collection_data/census_row.xml")
attrb_list =[ k for k, v in  xml_tree.find("row").attrib.items()]
with open("F:/LDS/LDS_2020/Data2020_21/census_ElemenetsET2.csv","a")as Ifile:
    csv_writer = csv.writer(Ifile)
    csv_writer.writerow(attrb_list)
#print(attrb_list)
line_value = []
for line in xml_tree.findall("row"):
    for c in attrb_list:
        if c in line.attrib:
            r = line.get(c)
            line_value.append(r)
        else:
            line_value.append("?")
    with open("F:/LDS/LDS_2020/Data2020_21/census_ElemenetsET2.csv","a") as file:
        csv_writer2 = csv.writer(file)
        csv_writer2.writerow(line_value)
    line_value= []
        
    