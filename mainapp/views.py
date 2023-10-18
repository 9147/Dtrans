from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'mainapp/home.html')

def text(request):
    return render(request, 'mainapp/text.html')

def getdata(request,src_lang_code,tgt_lang_code,input):
    print(src_lang_code,tgt_lang_code,input)
    result="this is the result"
    return JsonResponse({"data":result})
