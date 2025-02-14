from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class Post(Base):
    """Post model for SQLite3 database."""
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)