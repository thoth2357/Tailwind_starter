#importing modules
import sys
import os
import subprocess
import getopt


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
    '''Creates folder structure'''
    folder_Structure = ['public', 'src']
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        print('Creating Directory structure')
        for folder in folder_Structure:
            os.makedirs(f'{os.path.join(os.getcwd(), folder_name)}/{folder}')

#install tailwind
def install_tailwind():
    'Installs tailwind and configures it'
    print('creating package.json')
    os.chdir(os.path.join(os.getcwd(), folder_name))
    os.system('npm init -y')

    print('Installing TailWind and LiveServer')
    os.system('npm install -D tailwindcss@latest postcss@latest autoprefixer@latest')

    print('configuring tailwind')
    os.system('npx tailwindcss init')
    
    print('creating files and content')
    os.makedirs(f'{os.getcwd()}/src/css')

    os.system(f'echo "@tailwind base;\n@tailwind components;\n@tailwind utilities;" > {os.getcwd()}/src/css/tailwind.css')
    
    os.system(f'sed -i \'/test/c\  "build": "tailwindcss -i {os.getcwd()}/src/css/tailwind.css -o {os.getcwd()}/public/styles.css -w"\' package.json')
    
    os.system(f'sed -i \'/content/c\  content: ["./public/index.html"],\' tailwind.config.js')
    index_path = os.getcwd() + '/public/index.html'

    os.system(f'echo "node_modules/"> .gitignore')

    os.system(f'echo "<html lang=\"en\"> \n \
 <head>  \n \
    <meta charset="utf-8" />  \n \
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />  \n \
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">  \n \
    <title>TailwindCSS 2.0</title>  \n \
    <link rel="stylesheet" href=\"styles.css\" />  \n \
 </head> \n \
<body> \n \
    <div class=\"flex-column justify-center items-center h-screen\"> \n \
    <div class="p-20 text-center"> \n \
      <h1 class="text-9xl">tailwindcss Quick Starter</h1> \n \
      <h3>Created By @Thoth</h3> \n \
      <div class="bg-green-200 hover:bg-green-500 p-10 text-4xl">Is now configured andlive on server !!</div> \n \
      <div class="p-5 text-2xl"> \n \
    </div> \n </div> \n</div>" > {index_path}')

def run_builds():
    'runs the tailwind configuraton'
    os.system('npm run build')
    print('Script completed ..Start Editing the public/index.html')

create_folder()
install_tailwind()
run_builds()



    



