from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from .models import Candidate

def index(request):
    candidates = Candidate.objects.all() #Candidate에 있는 모든 객체를 불러와 candidates에 저장
    str = '' #리턴해줄 문자열(14번째줄)
    for candidate in candidates:
        str += "<p>No. {}번  name. {}<br>".format(candidate.party_number,
            candidate.name)#<br>은 html코드로 다음줄로 줄내림할때 사용
        str += candidate.introduction+"</p>"#<p>는 html코드로 단락이동할때 
    return HttpResponse(str)