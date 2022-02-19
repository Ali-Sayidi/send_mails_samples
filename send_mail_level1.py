import smtplib

# my_email and my_password are exmaple, should put correct info

my_email = "example1@gmail.com"
my_password = "12345677"

# For accessing gmail account enable less secure app
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(my_email, my_password)
server.sendmail(my_email,
                "example2@gmail.com",
                "Hello How are you?? "
                )

server.quit()