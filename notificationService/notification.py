import sendgrid
import os
from sendgrid.helpers.mail import *
import nexmo


class Notification(object):

    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(
            apikey=os.environ.get('SENDGRID_API_KEY'))
        self.from_email = "atom@projectpescadero.com"
        self.client = nexmo.Client(key='bcefb8f8', secret='G4BbrKWlbWhTF1dI')
        self.from_number = '13364772034'

    def sendEmail(self, to_email, subject, content):
        mail = Mail(self.from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

    def sendSMS(self, to_number, text):

        self.client.send_message(
            {
                'from': self.from_number,
                'to': to_number,
                'text': text
            }
        )


if __name__ == "__main__":

    xNotifier = Notification()
    # sms
    xNotifier.sendSMS('14159008591', 'Nexmo test')

    # email not working

    # email = "carlos.alba@students.makeschool.com"
    # subject = "Sendgrid Test"
    # content = "<h1> This is a message sent from the notifiaction service on Project Pescadero </h1>"
    # xNotifier.sendEmail(email, subject, content)
