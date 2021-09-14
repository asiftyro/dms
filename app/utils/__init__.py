from flask import current_app
from flask_mail import Message
from app import mail, executor


def send_email(to, subject, message_text='', message_html=''):
    msg = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = message_text
    msg.html = message_html
    mail.send(msg)


def send_async_email(to, subject, message_text='', message_html=''):
    future = executor.submit(send_email, to, subject, message_text, message_html)
