from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        user_data = {'username': 'yakubov', 'password': 'Sirojiddin'}
        create_user_response = self.client.post('/api/v1/user/auth/users/', user_data, format='json')

        self.assertEqual(create_user_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'yakubov')

        token_response = self.client.post('/api/v1/user/auth/jwt/create/', user_data, format='json')

        self.assertEqual(token_response.status_code, status.HTTP_200_OK)

        self.assertEqual(list(token_response.data.keys()), ['refresh', 'access'])
        access = token_response.data.get('access')
        refresh = token_response.data.get('refresh')


        login = self.client.post('/api/v1/user/login/', user_data, format='json')

        self.assertEqual(login.status_code, status.HTTP_200_OK)
        print(login.data)


