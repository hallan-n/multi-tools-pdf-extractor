import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)


DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()


def test_create_user(db_session):
    # Teste para criar um usuário no banco de dados
    user_data = {"username": "john_doe", "email": "john@example.com"}
    user = User(**user_data)
    db_session.add(user)
    db_session.commit()

    assert user.id is not None


def test_get_user(db_session):
    # Teste para obter um usuário do banco de dados
    user_data = {"username": "jane_doe", "email": "jane@example.com"}
    user = User(**user_data)
    db_session.add(user)
    db_session.commit()

    retrieved_user = db_session.query(User).filter(User.username == "jane_doe").first()
    assert retrieved_user is not None
