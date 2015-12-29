import random
import time
import smtplib
import email

#base email is your gmail without the @gmail.com
myemail = "joeshmoe"

#how many times do you want this to run
attempts = 5

#account to use to send the mail
gmail_login = myemail + "@gmail.com"
gmail_pass = "xxxxxxxxx"

#generate some random characters
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
rand_length = 8
randtext = ""

for _ in range(attempts):
	for i in range(rand_length):
		next_index = random.randrange(len(alphabet))
		randtext = randtext + alphabet[next_index]
 
 
	#concate our random numbers to our email   
	myemail = myemail + "+" + randtext + "@gmail.com"
 
 
	#form the email
	fromaddr = myemail
	toaddr = "HeinekenGiftXChange@asmnet.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Heineken Holiday Gift XChange Game"
 
	body = " "
	msg.attach(MIMEText(body, 'plain'))
 
	#send it
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(gmail_login, gmail_pass)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print("email sent to " + myemail)
	time.sleep(10)