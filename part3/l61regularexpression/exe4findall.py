import re 

# exe 1 (contains abc) 
text = "123abc456"
pattern = r"abc"

match = re.search(pattern,text)
print("Match found!" if match else "Not found!")

# exe 2 (match only at the beginning of a string) 
text = "abc456"
pattern = r"abc"

if re.match(pattern,text):
    print("Pattern found at the beginning!")

# exe 3 (finad all digits) 
text = "Product123 costs $456 and qty is 789"
pattern = r"\d+"

result = re.findall(pattern,text)
print("Found digit : ",result) # ['123', '456', '789']

# exe 4 (split = string numeric) 

text = "apple, banana; orange|mango 12345"
pattern = r"\W+"

result = re.split(pattern,text)
print("Split parts : ",result) # ['apple', 'banana', 'orange', 'mango', '12345']

# exe 4 (split = string char) 

text = "apple, banana; orange|mango 12345"
pattern = r"\w+"

result = re.split(pattern,text)
print("Split parts : ",result) #  ['', ', ', '; ', '|', ' ', '']

# exe 5 ( replace all )

text = "Python is fun and powerful"
pattern = r"\s"

result = re.sub(pattern,"-",text)
print("Replaced : ", result) #  Python-is-fun-and-powerful

# Validate phone number format 

phones = ["098-765-4321","0987654321","555-abc-1234","098-7654-321"]
pattern = r"^\d{3}-\d{3}-\d{4}$"

for phone in phones:
    if re.match(pattern,phone):
        print(f"{phone} is valid.")
    else: 
        print(f"{phone} is invalid.")

# => Validate password format , fullmatch() 

pattern = re.compile(r"[A-Za-z0-9@#$%]{8,}")
password = "12345678"

check = pattern.fullmatch(password)
print("Valid Password Format!" if check else "Invalid Password Format!")

# => Extract email addresses , findall()

text = "Contact us at support@gmail.com or admin@shop.org.Thank you."
pattern = r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+"

emails = re.findall(pattern,text)
print("Emails : ",emails) #  Emails :  ['support@gmail.com', 'admin@shop.org']