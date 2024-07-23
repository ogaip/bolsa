import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user("john", "john@example.com", "secret")
    assert user.username == "john"
    assert user.email == "john@example.com"
    assert user.check_password("secret")


