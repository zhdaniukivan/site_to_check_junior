import django.utils.timezone
from django.test import TestCase
from django.contrib.auth.models import User
from test_page.models import Profile

class ProfileModelsTest(TestCase):
    def test_profile_creation_signal(self):
        user = User.objects.create(username='test_user_name_1')
        self.assertTrue(Profile.objects.filter(user=user).exists())
        profile = Profile.objects.get(user=user)
        profile.location = 'Minsk'
        profile.birth_date = '2000-01-01'
        profile.gender = Profile.Gender.MALE
        profile.save()
        profile_2 = Profile.objects.get(user=user).location
        self.assertEqual(profile_2, 'Minsk')
    # def setUp(self):
    #     user = User.objects.create(username='testuser1')
    #     profile = Profile.objects.create(user_id=user.id, location='Test Location',
    #                                            birth_date=django.utils.timezone.now(), gender=Profile.Gender.MALE)
    #
    # def tearDown(self):
    #     pass
    #
    # def test_profile_user(self):
    #     username = User.objects.get(id=1).username
    #
    #     self.assertEqual(username, 'testuser1')  # Исправлено на assertEqual
    #
    # def test_location_max_light(self):
    #     max_light = Profile.objects.get(id=1)

    # def test_profile_creation(self):
    #
    #     profile_locaton = Profile.objects.get(user_id=1).location
    #
    #     self.assertEqual(profile_locaton, 'Test Location')