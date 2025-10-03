from flask_mail import Message
from .. import mail

class MailService:
    @staticmethod
    def send_confirmation(user_email, first_name, last_name, date):
        body = f"Hi {first_name}, thank you for your submission.\n\n" \
               f"Details:\nName: {first_name} {last_name}\nStart Date: {date}"

        msg = Message(subject="Form Confirmation",
                      sender="noreply@example.com",
                      recipients=[user_email],
                      body=body)
        mail.send(msg)
