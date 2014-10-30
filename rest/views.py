#coding=utf-8
from django.shortcuts import render
from models import Rest
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from validate import is_valid_email, is_valid_data
from send_msg import send_to_client, send_to_admin

ct = "application/json"

@csrf_exempt
def rest_index(request):

    mails = {
        "items":[],
        "href":"http://localhost:8000/rest",
        "template":{
            "email":"",
            "first_name":"",
            "last_name":"",
            "contact_number":"",
            "title":"",
            "content":"",
            "link":"title"
        }
    }
    if request.method == "OPTIONS":
        return HttpResponse(json.dumps({"allow":"GET, POST, OPTIONS"}), status=200)

    if request.method == "POST":
        data = json.loads(request.body)
        print type(data)
        data.pop('id', None)
        
        for k, v in data.items():
            if len(data[k]) < 1:
                return HttpResponse(json.dumps({"error":"wrong field data, check again pls."}), content_type=ct, status=404)
        if not is_valid_email(data['email']):
            return HttpResponse(json.dumps({"error":"wrong email."}), content_type=ct, status=404)
        r = Rest(**data)
        try:
            r.save()
        except:
            return HttpResponse(json.dumps({"error":"wrong key"}), content_type=ct, status=404)

        send_to_client(data)
        send_to_admin(data)
        return HttpResponse(json.dumps(data, indent=4), content_type=ct, status=201)

    m = Rest.objects.all().values()
    for i in m:
        i['href'] = "http://localhost:8000/rest/" + str(i["id"])
        mails['items'].append(i)
    
    return HttpResponse(json.dumps(mails, indent=4), content_type=ct, status=200)

@csrf_exempt
def rest_id(request, id):
    try:
        item = Rest.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"error":"id not found"}), content_type=ct, status=404)

    if request.method == "OPTIONS":
        return HttpResponse(json.dumps({"allow":"GET, PUT, OPTIONS"}), status=200)  

    if request.method == "PUT":
        rest_fields = Rest._meta.get_all_field_names()
        data = json.loads(request.body)
        print type(data)
        print data
        data.pop('id', None)
        for k, v in data.items():
            if k in rest_fields:
                if len(data[k]) < 1:
                    return HttpResponse(json.dumps({"error":"not allow null value."}), content_type=ct, status=404)
                if k == 'email':
                    if not is_valid_email(data[k]):
                        return HttpResponse(json.dumps({"error":"wrong email."}), content_type=ct, status=404)
                setattr(item, k, data[k])
        try:
            item.save()
            item = model_to_dict(item)
            return HttpResponse(json.dumps(item, indent=4), content_type=ct, status=200)
        except:
            return HttpResponse(json.dumps({"error":"wrong in saving."}), content_type=ct, status=404)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse("deleted.", status=200)

    mail = model_to_dict(item)
    mail_dict = {}
    mail_dict['href'] = "http://localhost:8000/rest/" + str(mail["id"])
    mail_dict['mail'] = mail

    return HttpResponse(json.dumps(mail_dict, indent=4), content_type=ct, status=200)