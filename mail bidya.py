import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

   
server.login('bidyashreenayak@gmail.com', "eedjtebnsteghodt")

subject = "CHALLENGES COMPLETION"
  
body = " NAME: Bidyashree Nayak \n Email: bidyashree.2125it@kiet.edu \n Ph.No:8472827878 \nB.Tech IT \n 2nd year \n2100290130058 \n Photo: https://drive.google.com/file/d/1I-ULkZl01nLxC1aChPvUHcMRta-OPK-G/view?usp=drivesdk \n Gitrepo: https://github.com/bidyashree0211/Cabin4j"

msg = f"subject: {subject} \n\n\n {body}"

server.sendmail(
        'bidyashreenayak@gmail.com',
        'sales@cabin4j.com',
    msg
    )
print('Message is sent succesfully!')


