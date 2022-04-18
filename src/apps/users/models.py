from typing import List
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


class User(AbstractUser):
    @staticmethod
    def get_admin_emails() -> List[str]:
        return User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
