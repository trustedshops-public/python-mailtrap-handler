# mailtrap-handler
Implimentation for mailtrap basic functionalities using python
### Usage

```python
mailtrap = MailTrapHandler(TOKEN)
```
### Functions
Get mail id:
```python
#default value for title is None
list_of_ids = MailTrapHandler.get_mail_id(inbox, email, title="SOME TEXT")
#returns a list of found mails ids
```
Get mail html content:
```python
#default value for title is None
#default value for waiting_time is 0
MailTrapHandler.get_mail(inbox, email, title, waiting_time=30)
#returns mail html content
```
Clean the inbox:
```python
MailTrapHandler.clean_inbox(inbox)
```
Delet target mail:
```python
MailTrapHandler.delete_mail(inbox, email, title="Some Title here")
#default value for title is None
```
## Example Code
```python
from mailtrap_handler import MailTrapHandler

#requirements
token = "123wellthiswouldbeyourtokenhere098"
inbox = 12349876 #this is your mailtrap inbox id
email = "target_email+probably_with_some_alias@inbox.mailtrap.io"
title = "Oy! Congrats on getting Your new T-shirt"

#creating mailtraphandler object
mailtrap = MailTrapHandler(token)
#getting the html content
mail_id = mailtrap.get_mail(inbox, email, title=title, 10)
#this will log the html conent:
print(mail_id[0])
#and now we delete this mail
mailtrap.delete_mail(inbox, email, title=title)
#you know what let's just delete every mail in the inbox
mailtrap.clean_inbox(inbox)
#I got no more mails!
```