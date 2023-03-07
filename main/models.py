from django.db import models

class Info(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to="logo/")
    text_uz = models.TextField()
    text_ru = models.TextField()

class Social_media(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="social_media/")
    link = models.URLField()
    
class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Discount(models.Model):
    img = models.ImageField(upload_to="discount/")

class Product(models.Model):
    img = models.ImageField(upload_to="product/")
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    price = models.IntegerField()

class About_Product(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    img = models.ImageField(upload_to="about_product/")

class About_Company(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()

class WhoUser(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

class HowToUse(models.Model):
    title_uz = models.CharField(max_length=266)
    title_ru = models.CharField(max_length=266)
    text_uz = models.TextField()
    text_ru = models.TextField()

class Fact(models.Model):
    number = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    