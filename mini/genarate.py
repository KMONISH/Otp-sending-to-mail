import smtplib
import mail
import smail
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(mail.EMAIL_ADDRESS1, mail.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(mail.EMAIL_ADDRESS1, smail.EMAIL_ADDRESS2, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")
        
