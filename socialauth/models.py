import django
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not email:
            raise ValueError('Email requis !')

        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_user(self, email, password=None, **extra_fields):

        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(username, email, password, is_staff, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        return self._create_user(email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Nom & Prénom', max_length=140, default=None, null=True)
    username = models.CharField('username', max_length=140, default=None, null=True)
    email = models.EmailField('email address', max_length=140, unique=True, db_index=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password',]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
 
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
    	return str(self.email)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	prenom = models.CharField(max_length=30, blank=True)
	dateDeNaissance = models.DateField('date de naissance', null=True)