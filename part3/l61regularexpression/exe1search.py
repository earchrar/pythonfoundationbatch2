import re 

pattern = re.compile("flower")
print(type(pattern)) # <class 're.Pattern'>

print(pattern.search("orange")) # None

match = pattern.search("A white flower in the field flower")
print(type(match)) # <class 're.Match'>

if match: 
    print(match.group()) # flower
    print(match.start()) # 8 (index)
    print(match.end()) # 14 (index)
    print(match.span()) # (8, 14) (start,end)

# --------------------------------------------------------------------

# exe 2 

text = "123abc456"

# Method 1 
pattern = re.compile("abc")

# Method 2 
pattern = r"abc"

match = re.search(pattern,text)
print("Match Found!" if match else "Not Match.")

# --------------------------------------------------------------------