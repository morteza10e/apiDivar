from datetime import timezone

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, bio=None, is_active=True,
                    city=None, phone_number=None,
                    is_staff=False, is_superuser=False):
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email,
                          username=username,
                          bio=bio,
                          city=city,
                          phone=phone_number,
                          is_active=is_active,
                          is_staff=is_staff,
                          is_superuser=is_superuser)
        user.set_password(password)

        user.save(using=self._db)
        return user


def createsuperuser(self, username, email, password, **kwargs):
    kwargs.setdefault("is_staff", True)
    kwargs.setdefault("is_superuser", True)

    if kwargs.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')
    if kwargs.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

    return self.create_user(username, email, password, **kwargs)
