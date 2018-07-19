import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sriharsha8811@gmail.com","momdaddy8811")
message = "hi hello"
server.sendmail("poushighosh@gmail.com","poushigosh@gmail.com",message)
print("sss")
server.quit()
