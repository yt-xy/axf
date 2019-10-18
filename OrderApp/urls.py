from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    # 下单界面
    url('^make_order/',views.make_order,name='make_order'),
    # 支付界面
    url('^order_detail',views.order_detail,name='order_detail'),
    # 支付
    url('^testpay',views.testpay,name='testpay'),
]