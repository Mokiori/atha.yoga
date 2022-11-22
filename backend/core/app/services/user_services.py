from functools import cached_property
from typing import Tuple

from core.app.services.types import UserRegisterData
from core.models import User, get_tokens_for_user, UserToken


class UserRegister:
    def __init__(self, data: UserRegisterData):
        self._data = data

    @cached_property
    def user(self) -> User:
        user = User()
        user.username = user.email = self._data["email"]
        user.set_password(self._data["password"])
        user.save()
        return user

    def register(self) -> Tuple[User, UserToken]:
        token_data = get_tokens_for_user(user=self.user)
        return self.user, token_data
