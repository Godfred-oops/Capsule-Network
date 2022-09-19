# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:52:56 2022

@author: Quophi_ababio
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_folder = os.path.join(os.getcwd(), 'txt_files')

finals_list = []
for root, folder, files in os.walk(data_folder):
    for file in files:
        path = os.path.join(root, file)
        with open(path) as f:
            content = f.readlines()   #extracting the data points from the txt file
            df = content[4:]
            empty = []
            for i in range(len(df)):
                dff = df[i].split()
                empty.append(dff)
                
            empty_2 = []
            for j in range(len(empty)):
                for k in range(len(empty[j])):
                    empty_2.append(empty[j][k])
                    
            empty_float = [float(x) for x in empty_2]        
           
            time_info = content[3].split()
            time_step = float(time_info[3])
            num_points = time_info[1]
            num_points = int(num_points.translate({ord(","): None}))
            time_points = np.linspace(time_step, time_step*(num_points + 1), num_points)
            time_points = [round(a,3) for a in time_points]
            #putting the list into a dataframe
            final_df = pd.DataFrame(zip(time_points, empty_float), columns = ['time_points', 'points'])
            
            #expections for the time_steps (removing 0.005 steps)
            for b in range(len(final_df['time_points'])):
                if time_step == 0.005 and b % 2 == 0:
                    final_df = final_df.drop(b, axis = 0)   
                else:
                    continue
                
            finals_list.append(final_df)
#plotting the earthquake           
for t in range(len(finals_list)):
    fig = plt.figure()
    plt.plot(finals_list[t]['time_points'], finals_list[t]['points'])
    fig.savefig("/Users/Godfred/Desktop/extract_data/images/earthquake_{}.png".format(t))



    
    

    
    