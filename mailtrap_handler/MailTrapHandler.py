import logging

from requests import get, patch, delete
import json
from polling import poll

API_BASE_URL_V2 = "https://mailtrap.io/api"
API_BASE_URL_V1 = "https://mailtrap.io/api/v1"


class MailTrapHandler:
    """
    Utility for MailTrap API communication
    """

    def __init__(self, token, account_id):
        self.__headers = {
            "Api-Token": token
        }
        self.__base_url = f"{API_BASE_URL_V2}/accounts/{account_id}"

    def get_mail_id(self, inbox, email, title=None):
        """
        Get all mail ids for a given inbox

        :param inbox: Name of the inbox
        :param email: E-Mail address of the target mailbox
        :param title: Title to filter for, if none is specified all mails will be selected
        :return: List of mail ids
        """
        res = get(f"{self.__base_url}/inboxes/{inbox}/messages/",
                  headers=self.__headers)
        mails = json.loads(res.text)
        mails_id_list = list()

        for mail in mails:
            if title is None:
                if mail["to_email"] == email:
                    mails_id_list.append(mail["id"])
            else:
                if mail["to_email"] == email and title in mail["subject"]:
                    mails_id_list.append(mail["id"])

        return mails_id_list

    def get_mail(self, inbox, email, title=None, waiting_time=1):
        """
        Wait for mails to appear in inbox

        :param inbox: Name of the inbox
        :param email: Email address of the mailbox
        :param title: Title of the mail to filter for
        :param waiting_time: How long to wait in seconds
        :return: HTML bodies of the mails
        """
        mails_text = list()
        mails_ids_list = list()

        # detecting the mail id
        try:
            buffer_list = poll(
                lambda: self.get_mail_id(inbox, email, title),
                timeout=waiting_time,
                step=0.5
            )
            if buffer_list is not None:
                mails_ids_list = buffer_list
        except:
            logging.info("didn't recieve any results")

        # waiting for mail to come
        for mail_id in mails_ids_list:
            r = get(f"{self.__base_url}/inboxes/{inbox}/messages/{mail_id}/body.html",
                    headers=self.__headers)
            mails_text.append(r.text)

        return mails_text

    def clean_inbox(self, inbox):
        """
        Cleanup the given inbox

        :param inbox: Name of the inbox
        :return: None
        """
        patch(f"{self.__base_url}/inboxes/{inbox}/clean",
              headers=self.__headers)

    def delete_mails_by_email(self, inbox, email, title=None):
        """
        Delete all mails from an inbox for a given mail address

        :param inbox: Name of the inbox
        :param email: Email address of the mailbox
        :param title: Filter for mail title, if not specified will affect all mails
        :return: None
        """
        # detecting the mail id
        mails_ids_list = self.get_mail_id(inbox, email, title)
        for mail_id in mails_ids_list:
            delete(f"{self.__base_url}/inboxes/{inbox}/messages/{mail_id}",
                   headers=self.__headers)
