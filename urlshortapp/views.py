from django.http import JsonResponse
from django.core.serializers import serialize,deserialize
from django.shortcuts import redirect
from urlshortapp.models import URLModel
import base64
import json
import random
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def generate_short_url(request):
    if request.method == "POST": 
        original_url = json.loads(request.body).get('url')
        
        if original_url:
        
            byte_string = original_url.encode('utf-8')
            base64_string = base64.b64encode(byte_string).decode('utf-8')
            
            redirect_url = "/"+base64_string
            existingurl = URLModel.objects.filter(redirect_url__contains = redirect_url).all()

            if existingurl:
        
                ranum = random.randint(1,99999)
                padding = "{0:05d}".format(ranum)
                redirect_url = redirect_url+padding

            url_obj = URLModel(original_url=redirect_url,redirect_url=original_url)
            
            url_obj.save()
            serialized_data = serialize('json',[url_obj])
            print("url_obj",json.loads(serialized_data))
            # print(type(serialized_data))

            return JsonResponse(json.loads(serialized_data)[0],safe=False)


def catch_all(request):
    original_url = request.path
    print("original_url",original_url.rstrip("/"))
    redirect_url = URLModel.objects.filter(original_url=original_url.rstrip("/")).first().redirect_url

    print(redirect_url)

    if redirect_url:
        return redirect(redirect_url)
    else:
        return redirect(original_url)  # Redirect to a default path if not found
