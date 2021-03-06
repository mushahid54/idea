from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.management import BaseCommand
import requests
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from django.core.mail import EmailMessage


class Command(BaseCommand):
    help = "Comparing live and reference data hourly and emailing if live power_dc is less that 80 % of reference power_dc"

    def handle(self, *args, **options):
        inspection_url = "http://oorjan.southindia.cloudapp.azure.com/api/v1/tracking/solar_system/del_000001/power_inspection"
        params = {
            "date": "02-02-2017"
        }
        response = requests.get(url=inspection_url, params=params)

        if response.status_code == 200 and response.json().__len__() > 0:
            sender = 'eynimumbaiindia@gmail.com'
            reciever = ['keshav@oorjan.com', "mushahidcs0054@gmail.com"]
            message = MIMEMultipart('alternative')
            message['Subject'] = "Find the detail for 02-02-2017 "
            html_content = "<table broder=\"1\"><tr><th>S.No</th><th>hour</th><th>reference_hour</th><th>reference_power_dc</th><th>live_power_dc</th></tr>"

            for counter,element in enumerate(response.json()):
                html_content += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>".format(counter, element['hour'], element['reference_hour'], element['reference_power_dc'], element['live_power_dc'])

            html_content += "</table>"

            try:
               smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
               smtpObj.starttls()
               smtpObj.login('eynimumbaiindia@gmail.com', 'liomessi10')
               email_body = MIMEText(html_content, 'html')
               message.attach(email_body)
               smtpObj.sendmail(sender, reciever, message.as_string())
            except Exception:
               print ("Error: unable to send email")
            #
            # subject, from_email, to = 'Daily report for 02-02-2017', 'eynimumbaiindia@gmail.com', 'mushahidcs0054@gmail.com'
            # text_content = 'Hey please, find the email.'
            #msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # #msg.add_header('Content-Transfer-Encoding')
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()




