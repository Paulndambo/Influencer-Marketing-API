from django.conf import settings


class SendMessage(object):
    def __init__(self, message_type, to_email=None, phone_number=None, template=None, context_data={}):
        self.message_type = message_type
        self.to_email = to_email
        self.phone_number = phone_number
        self.template = template
        self.context_data = context_data
        self.from_email = settings.SITE_EMAIL
        

    def send_sms(self):
        pass

    def send_email(self):
        pass
