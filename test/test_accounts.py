# test_account.py
import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User


def test_register_view(client):
    response = client.get(reverse('register'))
    assert response.status_code == 200
    assert 'form' in response.context


@pytest.mark.django_db
def test_register_user(client):
    response = client.post(reverse('register'), {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'testpassword',
    })
    assert response.status_code == 302
    assert User.objects.filter(username='testuser').exists()


def test_login_view(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assert 'form' in response.context


@pytest.mark.django_db
def test_login_user(client):
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'testpassword',
    }, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain[0][0] == reverse('perfil')

