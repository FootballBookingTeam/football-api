import pdb
from django.test import TestCase
from rest_framework.test import APITestCase
from ..models import User, Image, Schedule, Turf
from ..utils import *
from django.urls import reverse

# No delete, update url yet
class TestImage(APITestCase): 
    dataTurf = {
        'name': 'turf',
        'type': 'TURF7',
        'price': 100000.0,
        'rating': 5.0,
    }
    data = {
        'image' : 'ABC.png'
    }
    newData = {
        'image' : 'NewImage.png'
    }
    emtyData = {
        'image' : ''
    }
    errorData = {
        'image' : 1
    }

    def test_create_image_with_data(self):
        res = self.client.post(reverse('turfs'), self.dataTurf, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Turf.objects.count(),1)

        res_image = self.client.post(reverse('images', args=('1')), self.data, format='json')
        self.assertEqual(res_image.status_code, 200)
        self.assertEqual(Image.objects.count(),1)

    # def test_create_image_with_error_data(self):
    #     res = self.client.post(reverse('turfs'), self.dataTurf, format='json')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(Turf.objects.count(),1)

    #     res_image = self.client.post(reverse('images', args=('1')), self.emtyData, format='json')
    #     self.assertEqual(res_image.status_code, 400)
    #     self.assertEqual(Image.objects.count(),0)

    #     res_image = self.client.post(reverse('images', args=('1')), self.errorData, format='json')
    #     self.assertEqual(res_image.status_code, 400)
    #     self.assertEqual(Image.objects.count(),0)

    def test_create_image_with_no_turf(self):
        self.assertEqual(Turf.objects.count(),0)
        
        res_image = self.client.post(reverse('images', args=('1')), self.data, format='json')
        self.assertEqual(res_image.status_code, 400)
        self.assertEqual(Image.objects.count(),0)

    # def test_update_image_with_newData(self):
    #     res = self.client.post(reverse('turfs'), self.dataTurf, format='json')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(Turf.objects.count(),1)

    #     res_image = self.client.post(reverse('images', args=('1')), self.data, format='json')
    #     self.assertEqual(res_image.status_code, 200)
    #     self.assertEqual(Image.objects.count(),1)

    #     res_image = self.client.put(reverse('images', args=('1')), self.newData, format='json')
    #     self.assertEqual(res_image.status_code, 200)
    #     self.assertEqual(Image.objects.count(),1)

    def get_turf_images(self):
        res = self.client.post(reverse('turfs'), self.dataTurf, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Turf.objects.count(),1)

        res_image = self.client.post(reverse('images', args=('1')), self.data, format='json')
        self.assertEqual(res_image.status_code, 200)
        self.assertEqual(Image.objects.count(),1)

        res_image_2 = self.client.post(reverse('images', args=('1')), self.newData, format='json')
        self.assertEqual(res_image_2.status_code, 200)
        self.assertEqual(Image.objects.count(),2)

        res = self.client.get(reverse('images', args=('1')), format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data),2)