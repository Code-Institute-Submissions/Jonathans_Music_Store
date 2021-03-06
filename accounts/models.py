from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

class AccountUserManager(UserManager):
	def _create_user(email, password,
					 is_staff, is_superuser, **extra_fields):

		"""
		Creates and saves a User with an email and password
 		"""		  	

class User(AbstractUser):
	

	# Custom attribute added to user class
	
	stripe_id = models.CharField(max_length=30, default='')
	subscription_end = models.DateTimeField(default=timezone.now)
	city = models.CharField(max_length=40, default='')
	surname = models.CharField(max_length=40, default='')
	occupation = models.CharField(max_length=40, default='')
	objects = AccountUserManager()
