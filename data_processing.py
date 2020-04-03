#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  31 11:22:45 2020

@author: hongxueying
"""

import pandas as pd
import os
from glob import glob
import numpy as np 
import csv
import h5py as h5
import cv2

# import images
labels = pd.read_csv('/Users/hongxueying/Downloads/5703/dataset/NIH/sample/NIH_label.csv')

source = '/Users/hongxueying/Downloads/5703/dataset/NIH/sample/images'

#Sample_images = os.path.join(source, "sample", "images")


images = glob(os.path.join(source, "*.png"))
#print(images.type)

#------------------------------------------------------------------------------
#reduce useless information for label

Nor = pd.DataFrame(columns = ["Image Index", "Finding Labels", "Follow-up #", "Patient ID", "Patient Age","Patient Gender",
                              "View Position","OriginalImageWidth","OriginalImageHeight","OriginalImagePixelSpacing_x","OriginalImagePixelSpacing_y"])

for i in range(labels['Finding Labels'].size):
    if labels['Finding Labels'][i] == 'No Finding':        
         Nor = pd.concat([Nor,labels[i:i+1]])
    if labels['Finding Labels'][i] == 'Pneumonia':        
         Nor = pd.concat([Nor,labels[i:i+1]])

arry = Nor[["Image Index"]].values
arry_flat = arry.flatten()
print(arry_flat.size)

#------------------------------------------------------------------------------
#reduce useless information for images

new_image =[]
for i in range(arry_flat.size):
    for j in range(len(images)):
        temp = '/Users/hongxueying/Downloads/5703/dataset/NIH/sample/images/' + arry_flat[i]
        if temp == images[j]:
           #Nor = pd.concat([Nor,labels[i:i+1]])
           temp = cv2.resize(temp, (512,512))
           new_image.append(temp)
           
           



"""
new_image =[]
for i in range(arry_flat.size):
    for image in images:
        temp = '/Users/hongxueying/Downloads/5703/dataset/NIH/sample/images/' + arry_flat[i]
        if temp == image:
           #Nor = pd.concat([Nor,labels[i:i+1]])
           img = cv2.imread(image)
           img = cv2.resize(img, (512,512))
           new_image.append(img)
           
           
print(new_image)           
           
#print(new_image)
"""
"""
labels = []
imgs = []
for image in new_image:
    finding = Nor['Image Index'] == labels['Finding Labels'].values[0]
    if finding in 'No Finding':
        label = 1
    else:
        label = 0
    labels.append(label)
    img = cv2.imread(image)
    img = cv2.resize(img, (512,512))
    #img = img.reshape(786432)
    imgs.append(img)
"""

#------------------------------------------------------------------------------
#clean data for label

Nor.rename(columns=
            {"Image Index": "image",
            "Finding Labels": "labels",
            "Patient Age": "age",
            "Patient Gender": "gender",
            "View Position": "position",
            "OriginalImageWidth": "width",
            "OriginalImageHeight": "height",
            "OriginalImagePixelSpacing_x": "space_x",
            "OriginalImagePixelSpacing_y": "space_y"}, inplace=True)


Nor["gender"].replace(["F", "M"],[0, 1],inplace=True)

Nor["age"].replace("411Y", "041Y", inplace=True)
Nor["age"] = Nor["age"].str.replace("Y","365")  # For Years
Nor["age"] = Nor["age"].str.replace("M","030")  # For Months
Nor["age"] = Nor["age"].str.replace("D","001")  # For Days
Nor["age"] = Nor["age"].astype(float)
Nor["age"] = (Nor["age"]%1000 * Nor["age"]//1000)//365  # Convert age to years

Nor.replace("No Finding", "Nothing", inplace=True) 

print(Nor['labels'])
#labels.to_csv("/Users/hongxueying/Downloads/5703/dataset/NIH/sample/NIHlabel.csv", index_label="index_label")

#------------------------------------------------------------------------------
#reshape the image

"""

#normal_images = []



#print(Nor['Image Index'][0:1])
        
#images = glob(os.path.join(Sample_images, Nor['Image Index']))

#print(len(image))

#Nor.to_csv("/Users/hongxueying/Downloads/5703/dataset/NIH/sample/Normal_label.csv", index_label="index_label")


"""