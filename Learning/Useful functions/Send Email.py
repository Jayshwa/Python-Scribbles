import smtplib

SENDER = ""
PASSWORD = ""


def send_email(reciever_email, subject, body):
    """
    Login to email account and send an email.
    """
    message = f"Subject: {subject}/n/n{body}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, reciever_email, message)
