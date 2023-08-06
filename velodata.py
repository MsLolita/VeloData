import time
from random import choice

import requests
import pyuseragents

from anticaptchaofficial.turnstileproxyless import turnstileProxyless

from data.captcha import ANTICAPTCHA_API_KEY, SITE_KEY, URL
from utils import str_to_file, logger
from string import ascii_lowercase, digits

from utils import MailUtils


class VeloData(MailUtils):
    referral = None

    def __init__(self, email: str, imap_pass: str, proxy: str = None):
        super().__init__(email, imap_pass)
        self.address = None  # address
        self.proxy = f"http://{proxy}" if proxy else None

        self.password = VeloData.generate_password(7)

        self.headers = {
            'authority': 'velodata.app',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,uk;q=0.8,ru-RU;q=0.7,ru;q=0.6,en-GB;q=0.5',
            'referer': 'https://velodata.app/ref/apxw5v3e',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': pyuseragents.random(),
        }

        self.session = requests.Session()

        self.session.headers.update(self.headers)
        self.session.cookies.update({
            'theme': 'Light',
            'refby': VeloData.referral
        })
        self.session.proxies.update({'https': self.proxy, 'http': self.proxy})

    def sign_up(self):
        for _ in range(2):
            url = 'https://velodata.app/api/a/register'
            token = VeloData.__bypass_turnstile_captcha()

            json_data = {
                'email': self.email,
                'password': self.password,
                'code': token,
            }

            response = self.session.post(url, json=json_data)

            if response.ok:
                return response.ok

            time.sleep(3)

    def verify_email(self):
        otp_code = self.get_otp_code()

        return self.approve_email(otp_code)

    def get_otp_code(self):
        result = self.get_msg(from_="support@velodata.app", limit=1)
        msg = result["msg"]
        return msg.split('line-break: anywhere;">')[-1].split("</h2>")[0]

    def approve_email(self, otp_code: str):
        params = {
            'ref': otp_code,
        }

        response = self.session.get('https://velodata.app/api/a/verify', params=params)

        return response.ok, response.text

    def logs(self):
        file_msg = f"{self.email}|{self.address}|{self.proxy}"
        str_to_file(f"data\\logs\\success.txt", file_msg)
        logger.success(f"Register {self.email}")

    def logs_fail(self, msg: str = ""):
        file_msg = f"{self.email}|{self.address}|{self.proxy}"
        str_to_file(f"data\\logs\\failed.txt", file_msg)
        logger.error(f"Failed {self.email} {msg}")

    @staticmethod
    def __bypass_turnstile_captcha():
        solver = turnstileProxyless()
        # solver.set_verbose(1)
        solver.set_key(ANTICAPTCHA_API_KEY)
        solver.set_website_url(URL)
        solver.set_website_key(SITE_KEY)

        solver.set_action("login")
        token = solver.solve_and_return_solution()

        if not token:
            logger.error(f"{token} Failed to solve captcha! Please put your API key in data/captcha/__init__.py")
            exit()

        return token

    @staticmethod
    def generate_password(k=10):
        return ''.join([choice(ascii_lowercase + digits) for i in range(k)])

