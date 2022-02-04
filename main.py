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
            os.makedirs(f'{os.path.join(os.getcwd(), folder_name)}/{folder}')
        os.makedirs('')

#install tailwind
def install_tailwind():
    'Installs tailwind and configures it'
    print('creating package.json')
    os.system('npm init -y')

    print('Installing TailWind')
    os.system('npm install -D tailwindcss@latest postcss@latest autoprefixer@latest')

    print('configuring tailwind')
    os.system('npx tailwindcss init')
    
    print('creating files and content')
    os.makedirs(f'{os.path.join(os.getcwd(),folder_name)}/src/css')
    os.makedirs(f'{os.path.join(os.getcwd(),folder_name)}/src/css/tailwindcss')

    os.system(f'echo "@tailwind base;\n@tailwind components;\n@tailwind utilities;" > {os.path.join(os.getcwd(),folder_name)}/src/css/tailwindcss')

    







    



