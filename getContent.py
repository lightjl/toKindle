#!usr/bin/env
# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS
import os
import codecs
import smtplib
import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sub_folder = os.path.join(os.getcwd(), "/xs/")
if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)

class saveToFile():
    def __init__(self):
        self.sub_folder = sub_folder
        pass

    def save(self, filename, text):
        self.__filename = sub_folder + filename + ".txt"
        #print(self.__filename)
        f = codecs.open(self.__filename, "a", "utf-8")
        f.write(text)
        f.close()

    def isDownloaded(self, filename):
        filename2 = sub_folder + filename + ".txt"
        #print(filename2)
        return os.path.isfile(sub_folder + filename + ".txt")  # 如果不存在就返回False
        pass
'''
for i in range(2000):
    url = one_url + str(i + 1)
    r = requests.get(url)
    if r.status_code == 200:
        print(url)
        soup = BS(r.text, "lxml")
        title = soup.select('div.tab-content > div.one-articulo > h2')
        # print title
        print("标题: ", title[0].get_text().strip())
        # file_name = title[0].get_text().strip() + ".txt"
        file_name = str(i + 1) + ".txt"

        content = soup.select('div.articulo-contenido')

        filename = sub_folder + "/xs" + file_name
        # print filename
        # print os.path.join(sub_folder, file_name)

        print("start writing content into file", file_name)
        f = codecs.open(filename, "a", "utf-8")
        f.write(content[0].get_text())
        f.close()
        print("finish writing into file \n")

        sender = "youremailid@163.com"
        sender_password = ""
        receiver = 'yamieborn_1@kindle.cn'
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "convert" + str(datetime.datetime.now())
        msg['From'] = sender
        msg['To'] = "Your Kindle" + "<" + receiver + ">"
        att = MIMEText(open(os.path.join(sub_folder, file_name), 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
        msg.attach(att)
        try:
            server = smtplib.SMTP()
            server.connect('smtp.163.com')
            print("start login")
            server.login(sender, sender_password)
            print("start sending email")
            server.sendmail(sender, receiver, msg.as_string())
            server.quit()
'''