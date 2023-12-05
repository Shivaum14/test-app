from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime as SADateTime
from sqlalchemy import inspect
from .utils import generate_uid, get_db_connection_url

# Configure your database
engine = create_engine(get_db_connection_url())
Session = sessionmaker(bind=engine)
Base = declarative_base()


class BaseMixin:
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)

#     def __repr__(self):
#         return f"<User {self.name}>"


class Todo(Base, BaseMixin):
    __tablename__ = "todo"
    id = Column(String, primary_key=True, default=generate_uid)
    value = Column(String, nullable=False)
    date = Column(SADateTime, nullable=True)

    def __repr__(self):
        return f"<TODO {self.value}>"


# Create tables
Base.metadata.create_all(engine)
