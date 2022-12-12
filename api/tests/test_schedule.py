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
        "total_price": 10001.0,
        "user": 1,
        "turf": 1
    }
    newData = {
        "name": "newSchedule",
        "start_time": "2022-10-30T01:46:56Z",
        "end_time": "2022-10-30T01:46:58Z",
        "status": "DONE",
        "total_price": 10000.0,
        "user": 1,
        "turf": 1
    }

    errorData = {
        "name": "",
        "start_time": "2022-11-30T01:46:56Z",
        "end_time": "2022-11-30T01:46:58Z",
        "status": "",
        "total_price": '10000.0',
        "user": 1,
        "turf": 1
    }

    userData = {
        'name': 'updateName',
        'phone': '0354179999',
        'username': 'updateAdmin',
        'password': 'admin123',
        'role' : 'ADMIN',
    }
    turfData = {
        'name': 'turf',
        'type': 'TURF7',
        'price': 100000.0,
        'rating': 5.0,
    }

    def create_schedule_without_user_turf(self):
        res = self.client.post(reverse('schedules'), self.data, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(Schedule.objects.count() , 0)


    def create_schedule_with_user_turf(self):
        res_user = self.client.post(reverse('users'), self.userData, format='json')
        res_turf = self.client.post(reverse('turfs'), self.turfData, format='json')
        res = self.client.post(reverse('schedules'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 1)

    def create_schedule_without_data(self):
        res_user = self.client.post(reverse('users'), self.userData, format='json')
        res_turf = self.client.post(reverse('turfs'), self.turfData, format='json')
        res = self.client.post(reverse('schedules'), self.errorData, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(Schedule.objects.count() , 0)
        pdb.set_trace()

    def update_schedule_exist(self):
        res_user = self.client.post(reverse('users'), self.userData, format='json')
        res_turf = self.client.post(reverse('turfs'), self.turfData, format='json')
        res = self.client.post(reverse('schedules'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 1)
        res_update = self.client.patch(reverse('schedule', args=('1')), self.newData, format='json')
        self.assertEqual(res_update.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 1)

    def update_schedule_without_user_turf(self):
        res_user = self.client.post(reverse('users'), self.userData, format='json')
        res_turf = self.client.post(reverse('turfs'), self.turfData, format='json')
        res = self.client.post(reverse('schedules'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 1)
        self.data['user'] = '2'
        self.data['turf'] = '2'
        res_update = self.client.patch(reverse('schedule', args=('1')), self.data, format='json')
        self.assertEqual(res_update.status_code, 400)
        self.assertEqual(Schedule.objects.count() , 1)

    def get_schedules_list(self):
        res_user = self.client.post(reverse('users'), self.userData, format='json')
        res_turf = self.client.post(reverse('turfs'), self.turfData, format='json')
        res = self.client.post(reverse('schedules'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 1)
        res2 = self.client.post(reverse('schedules'), self.newData, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 2)

        res_get = self.client.get(reverse('schedules'), format='json')
        self.assertEqual(res_get.status_code, 200)
        self.assertEqual(len(res_get.data) , 2)

    def get_schedule(self):
        res_user = self.client.post(reverse('users'), self.userData, format='json')
        res_turf = self.client.post(reverse('turfs'), self.turfData, format='json')
        res = self.client.post(reverse('schedules'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Schedule.objects.count() , 1)
        res_get = self.client.patch(reverse('schedule', args=('1')), format='json')
        self.assertEqual(res_get.status_code, 200)
        self.assertEqual(res_get.data['total_price'] , 10001.0)
