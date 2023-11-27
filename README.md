# main
Для запуска программы в Docker выполните следующие действия/
1. Установите Docker
2. Откройте файл myproject/settings.py\
   Найдите строчки\
   EMAIL_HOST_USER = 'your_mail'\
   EMAIL_HOST_PASSWORD = 'your_password'\
   Введите данные от своей электронной почты. Это нужно для отправки сообщений при регистрации

3. Откройте консоль
4. Введите последовательно 2 команды\
   docker-compose build  - собирает образы контейнеров из Dockerfile и файлов docker-compose.yml\
   docker-compose up  - запускает контейнеры из файла docker-compose.yml\

6. Дождитесь завершения выполнения команд
7. Откройте адрес http://localhost:8000\
8. Логин от панели администратора 123, пароль 123\
9. При необходимости перед сборкой образа можете поменять их в файле docker-compose.yml\
   Строчка  echo 'from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.create_superuser(username=\"123\", email=\"your_email@example.com\"); user.set_password(\"123\"); user.save()' | python manage.py shell &&

   
    
