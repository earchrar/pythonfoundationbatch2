from gmailsender import GmailSender

sender = "rzarni17906@gmail.com"
apppassword = "xxoz hnue udbr yqmn"

receiver = "earch821@gmail.com"
subject = "Test Email Python OOP"
body = "This is a test email sent from Python class using Gmail SMTP."

gmail = GmailSender(sender,apppassword)
gmail.send(receiver,subject,body)