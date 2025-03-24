# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:57:48 2020

@author: selam
"""
#import xml.dom.minidom as minidom
import csv
from xml.dom.minidom import parse
tree = parse("F:/LDS/LDS_2020/Data2020_21/collection_data/census_elements.xml")
print(tree.documentElement.tagName)
census_list = tree.getElementsByTagName("census")
col_list = ['id','age', 'workclass', 'fnlwgt','education',
            'education-num', 'marital-status','occupation',
            'relationship', 'race','sex','capital-gain',
            'capital-loss','hours-per-week','native-country',
            'class']
with open("F:/LDS/LDS_2020/Data2020_21/census_elements.csv", "a") as file:
    header_writer = csv.writer(file)
    header_writer.writerow(col_list)
row_value = []
for census in census_list:
    for col in col_list:
        if census.getElementsByTagName(col):
            data = census.getElementsByTagName(col)[0].childNodes[0].data
            row_value.append(data)
        else:
            row_value.append("?")
    with open("F:/LDS/LDS_2020/Data2020_21/census_elements.csv", "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row_value)
    row_value = []
         
            
    