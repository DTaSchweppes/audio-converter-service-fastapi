import shutil
from fastapi import UploadFile
from sqlalchemy.orm import Session
import uuid
from pyffmpeg import FFmpeg
from app.models.models import User, Audio
import os

ROOT_DIR = os.path.abspath(os.curdir) +'\\audio\\'


def create_user(db: Session, name: str):
    _user = User(name=name, uuid=uuid.uuid4())
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def converte_audio(exist_file_name_wav: str, file_mp3_name: str): #100% правильно сюда приходит
    ff = FFmpeg()
    try:
        output_file = ff.convert(exist_file_name_wav, file_mp3_name)
    except Exception:
        pass


def create_audio(db: Session, user_id: int, user_uuid: str, file: UploadFile):
    with open(ROOT_DIR + file.filename, "wb") as fl:
        shutil.copyfileobj(file.file, fl)
        file.file.close()
    converte_audio(ROOT_DIR +file.filename, ROOT_DIR +file.filename.replace("wav", "mp3")) #тут 100% правильно
    _audio = Audio(name=file.filename, user_uuid=user_uuid, user_id=user_id, uuid=uuid.uuid4())
    db.add(_audio)
    db.commit()
    db.refresh(_audio)
    return _audio


def get_audio(db: Session, record_id: int, user_id: int):
    return db.query(Audio).filter(Audio.id == record_id and Audio.user_id == user_id).first()
