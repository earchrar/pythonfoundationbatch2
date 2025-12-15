import re 

pattern = re.compile("flower")

text = "There are a lot of flowers in the flower field. i love flower."

print(pattern.findall(text)) # ['flower', 'flower', 'flower']
print(pattern.findall("orange")) # []

for match in pattern.findall(text):
    print(match)

for match in pattern.finditer(text):
    print(match)