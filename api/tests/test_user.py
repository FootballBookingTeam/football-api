import pdb
from rest_framework.test import APITestCase
from ..models import User
from ..utils import *
from django.urls import reverse
class TestUser(APITestCase):
    data = {
        'name': 'admin',
        'phone': '0354175296',
        'username': 'Admin',
        'password': 'admin123',
        'role' : 'ADMIN',
    }
    newData = {
        'name': 'updateName',
        'phone': '0354179999',
        'username': 'updateAdmin',
        'password': 'admin123',
        'role' : 'ADMIN',
    }
    emptyData = {
        'name' : '',
        'phone': '',
        'username': '',
        'password': '',
        'role' : '',
    }
    errorData = {
        'name' : 'abc123',
        'phone': '123a21abxa',
        'username': '0.3',
        'password': '1/2',
        'role' : '-12',
    },
    dataLogin = {
        'data' : {
            'username' : 'admin',
            'password': 'admin123'
        }
    }
    
    def test_create_user_with_data(self):
        res = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.get().name, self.data['name'])

    def test_create_many_user_with_data(self):
        res = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.get().name, self.data['name'])

        res_2 = self.client.post(reverse('users'), self.newData, format='json')
        self.assertEqual(res_2.status_code, 200)
        self.assertEqual(User.objects.count(),2)

    def test_create_user_with_empty_data(self):
        res = self.client.post(reverse('users'), self.emptyData, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(User.objects.count(),0)
        
    def test_create_user_with_error_data(self):
        res = self.client.post(reverse('users'), self.errorData , format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(User.objects.count(),0)

    def test_create_user_already_exists(self):
        res = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(res.status_code, 200)
        res_2 = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(res_2.status_code, 400)
        self.assertEqual(User.objects.count(),1)
    
    def test_update_user_with_new_data(self):
        createRes = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(User.objects.get().id, 1)

        updateRes = self.client.put(reverse('user' , args=('1')), self.newData, format='json')
        self.assertEqual(updateRes.status_code, 200)
        self.assertNotEqual(User.objects.get().name , self.data['name'])
        self.assertEqual(User.objects.get().name , self.newData['name'])
        self.assertEqual(User.objects.count(),1)
       
    def test_update_user_with_empty_data(self):
        createRes = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(User.objects.get().id, 1)

        updateRes = self.client.put(reverse('user' , args=('1')), self.emptyData, format='json')
        self.assertEqual(updateRes.status_code, 400)
        self.assertEqual(User.objects.get().name , self.data['name'])
        self.assertEqual(User.objects.count(),1)
        
    def test_update_user_with_error_data(self):
        createRes = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(User.objects.get().id, 1)

        updateRes = self.client.put(reverse('user' , args=('1')), self.errorData, format='json')
        self.assertEqual(updateRes.status_code, 400)
        self.assertEqual(User.objects.get().name , self.data['name'])
        self.assertEqual(User.objects.count(),1)

    def test_update_user_with_another_user_already_exists(self):
        createRes = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(User.objects.get().id, 1)

        createRes_2 = self.client.post(reverse('users'), self.newData, format='json')
        self.assertEqual(createRes_2.status_code, 200)
        self.assertEqual(User.objects.count(), 2)

        updateRes = self.client.put(reverse('user', args=('1')), self.newData, format='json')
        self.assertEqual(updateRes.status_code, 400)
        self.assertEqual(User.objects.count(), 2)

    
    def test_delete_user(self):
        createRes = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        self.assertEqual(User.objects.get().id, 1)
        self.assertEqual(User.objects.count(), 1)

        deleteRes = self.client.delete(reverse('user', args=('1')), self.newData, format='json')
        self.assertEqual(deleteRes.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_delete_many_user(self):
        createRes = self.client.post(reverse('users'), self.data, format='json')
        self.assertEqual(createRes.status_code, 200)
        createRes_2 = self.client.post(reverse('users'), self.newData, format='json')
        self.assertEqual(createRes_2.status_code, 200)

        deleteRes = self.client.delete(reverse('user', args=('1')), self.newData, format='json')
        self.assertEqual(deleteRes.status_code, 200)
        deleteRes_2 = self.client.delete(reverse('user', args=('2')), self.newData, format='json')
        self.assertEqual(deleteRes_2.status_code, 200)

        self.assertEqual(User.objects.count(), 0)
