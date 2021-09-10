#! /usr/bin/env python

# Downloading the pdf
import urllib.request

URL = "http://kafemud.bilkent.edu.tr/kumanya_menusu.pdf"


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", "wb")
    file.write(response.read())
    file.close()


download_file(URL, "Menu")

# Sending the email
import smtplib
import os
from email.message import EmailMessage


contacts = ["g_ahmeddd@yahoo.com"]

EMAIL = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")

msg = EmailMessage()
msg["Subject"] = "This week's Table D'Hote menu"
msg["From"] = EMAIL
msg["To"] = contacts
msg.set_content("Afiyet olsun")

files = ["Menu.pdf"]

for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="Application", subtype="octet-stream", filename=file_name
    )


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, PASSWORD)

    smtp.send_message(msg)
    print("Message sent")
