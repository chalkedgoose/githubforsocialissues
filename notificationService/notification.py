import sendgrid
import os
from sendgrid.helpers.mail import *


class Notification(object):

    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(
            apikey=os.environ.get('SENDGRID_API_KEY'))
        self.from_email = "atom@projectpescadero.com"

    def sendEmail(self, to_email, subject, content):
        mail = Mail(self.from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)


if __name__ == "__main__":

    xNotifier = Notification()
    email = "carlos.alba@students.makeschool.com"
    subject = "Sendgrid Test"
    content = "<h1> This is a message sent from the notifiaction service on Project Pescadero </h1>"
    xNotifier.sendEmail(email, subject, content)
