from django.shortcuts import render

# Create your views here.
from HomeApp.models import AxfWheel, AxfNav, AxfMustBuy, AxfMainshow


def home(request):
    wheels = AxfWheel.objects.all()
    navs = AxfNav.objects.all()
    mustbuys = AxfMustBuy.objects.all()
    mainshows = AxfMainshow.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())

