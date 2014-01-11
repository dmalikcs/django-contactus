from django.db import models
from django import forms


class ContactUs(models.Model):
    STATUS = (
        ('N', 'New'),
        ('c', 'closed'),
        ('f', 'fake'),
        ('w', 'working'),
    )
    name = models.CharField(
        max_length=30,
    )
    email = models.EmailField()
    message = models.TextField(
        max_length=200,
    )
    status = models.CharField(
        choices=STATUS,
        max_length=2,
        verbose_name='Status',
        default='N'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('status', )
