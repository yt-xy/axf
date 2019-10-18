from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from CartApp.models import AxfCart
from MarketApp.models import AxfFoodType, AxfGoods


def market(request):
    typeid = request.GET.get('typeid','104749')

    foodtypes = AxfFoodType.objects.all()

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    # 全部分类:0#进口水果:103534#国产水果:103533
    # print(childtypenames)

    childtype_list = childtypenames.split('#')
    # ['全部分类:0', '进口水果:103534', '国产水果:103533']
    # print(childtype_list)

    typename_list = []
    for childtype in childtype_list:
        typename = childtype.split(':')
        typename_list.append(typename)

    # goods = AxfGoods.objects.all()
    # goods_list = AxfGoods.objects.filter(categoryid=typeid)
    # print(goods_list)
    childcid = request.GET.get('childcid','0')

    if childcid == '0':
        goods_list = AxfGoods.objects.filter(categoryid=typeid)
    else:
        goods_list = AxfGoods.objects.filter(categoryid=typeid).filter(childcid=childcid)


    sortid = request.GET.get('sortid','1')
    sort_list = [
        ['综合排序', '1'],
        ['价格升序', '2'],
        ['价格降序', '3'],
        ['销量升序', '4'],
        ['销量降序', '5'],
    ]

    if sortid == '2':
        goods_list = goods_list.order_by('price')
    elif sortid == '3':
        goods_list = goods_list.order_by('-price')
    elif sortid == '4':
        goods_list = goods_list.order_by('productnum')
    elif sortid == '5':
        goods_list = goods_list.order_by('-productnum')

    for good in goods_list:
        goodsid = good.id
        user_id = request.session.get('user_id')
        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)

        if carts.count() > 0:
            cart = carts.first()
            c_goods_num = cart.c_goods_num
        else:
            c_goods_num = 0
        good.c_goods_num = c_goods_num


    # c_goods_num = goods_list.axfcart_set.c_goods_num

    context = {
        'foodtypes':foodtypes,
        # 'goods':goods,
        'goods_list':goods_list,
        'typeid':typeid,
        'typename_list':typename_list,
        'childcid':childcid,
        'sort_list':sort_list,
        'sortid':sortid,
    }

    return render(request,'axf/main/market/market.html',context=context)