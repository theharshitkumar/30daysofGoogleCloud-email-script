
import smtplib, ssl
import csv
import json
import time
import concurrent.futures
csvFilePath = "progress.csv"
jsonFilePath = "progress.json"
id = 0


def email(element):
#for element in data:
    #print(" id: ",id," data: ",element)
    print (element['Student Name'],element['Student Email'], element['# of Skill Badges Completed in Track 1'],element['# of Skill Badges Completed in Track 2'])
    name = element['Student Name']
    mail = element['Student Email']
    t1 = int(element['# of Skill Badges Completed in Track 1'])
    t2 = int(element['# of Skill Badges Completed in Track 2'])
    if t1==6 or t2 ==6:
        id+=1

    if t1==0 and t2 ==0:
        receiver_email = mail  # Enter receiver address
        message = """Subject: Start completing your Qwiklabs quests & skill badges | 30 Days of Google Cloud program | ASIET

Dear {},

Thank you so much for enrolling in the 30 Days of Google Cloud program. We noticed that you have not completed any quests or skill badges in the program so far.

Please note that you have until 5th November to complete the milestones mentioned on the prizes rules section here and earn those exciting prizes. Please start completing them ASAP.

As always, please feel free to reach out to us on our Whatsapp group - *group link* in case of any questions or for future updates.
Visit the program website to know more about which skill badges you need to get - https://events.withgoogle.com/30daysofgooglecloud/
Check out the prize which you can get - https://events.withgoogle.com/30daysofgooglecloud/prize-rules/#content

All the best & happy learning,
Your 30 Days of Google Cloud Facilitator


.""".format(name)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    elif t1==6 and t2 ==6:
        receiver_email = mail  # Enter receiver address
        message = """Subject: Congratulations! You have successfully achieved your milestone | 30 Days of Google Cloud program | ASIET


Dear {},

Congratulations on successfully achieving your milestone in the 30 Days of Google Cloud program. We are so excited for and can’t wait for you to receive your prizes.

Please note that your prizes will be delivered to you after the program ends i.e. after 5th November. Meanwhile we request you to please not stop your learning journey and keep on working to get more badges on Qwiklabs so that you can become an expert in cloud.

As always, please feel free to reach out to us on our Whatsapp group - *group link* in case of any questions or for future updates.

All the best & happy learning,
Your 30 Days of Google Cloud Facilitator

.""".format(name)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
    elif t1==6 and t2 !=6:
        receiver_email = mail  # Enter receiver address
        message = """Subject: Congratulations! You have successfully achieved your milestone | 30 Days of Google Cloud program | ASIET


Dear {},

Congratulations on successfully achieving your milestone in the 30 Days of Google Cloud program. We are so excited for and can’t wait for you to receive your prizes.

Please note that your prizes will be delivered to you after the program ends i.e. after 5th November. Meanwhile we request you to please not stop your learning journey and keep on working to get skill badges in the track 2.
You have completed {} out of 6 skill badges in Track 2.

As always, please feel free to reach out to us on our Whatsapp group - *group link* in case of any questions or for future updates.
Visit the program website to know more about which skill badges you need to get  - https://events.withgoogle.com/30daysofgooglecloud/
Check out the prize which you can get - https://events.withgoogle.com/30daysofgooglecloud/prize-rules/#content

All the best & happy learning,
Your 30 Days of Google Cloud Facilitator

.""".format(name,t2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
    elif t2==6 and t1 !=6:
        receiver_email = mail  # Enter receiver address
        message = """Subject: Congratulations! You have successfully achieved your milestone | 30 Days of Google Cloud program | ASIET


Dear {},

Congratulations on successfully achieving your milestone in the 30 Days of Google Cloud program. We are so excited for and can’t wait for you to receive your prizes.

Please note that your prizes will be delivered to you after the program ends i.e. after 5th November. Meanwhile we request you to please not stop your learning journey and keep on working to get badges in the track 1.
You have completed {} out of 6 skill badges in Track 1.

As always, please feel free to reach out to us on our Whatsapp group - *group link* in case of any questions or for future updates.
Visit the program website to know more about which skill badges you need to get  - https://events.withgoogle.com/30daysofgooglecloud/
Check out the prize which you can get - https://events.withgoogle.com/30daysofgooglecloud/prize-rules/#content

All the best & happy learning,
Your 30 Days of Google Cloud Facilitator

.""".format(name,t1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
    else:
        receiver_email = mail  # Enter receiver address
        message = """Subject: You are almost there to win your prizes | 30 Days of Google Cloud program | ASIET


Dear {},

We noticed that you have completed {} skill badges already in the program's Track 1 and are just {} away from earning your prizes for track 1 also we found out that you have completed {} skill badges already in the program's Track 2 and are just {} away from earning your prizes for track 2.
We are so glad that you have made it so far in the program.

Please complete the remaining quests and the skill badges ASAP so that you can be entitled to your prizes. Note: You have until 5th November to complete the milestones mentioned on the prizes rules section https://events.withgoogle.com/30daysofgooglecloud/prize-rules/#content and earn those exciting prizes.

As always, please feel free to reach out to us on our Whatsapp group - *group link* in case of any questions or for future updates.
Visit the program website to know more about which skill badges you need to get  - https://events.withgoogle.com/30daysofgooglecloud/
Check out the prize which you can get - https://events.withgoogle.com/30daysofgooglecloud/prize-rules/#content


All the best & happy learning,
Your 30 Days of Google Cloud Facilitator

.""".format(name,t1,6-t1,t2,6-t2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode("utf-8"))


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
    sender_email = "enter email here"  # Enter your address
    password = "you know what to do here" # Enter your password or generate app password if you have 2 step authentication enable
    data = json.load(f)
    threads = 10 #increase workers if you need more multi threading on your own risk
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(email, data)
    #print(id," students completed atleast 1 track")
    t1 = time.time()
    print(f"{t1-t0} seconds to send {len(data)} emails.")
