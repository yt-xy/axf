from django.core.mail import send_mail
from django.template import loader


def send_email(name,email,token):
    subject = '红浪漫洗浴'

    message = '<h1>充值1000送免费洗澡一次111</h1>'

    context = {
        'name': name,
        'url': 'http://127.0.0.1:8000/axfuser/activeAccount/?token='+str(token)
    }

    html_message = loader.get_template('active.html').render(context=context)

    from_email = 'ythhh1@163.com'

    recipient_list = [email]

    send_mail(subject=subject, html_message=html_message, message=message, from_email=from_email,
              recipient_list=recipient_list)