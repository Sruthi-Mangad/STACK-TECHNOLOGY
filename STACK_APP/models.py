from django.db import models
from distutils.command.upload import upload
import email
from hashlib import blake2b
from random import choices
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.

userchoices = (
    (1, "ADMIN"),
    (2, "STAFF"),
    (3, "STUDENT"),
)


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']

    name = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.IntegerField(default=1, choices=userchoices)
    phone_number = models.CharField(max_length=13, null=True,blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    staff_id = models.CharField(max_length=13, unique=True, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class BLOG(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class COURSES(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    course_id = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    fee = models.IntegerField(null=True, blank=True)
    # link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class TESTIMONIAL(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    uploaded_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FEATURES(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True, upload_to='images/')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class ABOUT_US(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class INSTRUCTORS(models.Model):
    profile = models.ImageField(null=True, blank=True, upload_to='images/')
    name = models.CharField(max_length=255, null=True, blank=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

mail_status = (
    (1, "Read"),
    (0, "Unread"),
)

class CONTACT_US(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    status = models.IntegerField(default=0, null=True, blank=True, choices=mail_status)

    def __str__(self):
        return self.name

