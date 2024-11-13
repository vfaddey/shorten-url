from sqlalchemy import Column, String, URL

from database.database import Base


class URLModel(Base):
    __tablename__ = 'urls'

    long_url = Column(String, primary_key=True, index=True, unique=True)
    short_url = Column(String, primary_key=True, index=True, unique=True)