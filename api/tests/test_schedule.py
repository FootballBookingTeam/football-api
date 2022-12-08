import pdb
from rest_framework.test import APITestCase
from ..models import Turf
from ..utils import *
from django.urls import reverse

class TestSchedule(APITestCase):
    data = {
        "name": "admin",
        "start_time": "2022-11-30T01:46:56Z",
        "end_time": "2022-11-30T01:46:58Z",
        "status": "DONE",
        "total_price": 10000.0,
        "user": 1,
        "turf": 1
    }

    newData = {
        'name': 'updateName',
        'phone': '0354179999',
        'username': 'updateAdmin',
        'password': 'admin123',
        'role' : 'ADMIN',
    }

    def create_schedule_without_user_turf(self):
        res_2 = self.client.post(reverse('users'), self.data, format='json')
        res = self.client.post(reverse('schedules'), self.data, format='json')
        pdb.set_trace()