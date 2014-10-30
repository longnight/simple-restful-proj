#coding=utf-8
import datetime
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime

def send_to_client(data):
    msg = '''Dear %s,\n\n  We have received your application. \
    Please do NOT reply this email.\n\nThanks.\nTech Team. '''\
     % data['last_name']
    from_mail = settings.EMAIL_HOST_USER
    send_mail('Thanks for your application', msg, from_mail,
        [data['email']], fail_silently=False)

def send_to_admin(data):
    subject = 'Application Received from %s' % data['email']
    msg = '''Received an application from %s %s at %s''' \
    % (data['last_name'], data['first_name'],\
     datetime.now().strftime("%Y,%B,%d. %H:%M:%S"))
    from_mail = settings.EMAIL_HOST_USER
    dedicated_account = settings.DEDICATED_EMAIL_ACCOUNT
    send_mail(subject, msg, from_mail,[dedicated_account], fail_silently=False)