from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.management import BaseCommand
import requests


class Command(BaseCommand):
    help = "Comparing live and reference data hourly and emailing if live power_dc is less that 80 % of reference power_dc"

    def handle(self, *args, **options):
        inspection_url = "http://127.0.0.1:8000/api/v1/tracking/solar_system/del_000001/power_inspection"
        params = {
            "date": "02-02-2017"
        }
        response = requests.get(url=inspection_url, params=params)
        import pdb;pdb.set_trace()
        if response.status_code == 200 and response.json().__len__() > 0:
            html_content = "<table broder=\"1\"><tr><th>S.No</th><th>hour</th><th>reference_hour</th><th>reference_power_dc</th><th>live_power_dc</th></tr>"

            for counter,element in enumerate(response.json()):
                html_content += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>".format(counter, element['hour'], element['reference_hour'], element['reference_power_dc'], element['live_power_dc'])

            html_content += "</table>"

            subject, from_email, to = 'Testing Email', 'eynimumbaiindia@gmail.com', 'chitrankdixit@gmail.com'
            text_content = 'Hey Please, find the email.'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()




