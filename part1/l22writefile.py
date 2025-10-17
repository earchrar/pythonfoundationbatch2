# => Write a File 

# sudo chomd 777 -R files/

# mode 
# 'r' = Read (default)
# 'w' = Write 
# 'a' = Append 

#syntax 
# open('filename.txt',mode)

# => Write File 

# write()
# writelines()

# => Method 1 , write()
print("\n Method 1 , write()")

file = open('files/file2.txt','w')
file.write("Hello World")
file.close() # Always need to close to save changes

# => Method 2, writlines() 
print("\n Method 2 , writlines()")

lines = ["Hello Sir \n","This is Python Batch 1 zoom class. \n","How to read file in python programming language. \n"]
file = open('files/file3.txt','w')
file.writelines(lines)
file.close()

# Using with statement 
print("\n Using with statement")

with open('files/file4.txt','w') as file:
    file.write("Hello Sir \n")
    file.write("This is Python Batch 1 zoom class. \n")
    file.write("How to read file in python programming language. \n")

# => Append to a file 
print("\n Append to a file")

with open('files/file5.txt','a') as file:
    file.write("\n This is Python Batch 1 zoom class")

print("\n with variable")

name = "Yu Yu"
age = 27

with open('files/file6.txt','w') as file:
    file.write(f"My name is {name}. i am {age} years old. \n")

# Error Handling
print("\n Error Handling")

try:
    with open('files/file7.txt','w') as file:
        file.write("How to read file in python programming language.")
except Exception as err: # IOError , General Case
    print(f"An IO Error = {err}")
finally:
    print("Program Completed")