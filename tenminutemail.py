import tls_client

class MinuteMail:
    def __init__(self):
        self.email = None
        self.session = tls_client.Session(
            random_tls_extension_order=True, client_identifier="chrome_106"
        )
        self.session.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "dnt": "1",
            "pragma": "no-cache",
            "referer": "https://10minutemail.com/",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

    def create_address(self):
        response = self.session.get(url="https://10minutemail.com/session/address")

        if response.status_code == 200:
            self.email = response.json().get("address", None)
        else:
            self.email = None

    def get_message(self):
        response = self.session.get(
            url="https://10minutemail.com/messages/messagesAfter/0"
        )

        if response.status_code == 200:
            return response.json()
        else:
            return None


if __name__ == "__main__":
    minute_mail = MinuteMail()
    minute_mail.create_address()
    minute_mail.get_message()
