import sys 

# print("Enter your name : ")
# userinput = sys.stdin.readline()
# print(f"You name is : {userinput}")

sys.stderr.write("This is an error message\n")
sys.stdout.write("This is an error message\n")

print(sys.version) # 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)]
print(sys.platform) # win32
print(sys.path) # ['C:\\Users\\Acer\\Documents\\pythonbatch2\\part3', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\python313.zip', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\DLLs', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\Lib', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\Lib\\site-packages']
print(sys.argv) # ['l54sysmodule.py']
print(sys.argv[0]) # python3 l54sysmodule.py hello sir # l54sysmodule.py
print(sys.argv[1]) # python3 l54sysmodule.py hello # hello
print(sys.argv[2]) # python3 l54sysmodule.py hello sir # sir
print(sys.argv[1:]) # python3 l54sysmodule.py hello sir # ['hello', 'sir']

print("Before exit")
sys.exit()
print("After Exist")