import hashlib
import uuid

from sqlalchemy import (
    Column,
    DateTime,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    email = Column(String(255), nullable=False)
    password_hash_sha256 = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    gender = Column(String(255), nullable=True)
    age = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())

    def set_password(self, raw_password):
        self.password_hash_sha256 = hashlib.sha256(raw_password.encode()).hexdigest()

    def verify_password(self, raw_password):
        return (
            self.password_hash_sha256
            == hashlib.sha256(raw_password.encode()).hexdigest()
        )
