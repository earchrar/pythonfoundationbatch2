from gmailsender import GmailSender
from string import Template
from pathlib import Path 

sender = "rzarni17906@gmail.com"
apppassword = "xxoz hnue udbr yqmn"

receiver = "earch821@gmail.com"
subject = "Test Email Python OOP"

# HTML Template 
htmlbody = Template(Path("index.html").read_text())

gmail = GmailSender(sender,apppassword)
gmail.send(receiver,subject,htmlbody)