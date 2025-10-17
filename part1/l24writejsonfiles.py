import json 

# => Write a simple JSON file 

datas = {
    "title":"Python FastAPI Batch 1",
    "price":25.99,
    "packages":["FastAPI","Jinja2","Websocket","OpenAi"]
}

with open('files/file11.json','w') as file:
    # json.dump(datas,file)
    # json.dump(datas,file,indent=3) # indent is option for text indentation
    # json.dump(datas,file,indent=3,sort_keys=False)    # sort_key is option for a to z
    json.dump(datas,file,sort_keys=True)
    print("Successfully Created")

# => Error Handling 

try:
    invalidatas = {"numbers":{10,20,40}} # Set is not JSON-serializable
    with open('files/fileerror.json','w') as file:
        json.dump(invalidatas,file)
except TypeError as e:
    print("Error : Type Error ",str(e))