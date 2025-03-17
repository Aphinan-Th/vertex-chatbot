from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import DATABASE_URL, SQLALCHEMY_ECHO

engine = create_engine(
    DATABASE_URL,
    echo=SQLALCHEMY_ECHO,
    pool_pre_ping=True,
    pool_recycle=3600,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(SessionLocal)

Base = declarative_base()
Base.query = db_session.query_property()


def get_db():
    db = db_session()
    try:
        return db
    finally:
        db.close()


def init_db():
    from .models import User  # noqa: F401

    Base.metadata.create_all(bind=engine)
