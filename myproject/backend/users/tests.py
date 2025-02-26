from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser, Pref


class TestUserViewSet(TestCase):
    def setUp(self):
        # GIVEN: A Pref object with the name "Tokyo" is created
        self.client = APIClient()
        self.pref = Pref.objects.create(name="Tokyo")

        # GIVEN: A set of valid user data is provided
        self.user_data = {
            "username": "testuser",
            "password": "Testpassword123",
            "email": "testuser@example.com",
            "pref_id": self.pref.id,
            "tel": "1234567890",
        }
        # GIVEN: The URL for the UserViewSet
        self.url = reverse("users-list")  # This is the DRF router name for UserViewSet

    def test_register_user(self):
        # WHEN: A POST request is made to the users-list endpoint with valid user data
        response = self.client.post(self.url, self.user_data, format="json")

        # THEN: The response status code should be 201 Created
        assert response.status_code == status.HTTP_201_CREATED

        # THEN: The CustomUser object should be created in the database
        assert CustomUser.objects.filter(username="testuser").exists()

        # THEN: Verify that the password is hashed correctly
        user = CustomUser.objects.get(username="testuser")
        assert check_password(self.user_data["password"], user.password)

    def test_register_user_missing_fields(self):
        # GIVEN: A set of incomplete user data with only the username provided
        data = {"username": "testuser"}

        # WHEN: A POST request is made with the incomplete data
        response = self.client.post(self.url, data, format="json")

        # THEN: The response status code should be 400 Bad Request
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_invalid_pref(self):
        # GIVEN: A Pref object with the name "Tokyo" exists
        # GIVEN: Invalid pref_id (9999) is provided, which does not exist
        data = {
            "username": "testuser",
            "password": "Testpassword123",
            "email": "testuser@example.com",
            "pref_id": 9999,  # Invalid pref_id
            "tel": "1234567890",
        }

        # WHEN: A POST request is made with the invalid pref_id
        response = self.client.post(self.url, data, format="json")

        # THEN: The response status code should be 400 Bad Request
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_invalid_tel(self):
        # GIVEN: A Pref object with the name "Tokyo" exists
        # GIVEN: Invalid tel (non-numeric "abcd") is provided
        data = {
            "username": "testuser",
            "password": "Testpassword123",
            "email": "testuser@example.com",
            "pref_id": self.pref.id,
            "tel": "abcd",  # Invalid tel (non-numeric)
        }

        # WHEN: A POST request is made with the invalid tel
        response = self.client.post(self.url, data, format="json")

        # THEN: The response status code should be 400 Bad Request
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_duplicate_email(self):
        # GIVEN: A CustomUser with the email "testuser@example.com" already exists
        CustomUser.objects.create_user(
            username="testuser1",
            password="testpassword123",
            email="testuser@example.com",
            pref=self.pref,
        )

        # GIVEN: A new user is being registered with the same email
        data = {
            "username": "testuser2",
            "password": "testpassword123",
            "email": "testuser@example.com",  # Duplicate email
            "pref_id": self.pref.id,
            "tel": "1234567890",
        }

        # WHEN: A POST request is made with the duplicate email
        response = self.client.post(self.url, data, format="json")

        # THEN: The response status code should be 400 Bad Request
        assert response.status_code == status.HTTP_400_BAD_REQUEST
