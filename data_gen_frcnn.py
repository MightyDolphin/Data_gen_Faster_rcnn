# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:04:02 2021

@author: yunus
"""

import random
import pprint
import sys
import time
import numpy as np
import cv2
input_path="./json"
import os
import json
def get_data(input_path):

    annotation_path=input_path
    files = sorted(os.listdir(annotation_path))
    
    found_bg = False
    all_imgs = {}
    
    classes_count = {}
    
    class_mapping = {}
    counter=0
    visualise = True
    for i in files:
        name=i[:-5]    
        f= open("./json/"+i)   
        data=json.load(f)
          
        # represents the top left corner of rectangle
        shapes=data['shapes']
        end_points =[]
        start_points=[]
        for i in shapes:
            points=i['points']
            points[0][0]=int(points[0][0])
            points[0][1]=int(points[0][1])
        
            start_points.append(points[0])
            points[1][0]=int(points[1][0])
            points[1][1]=int(points[1][1])
            end_points.append(points[1])
            counter+=1
            
        w=600
        h=600
        le=len(end_points)
        for i in range(le):
            start=start_points[i]
            start_x=start[0]
            start_y=start[1]
            end=end_points[i]
            end_x=end[0]
            end_y=end[1]    
    
            
        x1=start_x
        y1=start_y
        x2=end_x
        y2=end_y

        filename=name+'.jpg'
        all_imgs[filename] = {}
        all_imgs[filename]['filepath'] = filename

        all_imgs[filename]['width'] = 600
        all_imgs[filename]['height'] = 600
        all_imgs[filename]['bboxes'] = []	
        all_imgs[filename]['bboxes'].append({'class': 'th', 'x1': int(x1), 'x2': int(float(x2)), 'y1': int(float(y1)), 'y2': int(float(y2))})

    
    all_data = []
    classes_count["ty"] =counter 
    class_mapping={'th': 0}
    for key in all_imgs:
        all_data.append(all_imgs[key])
    return all_data, classes_count, class_mapping
a=get_data(input_path)