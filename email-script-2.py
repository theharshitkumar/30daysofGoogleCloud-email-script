import codecs
import smtplib, ssl
import csv
import json
import time
import concurrent.futures
from IPython.core.display import display, HTML
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

csvFilePath = "progress.csv"
jsonFilePath = "progress.json"
fac_name ="Harshit Kumar" #facilitator name
id = 0

def email(element):
    #for element in data:
    #print(" id: ",id," data: ",element)
    #print (element['Student Name'],element['Student Email'], element['# of Skill Badges Completed in Track 1'],element['# of Skill Badges Completed in Track 2'])
    name = element['Student Name']
    mail = element['Student Email']
    t1 = int(element['# of Skill Badges Completed in Track 1'])
    t2 = int(element['# of Skill Badges Completed in Track 2'])
    if t1==0 and t2==0:
        print(element['Student Name'], "Didn't started yet")
        receiver_email = mail
        message = MIMEMultipart("alternative")
        message["Subject"] = "Subject: Start completing your Qwiklabs quests & skill badges | 30 Days of Google Cloud program | ASIET"
        message['To'] = receiver_email
        html = codecs.open("didnt-even-start.html","r", "utf-8").read().format(name,fac_name)
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    elif t1==6 and t2==6:
        print(element['Student Name'],"Completed Both tracks")
        receiver_email = mail # Enter receiver address
        message = MIMEMultipart("alternative")
        message["Subject"] = "Subject: Congratulations! You have successfully achieved your milestone | 30 Days of Google Cloud program | ASIET"
        message['To'] = receiver_email
        html = codecs.open("completed-both.html","r", "utf-8").read().format(name,fac_name)
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    elif t1==6 and t2!=6:
        print(element['Student Name'],"completed Track 1")
        receiver_email = mail  # Enter receiver address
        message = MIMEMultipart("alternative")
        message["Subject"] = "Subject: Congratulations! You have successfully achieved your milestone | 30 Days of Google Cloud program | ASIET"
        message['To'] = receiver_email
        html = codecs.open("track1-completed.html","r", "utf-8").read().format(name,t2,fac_name)
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    elif t2==6 and t1!=6:
        print(element['Student Name'],"completed Track 2")
        receiver_email = mail  # Enter receiver address
        message = MIMEMultipart("alternative")
        message["Subject"] = "Subject: Congratulations! You have successfully achieved your milestone | 30 Days of Google Cloud program | ASIET"
        message['To'] = receiver_email
        html = codecs.open("track2-completed.html","r", "utf-8").read().format(name,t1,fac_name)
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    else:
        print(element['Student Name'],"started but not completed any track")
        receiver_email = mail  # Enter receiver address
        message = MIMEMultipart("alternative")
        message["Subject"] = "Subject: You are almost there to win your prizes | 30 Days of Google Cloud program | ASIET"
        message['To'] = receiver_email
        html = codecs.open("non-zero-non-complete.html","r", "utf-8").read().format(name,t1,6-t1,t2,6-t2,fac_name)
        part2 = MIMEText(html, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == '__main__':
    t0 = time.time()
    # Read the CSV and add the data to dictionary ...
    with open(csvFilePath) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # Write data to a JSON file ...
    with open(jsonFilePath, "w") as f:
        json.dump(rows, f, indent=4)
    f = open('progress.json',)# returns JSON object as
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = ""  # Enter your address
    password = "" # Enter your password or generate app password if you have 2 step authentication enable
    data = json.load(f)
    threads = 10#increase workers if you need more multi threading on your own risk
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(email, data)
    #print(id," students completed atleast 1 track")
    t1 = time.time()
    print(f"{t1-t0} seconds to send {len(data)} emails.")
