from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from test_page.models import Profile

class ProfileModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test_user_name_0')
        profile = Profile.objects.get(user=user)
        profile.location = 'Minsk'
        profile.birth_date = timezone.now()
        profile.gender = Profile.Gender.MALE
        profile.save()


    def test_profile_creation_signal(self):
        user = User.objects.create(username='test_user_name_1')
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_profile_data_model(self):
        profile = Profile.objects.get(id=1).location
        self.assertEqual(profile, 'Minsk')

    def test_profile_location_label(self):
        profile = Profile.objects.get(id=1)
        label = profile._meta.get_field('location').verbose_name
        self.assertEqual(label, 'location')

    def test_profile_location_max_light(self):
        profile = Profile.objects.get(id=1)
        max_length_for_location = profile._meta.get_field('location').max_length
        self.assertEqual(max_length_for_location, 30)

    def test_profile_birth_date_label(self):
        profile = Profile.objects.get(id=1)
        label = profile._meta.get_field('birth_date').verbose_name
        self.assertEqual(label, 'birth date')

    def test_profile_gender_label(self):
        profile = Profile.objects.get(id=1)
        label = profile._meta.get_field('gender').verbose_name
        self.assertEqual(label, 'gender')

    def test_profile_gender_max_light(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('gender').max_length
        self.assertEqual(max_length, 1)

