from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    message = MIMEMultipart()
    text_content = MIMEText('附件中有好康的东西.', 'plain', 'utf-8')
    message['Subject'] = Header('让你康个够', 'utf-8')
    message.attach(text_content)

    with open(r'E:\Python1-100\b.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=b.txt'
        message.attach(txt)
    with open(r'E:\images\wulo.jpg', 'rb') as f:
        image = MIMEText(f.read(), 'base64', 'utf-8')
        image['Type'] = 'jpg'
        image['Content-Disposition'] = 'attachment; filename=wulo.jpg'
        message.attach(image)
    smtper = SMTP('smtp.163.com')
    sender = 'binngo163@163.com'
    receiver = '1030205454@qq.com'
    message['From'] = sender
    message['To'] = receiver
    smtper.login(sender, 'TYEYEDNVJQPQLVWA')
    smtper.sendmail(sender, receiver, message.as_string())
    smtper.quit()
    print('发送成功！')

if __name__ == '__main__':
    main()