from django.shortcuts import render
from rest_framework import generics
from .models import Collect
from .serializers import CollectSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CollectListCreate(generics.ListCreateAPIView):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer

    @method_decorator(cache_page(60*5))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def perform_create(self, serializer):
        collect = serializer.save()
        send_collection_email(collect)


class CollectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        send_payment_email(payment)

    @method_decorator(cache_page(60*5))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def send_collection_email(collect):
    subject = f'Новая коллекция: {collect.name}'
    html_message = render_to_string('collection_email.html', {'collect': collect})
    plain_message = strip_tags(html_message)
    from_email = 'your_email@example.com'  # Ваша электронная почта
    to_email = collect.author.email  # Адрес электронной почты автора коллекции
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


def send_payment_email(payment):
    subject = 'Успешный платеж'
    message = f'Вы сделали платеж на сумму {payment.amount}.'
    from_email = 'your_email@example.com'  # Ваша электронная почта
    to_email = 'recipient@example.com'  # Адрес электронной почты получателя
    send_mail(subject, message, from_email, [to_email])
