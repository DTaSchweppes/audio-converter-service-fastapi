from app import operations
from app.config import SessionLocal
from fastapi import APIRouter, Depends, UploadFile, Query
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.models.schemas import User

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/user")
def create_user_service(user: User, db: Session = Depends(get_db)):
    result = operations.create_user(db, name=user.name)
    return {"user id": result.id, "generated uuid": result.uuid}


@router.post('/audio')
def create_service_audio(user_id: int, user_uuid: str, file: UploadFile, db: Session = Depends(get_db)):
    result = operations.create_audio(db, user_id, user_uuid, file)
    return {"url": f"http://127.0.0.1:8000/record?{result.id}&user={result.user_id}"}


@router.get('/audio')
def get_audio_service(record_id: int = Query(gt=0), user_id: int = Query(gt=0),
                      db: Session = Depends(get_db)):
    result = operations.get_audio(db, record_id, user_id)
    # return {"sa": result.name.replace(".wav",".mp3"), "s": result.name}
    return FileResponse(result.name.replace(".wav", ".mp3"), filename=result.name.replace(".wav", ".mp3"))
