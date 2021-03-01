from requests import get, patch, delete
import json
import sys
import time
from polling import poll


class MailTrapHandler:

    def __init__(self, token):
        self.__headers = {"Api-Token": token}
        self.__base_url = "https://mailtrap.io/api/v1"

    def get_mail_id(self, inbox, email, title=None):
        url = f"{self.__base_url}/inboxes/{inbox}/messages/"
        res = get(url, headers=self.__headers)
        mails = json.loads(res.text)
        mails_id_list = list()
        for mail in mails:
            if title != None:
                if mail["to_email"] == email and title in mail["subject"]:
                    mails_id_list.append(mail["id"])
            else:
                if mail["to_email"] == email:
                    mails_id_list.append(mail["id"])
        return mails_id_list

    def get_mail(self, inbox, email, title=None, waiting_time=0):
        mails_text = list()
        # detecting the mail id
        mails_ids_list = poll(
            lambda: self.get_mail_id(inbox, email, title),
            timeout=waiting_time,
            step=0.5
        )
        # waiting for mail to come
        for mail_id in mails_ids_list:
            r = get(
                f"{self.__base_url}/inboxes/{inbox}/messages/{mail_id}/body.html", headers=self.__headers)
            mails_text.append(r.text)
        return mails_text

    def clean_inbox(self, inbox):
        patch(f"{self.__base_url}/inboxes/{inbox}/clean",
              headers=self.__headers)

    def delete_mails_by_email(self, inbox, email, title=None):
        # detecting the mail id
        mails_ids_list = self.get_mail_id(inbox, email, title)
        for mail_id in mails_ids_list:
            query = f"{self.__base_url}/inboxes/{inbox}/messages/{mail_id}"
            delete(query,headers=self.__headers)
