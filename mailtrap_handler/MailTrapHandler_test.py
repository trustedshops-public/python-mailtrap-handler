import unittest

from MailTrapHandler import MailTrapHandler
from os import environ


class MailTrapHandlerIntegrationTest(unittest.TestCase):
    """
    Requires the env vars:
    - token: MailTrap API token
    - inbox: Name of the inbox
    - email: Email to use for filtering
    """

    def test_get_mail(self):
        mth = MailTrapHandler(environ["token"])
        result = mth.get_mail(environ["inbox"], environ['email'], waiting_time=10)
        print(result)
