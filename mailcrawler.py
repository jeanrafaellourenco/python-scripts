#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip3 install requests, urllib3

import re
import sys
import urllib3
import requests
import urllib.parse

def extract_emails(url, user_agent):
    try:
        url = urllib.parse.unquote(url)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Desativa erros de certificado SSL

        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  # Verifica se a solicitação teve êxito

        email_pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]*\\.[a-zA-Z.]+[a-zA-Z])"
        emails = set()

        for email in re.findall(email_pattern, response.text):
            email = email.lower()
            emails.add(email)

        return emails

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"URL não informada!\nUse: {sys.argv[0]} https://example.com")
        sys.exit(1)

    url = sys.argv[1]
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"

    emails = extract_emails(url, user_agent)
    if emails:
        for email in emails:
            print(email)
