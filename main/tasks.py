from myproject.celery import app
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
@app.task

def send_register_email(user_email):
	print(user_email)
	send_mail(
		'Вы подписались на рассылку',
		'Добро пожаловать на сайт',  
		EMAIL_HOST_USER,
		[user_email],  
		fail_silently = False,

	)
		