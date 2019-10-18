from django.conf.urls import url

from CartApp import views

urlpatterns=[
    url(r'^cart/',views.cart,name='cart'),
    # 添加到购物车
    url('^addToCart/',views.addToCat,name='addToCart'),
    # 减少商品数量
    url('^subCart/',views.subCart,name='subCart'),
    # 改变选中状态
    url('^changeStatus/',views.changeStatus,name='changeStatus'),
    # 全选
    url('^allSelect/',views.allSelect,name='allSelect'),
]