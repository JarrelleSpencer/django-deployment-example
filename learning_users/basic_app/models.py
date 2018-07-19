from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    #Create relationship (dont inherit from the User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

# Once created model have to register to admin.py file for it to be recognised:
# admin.site.register(UserProfileInfo)
