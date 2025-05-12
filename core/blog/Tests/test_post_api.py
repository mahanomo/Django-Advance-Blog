from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime

from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user_obj = User.objects.create_user(email="test@fortest.com", password="A@/a123456")
    return user_obj


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_list_response_200(self, api_client):
        url = reverse("blog:api-v1:p-modelviewset-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self, api_client):
        url = reverse("blog:api-v1:p-modelviewset-list")
        data = {
            "title": "title test",
            "content": "description test",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201(self, api_client, common_user):
        url = reverse("blog:api-v1:p-modelviewset-list")
        data = {
            "title": "title test",
            "content": "description test",
            "status": True,
            "published_date": datetime.now(),
        }
        api_client.force_login(common_user)
        # or use this: api_client.force_authenticate(common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_with_invalid_data_response_400(self, api_client, common_user):
        url = reverse("blog:api-v1:p-modelviewset-list")
        data = {
            "title": "title test",
            "content": "description test",
        }
        api_client.force_login(common_user)
        # or use this: api_client.force_authenticate(common_user)
        response = api_client.post(url, data)
        assert response.status_code == 400
