import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    like = relationship('Like', backref='user', lazy = True)
    comment = relationship('Comment', backref='user', lazy = True)
    follow = relationship('Follow', backref='user', lazy = True)

class Post (Base):
    __tablename__ = 'post'
    id_post = Column(Integer, primary_key=True)
    photo_url = Column(String(100))
    time_stamp = Column(String(50))
    caption = Column(String(300), nullable=True)
    like = relationship('Like', backref='post', lazy = True)

class Comment (Base):
    __tablename__ = 'comment'
    id_comment = Column(Integer, primary_key=True)
    comment_text = Column(String(200))
    time_stamp = Column(String(50))
    fk_user = Column(Integer, ForeignKey('user.id_user'), nullable = False)

class Like(Base):
    __tablename__ = 'like'
    id_like = Column(Integer, primary_key=True)
    fk_user = Column(Integer, ForeignKey('user.id_user'), nullable = False)
    fk_post = Column(Integer, ForeignKey('post.id_post'))

class Follow(Base):
    __tablename__ = 'follow'
    id_follow = Column(Integer, primary_key=True)
    fk_user = Column(Integer, ForeignKey('user.id_user'), nullable = False)
    fk_user = Column(Integer, ForeignKey('user.id_user'), nullable = False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')