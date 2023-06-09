from sqlalchemy import Integer, String, Column, ForeignKey
from app.config import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "userstab1"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)

    audio = relationship("Audio",
                         back_populates="user")  # класс таблицы с кем связан, наименование объекта с кем связан


class Audio(Base):
    __tablename__ = "audiotab1"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    user_id = Column(Integer, ForeignKey("userstab1.id"))
    user_uuid = Column(String)

    user = relationship("User", back_populates="audio")