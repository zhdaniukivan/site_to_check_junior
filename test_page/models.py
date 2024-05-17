from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True)
    profile_creation_time = models.DateTimeField(default=timezone.now)
    last_visit_time = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'

# it is the signals thet create and save model Profile after change model user.
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

# delete these after created html page
# <h1>{{ user.get_full_name }}</h1>
#
#
#
# <ul>
#
#   <li>Имя пользователя: {{ user.username }}</li>
#
#   <li>Информация: {{ user.profile.bio }}</li>
#
#   <li>Дата рождения: {{ user.profile.birth_date }}</li>
#
# </ul>
#
#
#
# <div class="avatar">
#
#     <img src="{{ user.profile.avatar.url }}" alt="{{ user.username }}"/>
#
# </div>



class Question(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'M', 'Moderation'
        PUBLISHED = 'P', 'Published'

    class Language(models.TextChoices):
        Python = 'P', 'Python'
        JavaScript = 'JS', 'JavaScript'
        Java = 'J', 'Java'
        Typescript = 'T', 'Typescript'
        C = 'C#', 'C#'
        PHP = 'PHP', 'PHP'


    language = models.CharField(max_length=30, choices=Language.choices)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    added_by_user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()


    def __str__(self):
        return self.title

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    uset_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']


