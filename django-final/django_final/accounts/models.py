from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    email = models.EmailField(
    blank = True,
    verbose_name='email',
    max_length=50,
    unique=True,
    )
    
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)