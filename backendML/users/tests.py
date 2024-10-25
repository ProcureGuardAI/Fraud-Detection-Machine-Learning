from . models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


class UserTestCase(APITestCase):

    """
    Test suite for Contact
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            full_name='Test User',
            email='testuser@example.com',
            phone_number='1234567890',
            role='Developer',
            department='Engineering',
            office_location='Headquarters',
            security_question="What is your first pet's name?",
            two_fa=True
        )
        self.url = "/users/"
    def test_user_creation(self):
            self.assertEqual(self.user.username, 'testuser')
            self.assertEqual(self.user.full_name, 'Test User')
            self.assertEqual(self.user.email, 'testuser@example.com')
            self.assertEqual(self.user.phone_number, '1234567890')
            self.assertEqual(self.user.role, 'Developer')
            self.assertEqual(self.user.department, 'Engineering')
            self.assertEqual(self.user.office_location, 'Headquarters')
            self.assertEqual(self.user.security_question, "What is your first pet's name?")
            self.assertTrue(self.user.two_fa)
            self.assertTrue(self.user.check_password('testpassword'))

    def test_create_contact_without_name(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_name_equals_blank(self):
        '''
        test ContactViewSet create method when name is blank
        '''
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_message(self):
        '''
        test ContactViewSet create method when message is not in data
        '''
        data = self.data
        data.pop("message")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_message_equals_blank(self):
        '''
        test ContactViewSet create method when message is blank
        '''
        data = self.data
        data["message"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_email(self):
        '''
        test ContactViewSet create method when email is not in data
        '''
        data = self.data
        data.pop("email")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_email_equals_blank(self):
        '''
        test ContactViewSet create method when email is blank
        '''
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_email_equals_non_email(self):
        '''
        test ContactViewSet create method when email is not email
        '''
        data = self.data
        data["email"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

