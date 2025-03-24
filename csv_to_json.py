# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:27:05 2020

@author: selam
"""
# get the last_row
# read each row using csv.DictReader
# dump the dictionary 
# iterate through the reader obj if it's the last row write("\n") else write("\n" + ",")

import json
import csv
last_row = 0
def get_last_row():
    with open("F:/LDS/LDS_2020/Data2020_21/census.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        last_row = sum([1 for i in csv_reader])
        last_row = last_row - 1
def csv_to_json():
    get_last_row()
    json_file = open("F:/LDS/LDS_2020/Data2020_21/census.json", "w")
    json_file.write("[")
    count = 0
    with open("F:/LDS/LDS_2020/Data2020_21/census.csv", "r") as f_reader:
        f_reader = csv.DictReader(f_reader,fieldnames =None, delimiter = "," )
        for line in f_reader:
            json.dump(line,json_file, indent = 4)
            if count < last_row:
                json_file.write("\n" + ",")
            else:
                json_file.write("\n")
            count+=1
    json_file.write("]")
    json_file.close() 

csv_to_json()

                
       
            
    
