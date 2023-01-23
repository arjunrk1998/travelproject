from django.shortcuts import render

# Create your views here.
from . models import arjun,datas


def myfun(request):
    data=arjun.objects.all()
    owners=datas.objects.all()
    return render(request,'index.html',{'res':data,'owner':owners})
