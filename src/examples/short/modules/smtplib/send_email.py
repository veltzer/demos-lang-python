"""
An example of an application sending an email. This uses smtplib which is a standard python library.

References:
http://stackoverflow.com/questions/23616803/smtplib-smtp-starttls-fails-with-tlsv1-alert-decode-error
"""

import email.mime.text
import smtplib

import googleapiclient.discovery
import pygooglehelper

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def send_email(
        *,
        subject: str,
        content: str,
        fr: str,
        to: str,
        smtp_user: str,
        smtp_password: str,
        smtp_host: str = "smtp.gmail.com",
        smtp_port: int = 587,
        use_tls: bool = True,
        debug: bool = False,
):
    # build the message
    msg = email.mime.text.MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = fr
    # send the message via our own SMTP server,but dont include the envelope header.
    # server=smtplib.SMTP()
    server = smtplib.SMTP(host=smtp_host, port=smtp_port)
    server.ehlo()
    # server.connect(host=smtp_host, port=smtp_port)
    if debug:
        server.set_debuglevel(1)
    if use_tls:
        server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(fr, to, msg.as_string())
    server.quit()


pygooglehelper.ConfigRequest.scopes = SCOPES
pygooglehelper.ConfigRequest.app_name = "pyemail"
credentials = pygooglehelper.get_credentials()
service = googleapiclient.discovery.build(
    serviceName="gmail",
    version="v1",
    credentials=credentials,
)


send_email(
    subject="test sujbect",
    content="test content",
    to="mark.veltzer@gmail.com",
    fr="mark.veltzer@gmail.com",
    smtp_user="mark.veltzer@gmail.com",
    smtp_password="XXXXX",
)
