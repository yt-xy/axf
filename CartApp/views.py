from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart


def cart(request):
    user_id = request.session.get('user_id')
    is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user_id=user_id).exists()
    total_price = get_total_price(user_id)

    if user_id:
        # 查找当前登录的用户的购物车
        carts = AxfCart.objects.filter(c_user_id=user_id)

        context={
            'carts':carts,
            'is_all_select':is_all_select,
            'total_price':total_price,
        }

        return render(request,'axf/main/cart/cart.html',context=context)
    else:
        return redirect(reverse('axfuser:login'))

def addToCat(request):
    user_id = request.session.get('user_id')

    data = {
        'msg':'ok',
        'status':200
    }

    if user_id:
        goodsid = request.GET.get('goodsid')

        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)

        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.c_goods_id = goodsid
            cart.c_user_id = user_id

        cart.save()

        data['c_goods_num'] = cart.c_goods_num

        return JsonResponse(data=data)
    else:
        data['msg'] = '未登录'
        data['status'] = 201

        return JsonResponse(data=data)

@csrf_exempt
def subCart(request):
    data = {
        'msg':'ok',
        'status':200,
    }

    cartid = request.POST.get('cartid')
    cart = AxfCart.objects.get(pk=cartid)

    if cart.c_goods_num > 1:
        cart.c_goods_num = cart.c_goods_num - 1
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
    else:
        cart.delete()
        data['status'] = 204

    return JsonResponse(data=data)


def changeStatus(request):
    data = {
        'msg':'ok',
        'status':200
    }

    cartid = request.GET.get('cartid')
    cart = AxfCart.objects.get(pk=cartid)
    cart.c_is_select = not cart.c_is_select
    cart.save()

    data['c_is_select'] = cart.c_is_select

    is_all_select = not AxfCart.objects.filter(c_is_select=False).exists()
    data['is_all_select'] = is_all_select

    user_id = request.session.get('user_id')
    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)


def allSelect(request):
    cartidlist = request.GET.get('cartidlist')
    cartid_list = cartidlist.split('#')

    carts = AxfCart.objects.filter(id__in=cartid_list)

    data = {
        'msg':'ok',
        'status':200
    }

    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    user_id = request.session.get('user_id')
    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)


def get_total_price(user_id):
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    total_price = 0

    for cart in carts:
        total_price = total_price + cart.c_goods_num * float(cart.c_goods.price)

    return '%.2f' %total_price