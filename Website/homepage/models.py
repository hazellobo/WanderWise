from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    # user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

    # user_id = models.CharField(on_delete=models.DO_NOTHING)


    # Add any additional attributes you want
    phone_number = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
                                                                            

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    #instance.profile.username = User.objects.get('username')
    instance.userprofileinfo.save()


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfileInfo.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class CalculatePrice(models.Model):

    # user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='')

    departure_city = models.CharField(max_length=50, default='')
    adult = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    date_of_travel = models.DateField(max_length=10, default='')

    # def __str__(self):
    #     # Built-in attribute of django.contrib.auth.models.User !
    #     return self.departure_city
