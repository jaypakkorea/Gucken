from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    username = models.EmailField(unique=True)
    # email = models.EmailField(
    # blank = False,
    # verbose_name='email',
    # max_length=50,
    # unique=True,
    # )
    
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)

class favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drama = models.IntegerField()
    comedy = models.IntegerField()
    action = models.IntegerField()
    thriller = models.IntegerField()
    adventure = models.IntegerField()
    anime  = models.IntegerField()