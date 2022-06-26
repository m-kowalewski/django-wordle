''' WordleColourResult app tests '''
import datetime
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from WordleColourResult.models import RealUserResult
# Create your tests here.

rdate = datetime.date.today()
rtime = datetime.time(0,0,0)
user_string = str(rdate) + ' user123'

class RealUserResultTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user123 = User.objects.create_user('user123','user123@user.com','topsecret')     
        RealUserResult.objects.create(owner=self.user123, result_date=rdate, result_time=rtime)

    def test_real_user_result(self):
        user_test = RealUserResult.objects.get(owner = User.objects.get(username='user123'))
        self.assertEqual(str(user_test), '2022-06-26 user123')

