import requests

# => GET request 

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)

print(f"Status Code : {response.status_code}")

datas = response.json() 
# print(f"All Posts : {datas}")
# print(f"Total Posts : {len(datas)}")
print(f"First Posts : {datas[0]}")

# => GET request with a parameter 

postid = 3 
response = requests.get(f"https://jsonplaceholder.typicode.com/posts{postid}")
print(f"Post ID 3 : {response.json()}")

# => POST request 

newpost = {
    "userId": 1,
    "title": "My Test Post",
    "body": "This is a just a test"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",json=newpost) # automatically covert the dictionary
print(f"Create Post : {response.json()}")

# => PUT request 

updatepost = {
    "id":5,
    "userId": 1,
    "title": "My Test Post",
    "body": "This is a just a test"
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/5",json=updatepost) # automatically covert the dictionary
print(f"Update Post : {response.json()}")

# => DELETE request 

response = requests.delete("https://jsonplaceholder.typicode.com/posts/10",json=updatepost) # automatically covert the dictionary
print(f"Delete Status Code : {response.status_code}")