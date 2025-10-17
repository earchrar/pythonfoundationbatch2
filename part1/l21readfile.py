# => Open a File 
# mode 
# 'r' = Read (default)
# 'w' = Write 
# 'a' = Append 

#syntax 
# open('filename.txt',mode)

# => Read File 

# read()        = Read the entire file 
# readline()    = Read on line at a time 
# readlines()   = Read all lines into a list 

# => Method 1 , read() ( with statement ) , Read all content at once , Not momey-efficient for large files
print("\n Method 1 , read()")
with open('files/file1.txt','r') as file:
        # print(file) # <_io.TextIOWrapper name='files/file1.txt' mode='r' encoding='cp1252'>
        getcontent = file.read()
        print(getcontent)

# => File Encoding 

with open('files/file1.txt','r',encoding='UTF-8') as file:
    getcontent = file.read()
    print(file) # <_io.TextIOWrapper name='files/file1.txt' mode='r' encoding='UTF-8'>
    print(getcontent) 

# => Read Specific Number of characters 
print("\n Read Specific Number of characters")

with open('files/file1.txt','r',encoding='UTF-8') as file:
    getcontent = file.read(10)
    print(getcontent)

# => Method 2 , using strip() , Read line by line , ( One line at a time , Efficient for large file )
print("\n Method 2 , using strip()")

with open('files/file1.txt','r') as file:
    for line in file:
        # print(line)
        print(line.strip()) # .strip() removes extra newline characters

# => Method 3 , readline() , Read line by line , ( One line at a time , Efficient for large file )
print("\n Method 3 , readline()")

with open('files/file1.txt','r') as file:
     lines = file.readline()
        # print(lines) 
     while lines:
          print(lines.strip())
          lines = file.readline()

# => Method 4 , readlines() , Read all by line , ( All line at a once , can use a lot of memory for large files )
print("\n Method 4 , readlines()")

with open('files/file1.txt','r') as file:
     lines = file.readlines()
        # print(lines) # ['Hello World! \n', 'This is Python Batch 1 zoom class.\n', 'How to read file in python programming language.']
     for line in lines:
        # print(line)
          print(line.strip()) # .strip() removes extra newline characters

# Handling Exceptions

# => exceptiontype 
    # (i). FileNotFoundError 
    # (ii). PermissionError 
    # (iii). IOError

print("\n Handling Exceptions")

try:
     with open('files/file1.txt','r') as file:
        getcontent = file.read()
        print(getcontent)
except FileNotFoundError:
     print("Your file does not exists.")
except PermissionError:
     print("You do not have the necessary permission")
except IOError as err:
     print(f"An IO error : {err}")
finally:
     print("Program Completed")

