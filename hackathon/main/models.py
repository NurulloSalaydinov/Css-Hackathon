from django.db import models


class Contact(models.Model):
    full_name = models.CharField('Ism Familya', max_length=100)
    age = models.DateField('Tug\'ligan yili')
    phone = models.CharField('Telefon raqam', max_length=50)
    address = models.CharField('Yashash manzili', max_length=255)

    def __str__(self):
        return f"{self.full_name}"

