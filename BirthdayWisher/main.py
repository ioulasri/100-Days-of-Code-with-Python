import smtplib

my_email = "sender.program01@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password="Imadoox0123")
connection.sendmail(from_addr=my_email, to_addrs="python.recepient01@gmail.com", msg="Hello")
connection.close()
