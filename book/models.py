from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class NewBook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


def send_create(sender, instance, created, **kwargs):
    if instance.title:

        recievers = []
        for user in Client.objects.all():
            recievers.append(user.email)

        message = f"Description: \n {instance.description}"
        subject = f"The new book of {instance.title} is already in the store"
        send_mail(subject, message, 'email@gmail.com', recievers)

post_save.connect(send_create, sender=NewBook)
