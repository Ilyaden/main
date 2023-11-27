from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .forms import *
from django.core.mail import send_mail
from .tasks import send_register_email
from django.http import HttpResponseRedirect

def register(request):

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			send_register_email.delay(form.instance.email)
			return HttpResponseRedirect(request.path)
			

	else:
		form = UserRegistrationForm()		
	return render(request, 'main/register.html', {'form': form})


class UserApiAdd(generics.CreateAPIView): 
	serializer_class = UserSerializer

	def perform_create(self, serializer):
		user = serializer.save()
		send_register_email.delay(user.email)

class BookApiList(generics.ListCreateAPIView): #получение книг(get) и добавление книги (post)
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BookApiDetailView(generics.RetrieveUpdateDestroyAPIView): #получение информации о конкретной книге, изменение книги
	queryset = Book.objects.all()
	serializer_class = BookSerializer
