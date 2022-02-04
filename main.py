#importing modules
import sys
import os
import subprocess


#create folder
folder_name = sys.argv[1]
folder_Structure = ['public', 'src']
if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
    print('Creating Directory structure')
    for folder in folder_Structure:
        os.makedirs(f'{os.path.join(os.getcwd, folder_name)}/{folder}')

#install tailwind
print('Installing TailWind')
gi
    



