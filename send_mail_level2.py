import smtplib

sender = "example1@gmail.com"
sender_password = "12345673"


reciver = "example2@gmail.com"
message = """
    Hello, how are you
"""
smtp = smtplib.SMTP_SSL('smtp.gmail.com', port='465')
smtp.login(user=sender, password=sender_password)

try:
    smtp.sendmail(from_addr=sender, to_addrs=reciver, msg=message)
    print("successfully sent")
except smtp.SMTPException:
    raise "ERROR"
