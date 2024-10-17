import json
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from texnomart.models import Category, Product
from django.core.mail import send_mail
from django.conf import settings
import os
DELETED_PRODUCTS_FILE = 'deleted_products.json'
DELETED_CATEGORIES_FILE = 'deleted_categories.json'

@receiver(post_save, sender=Category)
def send_email_after_category_creation(sender, instance, created, **kwargs):
    if created:
        subject = 'Yangi Category yaratildi'
        message = f"Yangi Category: {instance.title} yaratildi."
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['abdulazizovasilbek005@gmail.com'])  # Email yuboruvchi va qabul qiluvchilar ro'yxati

@receiver(post_save, sender=Product)
def send_email_after_product_creation(sender, instance, created, **kwargs):
    if created:
        subject = 'Yangi mahsulot yaratildi'
        message = f"Yangi mahsulot: {instance.name} yaratildi. Narxi: {instance.price}."
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['abdulazizovasilbek005@gmail.com'])



def save_to_json(data, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []
    existing_data.append(data)

    with open(file_name, 'w') as file:
        json.dump(existing_data, file, indent=4)

@receiver(pre_delete, sender=Product)
def save_deleted_product(sender, instance, **kwargs):
    product_data = {
        'id': instance.id,
        'name': instance.name,
        'description': instance.description,
        'price': instance.price,
        'quantity': instance.quantity,
        'deleted_at': str(instance.updated_at)
    }
    save_to_json(product_data, DELETED_PRODUCTS_FILE)

@receiver(pre_delete, sender=Category)
def save_deleted_category(sender, instance, **kwargs):
    category_data = {
        'id': instance.id,
        'title': instance.title,
        'description': instance.description,
        'deleted_at': str(instance.updated_at)
    }
    save_to_json(category_data, DELETED_CATEGORIES_FILE)






# @receiver(pre_delete, sender=Product)
# def save_deleted_product_to_json(sender, instance, **kwargs):
#     file_path = os.path.join(settings.BASE_DIR, 'deleted_products.json')
#
#     product_data = {
#         'name': instance.name,
#         'description': instance.description,
#         'price': instance.price,
#         'quantity': instance.quantity,
#         'slug': instance.slug
#     }
#
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#     else:
#         data = []
#     data.append(product_data)
#
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)
#
# @receiver(pre_delete, sender=Category)
# def save_deleted_category_to_json(sender, instance, **kwargs):
#     file_path = os.path.join(settings.BASE_DIR, 'deleted_categories.json')
#
#     category_data = {
#         'title': instance.title,
#         'description': instance.description,
#         'slug': instance.slug
#     }
#
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#     else:
#         data = []
#
#     data.append(category_data)
#
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)