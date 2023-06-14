import requests
import tenminutemail
import re
import time
from bs4 import BeautifulSoup


class SnkrDunk:
    def __init__(self, username: str, password: str = "Dr4inG4ng!!"):
        self._save_accounts = open("./accounts.txt", "a+", encoding="utf-8")
        self.mailer = tenminutemail.MinuteMail()
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.csrf_token = None

        self.session.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "dnt": "1",
            "pragma": "no-cache",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    def configurationmicationmachine(self):
        response = self.session.get("https://snkrdunk.com/en/signup?slide=view")
        soupify = BeautifulSoup(response.text, "html.parser")
        self.csrf_token = soupify.find("input", {"name": "csrf_token"})["value"]
        print("get cookies - *snkrdunk* :", response.status_code)

    def create_account(self):
        self.mailer.create_address()
        response = self.session.post(
            "https://snkrdunk.com/en/signup?slide=view",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "username": self.username,
                "email": self.mailer.email,
                "password": self.password,
                "agreement": "on",
                "csrf_token": self.csrf_token,
                "tzDatabaseName": "America/Los_Angeles",
            },
        )
        print("create account - *snkrdunk* :", response.status_code)

    def verify_account(self):
        while not self.mailer.get_message():
            sleep(1.5)

        email_message = self.mailer.get_message()[0].get("bodyPlainText", "")
        activation_link = re.search(
            pattern=r"https\:\/\/snkrdunk\.com\/en\/account\/activation\?([\w+|\d+|\.|\/|\?|=|&])+",
            string=email_message,
            flags=re.DOTALL | re.MULTILINE,
        )
        response = self.session.get(activation_link.group(0))
        print("verify account - *snkrdunk* :", response.status_code)

        if "Your email verification has been confirmed" in response.text:
            self._save_accounts.write(
                f"{self.mailer.email}:{self.username}:{self.password}:{time.time()}"
            )
        

if __name__ == "__main__":
    snkr = SnkrDunk("l3g3nd4ryM3mb3r", password="meowPurr11!")
    snkr.configurationmicationmachine()
    snkr.create_account()
    snkr.verify_account()
    snkr._save_accounts.close()
