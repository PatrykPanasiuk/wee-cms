from sqlalchemy.orm import Session
from backend.models import Post

def get_all_posts(db: Session):
    """Fetch all posts from the database."""
    return db.query(Post).all()

def get_post(db: Session, post_id: int):
    """Fetch a single post by ID."""
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, title: str, content: str):
    """Create a new post."""
    new_post = Post(title=title, content=content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def delete_post(db: Session, post_id: int):
    """Delete a post by ID."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post