from datetime import datetime 

# => Get current date and time 
getdatetime = datetime.now()

print("Current date and time = ",getdatetime) #  2025-10-15 21:36:04.081267
print("Year = ",getdatetime.year) # 2025
print("Month = ",getdatetime.month) # 10
print("Day = ",getdatetime.day) # 15
print("Hour = ",getdatetime.hour) # 21
print("Minute = ",getdatetime.minute) # 37
print("Second = ",getdatetime.second) # 49

# => Create a specific datetime 
setdatetime = datetime(2006,9,17,13,30,45)
print("My Birthday = ",setdatetime) # 2006-09-17 13:30:45

# strftime , String Formating Date time 
getnow = datetime.now()
formatdatetime = getnow.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date Time = ",formatdatetime) #  2025-10-15 21:50:50

# strptime() , Convert a string to datetime 
strdate = "2025-10-15 21:50:50"
convertdate = datetime.strptime(strdate,"%Y-%m-%d %H:%M:%S")
print("Converted datetime = ",convertdate) #  2025-10-15 21:50:50

