#coding=utf-8
from django.core.validators import validate_email

def is_valid_email(email):
    try:
        validate_email(email)        
    except:
        return False
    return True


def is_valid_data(request):
    pass