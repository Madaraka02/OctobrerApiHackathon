from django.db import models
from companies.models import CompanyProfile
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import post_save 
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.FileField(upload_to='advocates/images', null=True, blank=True)
    short_bio = models.CharField(max_length=300,blank=True)
    long_bio = models.TextField(blank=True)
    advocate_years_exp = models.PositiveIntegerField(default=1)
    company = models.ForeignKey(CompanyProfile, related_name='advocates', on_delete=models.SET_NULL, null=True)
    youtube = models.URLField(null=True,blank=False)
    twitter = models.URLField(null=True,blank=False)
    github = models.URLField(null=True,blank=False)


    @property
    def links(self):
        links={
            'youtube': self.youtube,
            'twitter': self.twitter,
            'github': self.github
        }
        return links

    def __str__(self):
        return self.user.name


    @receiver(post_save, sender=User)
    def create_advocate_profile(sender, instance, created, **kwargs):
        if created:
            if instance.is_advocate == True:
            # instance.is_advocate
                Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_advocate_profile(sender, instance, **kwargs):
        if instance.is_advocate == True:
            instance.profile.save()