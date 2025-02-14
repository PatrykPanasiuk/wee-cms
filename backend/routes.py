from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.crud import get_all_posts, get_post, create_post, delete_post

router = APIRouter()

@router.get("/posts")
def list_posts(db: Session = Depends(get_db)):
    return get_all_posts(db)

@router.get("/posts/{post_id}")
def fetch_post(post_id: int, db: Session = Depends(get_db)):
    return get_post(db, post_id)

@router.post("/posts")
def add_post(title: str, content: str, db: Session = Depends(get_db)):
    return create_post(db, title, content)

@router.delete("/posts/{post_id}")
def remove_post(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)