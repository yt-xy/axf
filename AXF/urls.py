"""AXF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^axfhome/',include('HomeApp.urls',namespace='axfhome')),
    # 闪购
    url(r'^axfmarket/',include('MarketApp.urls',namespace='axfmarket')),
    # 购物车
    url(r'^axfcart/',include('CartApp.urls',namespace='axfcart')),
    # 我的
    url(r'^axfmine/',include('MineApp.urls',namespace='axfmine')),
    # 用户
    url(r'^axfuser/',include('UserApp.urls',namespace='axfuser')),
    # 用户
    url(r'^axforder/',include('OrderApp.urls',namespace='axforder')),
]
