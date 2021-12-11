from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
 
            if not username:
                raise ValueError('Users must have an username')
            user = self.model(username=username)
            user.set_password(password)
            user.save(using=self._db)
            return user
    def create_superuser(self, username, password):

            user = self.create_user(
            username=username,
            password=password,
            )
            user.is_admin = True
            user.save(using=self._db)
            return user
        
class Usuario (AbstractBaseUser, PermissionsMixin):
    
    id             = models.BigAutoField(primary_key=True)
    nombre         = models.CharField('Nombre', max_length = 30)
    username       = models.CharField('Username', max_length = 15, unique=True)
    identificacion = models.IntegerField('Cedula', unique=True)
    password       = models.CharField('Password', max_length = 256)
    correo         = models.EmailField('correo', max_length = 100)
    telefono       = models.CharField ('telfono',max_length=30, null=False)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'