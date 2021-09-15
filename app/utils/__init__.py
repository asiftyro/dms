from flask import current_app
from flask_mail import Message
from app import mail, executor
from itsdangerous import URLSafeTimedSerializer

# ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


def get_email_token(email):
    ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return ts.dumps(email, salt=current_app.config["EMAIL_CONFIRM_KEY"])


def check_email_token(token):
    ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    email = ts.loads(token, salt=current_app.config["EMAIL_CONFIRM_KEY"], max_age=86400) # 86400 seconds = 24 hour
    return email


def send_email(sender, to, subject='', message_text='', message_html=''):
    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = message_text
    msg.html = message_html
    mail.send(msg)


def send_async_email(sender, to, subject='', message_text='', message_html=''):
    future = executor.submit(send_email, sender, to, subject, message_text, message_html)
