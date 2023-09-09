import copy
import datetime
import io
import json
from datetime import date
from urllib.parse import urlencode

import requests
from django.conf import settings
from django.core.files import File
from django.core.mail import EmailMultiAlternatives
from django.db.models import F
from django.template.loader import get_template
from django.utils.html import strip_tags


class SendMessage(object):
    def __init__(self, context_data, template=None,recipient_list=None,  content='', other_recipients=list(), asynchronous=True):
        self.content = content
        self.other_recipients = other_recipients
        self.context_data = context_data
        self.asynchronous = asynchronous
        self.template = template
        self.recipient_list = recipient_list

        
    def send_email(self):
        try:
            html_message = get_template('messages/{0}.html'.format(self.template)).render(self.context_data)
            message = strip_tags(html_message)
            
            subject = '{0}- {1}'.format("Influencer Marketing", self.context_data['subject'])

            email = EmailMultiAlternatives(
                subject=subject,
                body=message,
                from_email=settings.SITE_EMAIL,
                to=self.recipient_list,
            )
            email.attach_alternative(html_message, "text/html")

            if 'attached_files' in self.context_data:
                for attached_file in self.context_data['attached_files']:
                    email.attach(
                        attached_file['name'],
                        attached_file['main_file'],
                        attached_file['media_type'],
                    )

            email.send()
        except Exception as e:
            print(f'_send_email >> error in sending email > {e}')
            raise e


    def __email_additional_configs(self):
        pass