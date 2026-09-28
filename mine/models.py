from  datetime import datetime
from sqlalchemy.orm import*
from sqlalchemy import *
from mine.db import Base

class creatingrecord(Base):
    __tablename__="posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True,nullable=False)
    email:Mapped[str]=mapped_column(unique=True,nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False
    )