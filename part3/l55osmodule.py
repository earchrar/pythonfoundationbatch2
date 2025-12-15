import os 
import time

# => get current working directory 
print(os.getcwd()) # C:\Users\Acer\Documents\pythonbatch2\part3

# => change directory 
# os.chdir("..")
# print(os.getcwd()) # C:\Users\Acer\Documents\pythonbatch2

# => list files and directories 
print(os.listdir()) # list everything in the current dir

# => create a new directory (single) 
# os.mkdir("newfolder")

# => create a new directory (nested) 
# os.makedirs("folder1/folder2/folder3",exist_ok=True)

# => Rename a file 

# with open("oldname.txt",'w') as file:
#     file.write("Hello Mandalay")

# os.rename("oldname.txt","newname.txt")

# => Delete a file 

# os.remove("newname.txt")

# => Check file or dir exists or not 
# url = "l54sysmodule.py"
url = "abc"

if os.path.exists(url):
    print(f"{url} exists.")
else:
    print(f"{url} does not exists.")

# => Check file or dir 
# url = "l54sysmodule.py"
url = "abc"

print("Is file : ",os.path.isfile(url))
print("Is directory : ",os.path.isdir(url))

# => Check file or dir 
url = "l54sysmodule.py"
# url = "abc"

print("Size : ",os.path.getsize(url),"bytes") # 1352 bytes

# => Get file or dir created,modified,accessed 
url = "l54sysmodule.py"
# url = "abc"

print("Created : ",time.ctime(os.path.getctime(url))) # Created :  Tue Nov 25 20:14:03 2025
print("Modified : ",time.ctime(os.path.getmtime(url))) # Modified :  Tue Nov 25 20:39:28 2025
print("Accessed : ",time.ctime(os.path.getatime(url))) # Accessed :  Tue Nov 25 21:17:08 2025

# => Set and Get Environment Variable 

os.environ["GREETING"] = "Hello Mandalay"
print(os.environ.get("GREETING")) # Hello Mandalay

# => Path join 
filepath = os.path.join("folder","subfolder","app.py")
print(filepath) # folder\subfolder\app.py

# => Absolute Path 
print(os.path.abspath("package.json")) # C:\Users\Acer\Documents\pythonbatch2\part3\package.json

# => Split file name extension 
filename = "cutedog.png"
print(os.path.splitext(filename)); # ('cutedog', '.png')



