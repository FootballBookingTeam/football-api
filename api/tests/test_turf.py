import pdb
from rest_framework.test import APITestCase
from ..models import Turf
from ..utils import *
from django.urls import reverse
class TestTurf(APITestCase):
    data = {
        'name': 'turf',
        'type': 'TURF7',
        'price': 100000.0,
        'rating': 5.0,
    }
    newData = {
        'name': 'updateTurf',
        'type': 'TURF5',
        'price': 85000.0,
        'rating': 4.5,
    }
    emptyData = {
        'name': '',
        'type': '',
        'price': 0.0,
        'rating': 0.0,
    }
    errorData = {
        'name': 'aa123',
        'type': 'TURF3',
        'price': -1.0,
        'rating': 6,
    },
    
    def test_create_turf_with_data(self):
        res = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Turf.objects.count(),1)
        self.assertEqual(Turf.objects.get().name, self.data['name'])

    def test_create_many_turf_with_data(self):
        res = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Turf.objects.count(),1)
        self.assertEqual(Turf.objects.get().name, self.data['name'])

        res_2 = self.client.post(reverse('turfs'), self.newData, format='json')
        self.assertEqual(res_2.status_code, 200)
        self.assertEqual(Turf.objects.count(),2)

    def test_create_turf_with_empty_data(self):
        res = self.client.post(reverse('turfs'), self.emptyData, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(Turf.objects.count(),0)
        
    def test_create_turf_with_error_data(self):
        res = self.client.post(reverse('turfs'), self.errorData , format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(Turf.objects.count(),0)
    
    def test_update_turf_with_new_data(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.get().id, 1)

        updateRes = self.client.put(reverse('turf' , args=('1')), self.newData, format='json')
        self.assertEqual(updateRes.status_code, 200)
        self.assertNotEqual(Turf.objects.get().name , self.data['name'])
        self.assertEqual(Turf.objects.get().name , self.newData['name'])
        self.assertEqual(Turf.objects.count(),1)
       
    def test_update_turf_with_empty_data(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.get().id, 1)

        updateRes = self.client.put(reverse('turf' , args=('1')), self.emptyData, format='json')
        self.assertEqual(updateRes.status_code, 400)
        self.assertEqual(Turf.objects.get().name , self.data['name'])
        self.assertEqual(Turf.objects.count(),1)
        
    def test_update_turf_with_error_data(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.get().id, 1)

        updateRes = self.client.put(reverse('turf' , args=('1')), self.errorData, format='json')
        self.assertEqual(updateRes.status_code, 400)
        self.assertEqual(Turf.objects.get().name , self.data['name'])
        self.assertEqual(Turf.objects.count(),1)
    
    def test_delete_turf(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.get().id, 1)
        self.assertEqual(Turf.objects.count(), 1)

        deleteRes = self.client.delete(reverse('turf', args=('1')), self.newData, format='json')
        self.assertEqual(deleteRes.status_code, 200)
        self.assertEqual(Turf.objects.count(), 0)

    def test_delete_many_turf(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        createRes_2 = self.client.post(reverse('turfs'), self.newData, format='json')
        self.assertEqual(createRes_2.status_code, 200)

        deleteRes = self.client.delete(reverse('turf', args=('1')), self.newData, format='json')
        self.assertEqual(deleteRes.status_code, 200)
        deleteRes_2 = self.client.delete(reverse('turf', args=('2')), self.newData, format='json')
        self.assertEqual(deleteRes_2.status_code, 200)

        self.assertEqual(Turf.objects.count(), 0)

    def get_turfs_list(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.get().id, 1)

        createRes_2 = self.client.post(reverse('turfs'), self.newData, format='json')
        self.assertEqual(createRes_2.status_code, 200)
        self.assertEqual(Turf.objects.count(), 2)

        res = self.client.get(reverse('turfs'), format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 2)
    
    def get_turf_detail(self):
        createRes = self.client.post(reverse('turfs'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.count(), 1)

        detailRes = self.client.get(reverse('turf', args=('1')), format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(Turf.objects.get().name, detailRes.data['name'])

    