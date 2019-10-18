import uuid

from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import check_password, make_password
from django.core.cache import cache

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO

from AXF import settings
from UserApp.models import AxfUser
from UserApp.view_constaint import send_email


def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        password = make_password(password)
        print(password)

        user = AxfUser()

        user.u_name = name
        user.u_password = password
        user.u_email = email
        user.u_icon = icon

        token = uuid.uuid4()

        user.u_token = token

        user.save()

        cache.set(token, user.id, timeout=45)

        send_email(name, email, token)

        return redirect(reverse('axfuser:login'))


def checkName(request):
    print(111)
    name = request.GET.get('name')
    users = AxfUser.objects.filter(u_name=name)

    data = {
        'msg': '*用户名可以使用',
        'status': 200
    }

    if users.count() > 0:
        data['msg'] = '*用户名已存在',
        data['status'] = 201

    return JsonResponse(data=data)


def testmail(request):
    subject = '红浪漫洗浴'

    message = '<h1>充值1000送免费洗澡一次111</h1>'

    context = {
        'name': '强',
        'url': 'http://www.1000phone.com'
    }

    html_message = loader.get_template('active.html').render(context=context)

    from_email = 'ythhh1@163.com'

    recipient_list = ['ythhh1@163.com']

    send_mail(subject=subject, html_message=html_message, message=message, from_email=from_email,
              recipient_list=recipient_list)

    return HttpResponse('send success')


def activeAccount(request):
    # 通过点击获得请求参数
    token = request.GET.get('token')

    # cache.set(token,user.id,timeout=45)

    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.u_active = True
        user.save()

        cache.delete(token)

        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新发送请求')


import re

def login(request):
    if request.method == 'GET':
        return render(request, 'axf/user/login.html')
    if request.method == 'POST':
        # 用户输入的验证码
        imgcode = request.POST.get('imgcode')
        # 所有的验证码生成策略都会把验证码的值绑定到session上
        verify_code = request.session.get('verify_code')

        b = re.match(imgcode,verify_code,re.IGNORECASE)

        if b:
            name = request.POST.get('name')
            users = AxfUser.objects.filter(u_name=name)
            if users.count() > 0:
                user = users.first()
                password = request.POST.get('password')

                print(password)
                if check_password(password,user.u_password):
                    if user.u_active == True:
                        request.session['user_id'] = user.id
                        return redirect(reverse('axfmine:mine'))
                    else:
                        msg = '用户未激活'
                        context = {
                            'msg': msg
                        }
                        return render(request, 'axf/user/login.html', context=context)
                else:
                    msg = '密码错误'
                    context = {
                        'msg': msg
                    }
                    return render(request, 'axf/user/login.html', context=context)
            else:
                msg = '用户不存在'
                context = {
                    'msg':msg
                }
                return render(request,'axf/user/login.html',context=context)




        else:
            msg = '验证码错误'
            return render(request,'axf/user/login.html',context=locals())


def get_code(request):

    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (100, 50)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 50)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(20*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random

def get_color():
    return random.randrange(256)

def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def logout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))