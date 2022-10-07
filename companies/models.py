from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import post_save 
from django.dispatch import receiver


# Create your models here.

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    logo = models.FileField(upload_to='companies/images', null=True, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.user.name

    @receiver(post_save, sender=User)
    def create_company_profile(sender, instance, created, **kwargs):
        if created:
            if instance.is_company == True:
                CompanyProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_company_profile(sender, instance, **kwargs):
        if instance.is_company == True:
            instance.companyprofile.save()