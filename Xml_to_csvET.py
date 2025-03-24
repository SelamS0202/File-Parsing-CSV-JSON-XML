# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:54:49 2020

@author: selam
"""
import csv
import xml.etree.ElementTree as ET
tree = ET.parse("F:/LDS/LDS_2020/Data2020_21/collection_data/census_elements.xml")
root = tree.getroot()
col_lst = ["id", "age","workclass","fnlwgt",
         "education", "education-num", "marital-status", 
         "occupation","relationship", "race",
         "sex", "capital-gain", "capital-loss",
         "hours-per-week", "native-country","class"]
#for child in  root:
# print(child.tag, child.attrib)
row = []
for cens in tree.findall("census"):
    for element in col_lst:
        record = cens.find(element)
        if record is None:
            row.append("?")
        else:
            val = record.text
            row.append(val)
    with open("F:/LDS/LDS_2020/Data2020_21/census_elementsET.csv", "a") as f1:
        csv_w = csv.writer(f1)
        csv_w.writerow(row)
    row = []
    
    
            
        
    
    
    
    
#for t in tree.findall("census"):
    