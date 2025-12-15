import os 
import sys 
from PIL import Image 

# grab first and second argument 
imagefolder = sys.argv[1]
print(imagefolder)
outputfolder = sys.argv[2]
print(outputfolder)

# change dir 
os.chdir("..")

# check is exists or not , if not create it 
if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)
print(outputfolder)

for filename in os.listdir(imagefolder):
    img = Image.open(f'{imagefolder}/{filename}')
    getimgname = os.path.splitext(filename)[0]
    img.save(f'{outputfolder}/{getimgname}.png','png')
    print("Convert Successfully")

# python main.py images output