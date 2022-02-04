#importing modules
import sys
import os
import subprocess
import getopt

from click import argument


arguments = sys.argv[1:]
  
try:
    opts, args = getopt.getopt(arguments, "n:l:", 
                                ["project_name ="])
    
except:
    print("Error In Flag argument passed")

for opt, arg in opts:
    if opt in ['-n', '--project_name']:
        folder_name = arg

#create folder
def create_folder():
    'Creates folder structure'
    folder_Structure = ['public', 'src']
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        print('Creating Directory structure')
        for folder in folder_Structure:
            os.makedirs(f'{os.path.join(os.getcwd, folder_name)}/{folder}')

def install_tailwind():
    'Installs tailwind and configures it'
#install tailwind
print('Installing TailWind')
subprocess.

    



