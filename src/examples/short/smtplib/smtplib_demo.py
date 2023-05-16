"""
An example of an application sending an email. This uses smtplib which is a standard python library.

References:
http://stackoverflow.com/questions/23616803/smtplib-smtp-starttls-fails-with-tlsv1-alert-decode-error
"""

import email.mime.text
import smtplib


def send_email(
        subject="default subject",
        fr="default from",
        to=None,
        content="default content",
        smtp_host="localhost",
        smtp_port=587,
        use_tls=True,
        user=None,
        password=None,
        debug=False,
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
    server.login(user, password)
    server.sendmail(fr, to, msg.as_string())
    server.quit()


send_email(
    smtp_host="smtp.gmail.com",
    user="myname@gmail.com",
    to="myname@gmail.com",
    fr="myname@gmail.com",
    password="XXXXXXXX",
    debug=True,
)
