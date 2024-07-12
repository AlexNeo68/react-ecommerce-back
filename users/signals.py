from django.contrib.auth.models import User
from django.db.models.signals import pre_save


def pre_save_user(sender, instance, **kwargs):
    print('signal pre_save_user')
    if instance.email != '':
        instance.username = instance.email


pre_save.connect(pre_save_user, sender=User)
