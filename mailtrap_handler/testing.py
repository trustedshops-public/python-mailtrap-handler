from MailTrapHandler import MailTrapHandler
from os import environ

mth = MailTrapHandler(environ["token"])
result = mth.get_mail(environ["inbox"], "cm_-c2c95e+20210301124d206@inbox.mailtrap.io", waiting_time=10)
print(result)