from datetime import timezone
from typing import Optional

from .base import get_db
from .models import User

UTC = timezone.utc


def create_user(email: str, password: str) -> User:
    db = get_db()

    user = User(email=email)
    user.set_password(password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_id(user_id: str) -> Optional[User]:
    return get_db().query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str) -> Optional[User]:
    return get_db().query(User).filter(User.email == email).first()


def verify_user_credentials(email: str, password: str) -> bool:
    user = get_db().query(User).filter(User.email == email).first()
    return user and user.verify_password(password)
