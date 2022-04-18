import pytest
from apps.users.models import User


def create_user(
    username: str,
    password: str,
    is_staff: bool = False,
    is_superuser: bool = False,
) -> User:
    return User.objects.create(
        username=username,
        password=password,
        is_staff=is_staff,
        is_superuser=is_superuser
    )


@pytest.fixture
def admin_user(db) -> User:
    return create_user(
        username='admin',
        password='admin',
        is_staff=True
    )


@pytest.fixture
def superadmin_user(db) -> User:
    return create_user(
        username='superadmin',
        password='superadmin',
        is_staff=True,
        is_superuser=True
    )


@pytest.fixture
def common_user(db) -> User:
    return create_user(
        username='common',
        password='common'
    )
