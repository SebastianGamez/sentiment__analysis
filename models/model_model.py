# Description: Base model class to the database.
# Author: Sebastián Gámez Ariza


# Importing the SQLAlchemy libraries.
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Date, Float, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# Import the datetime library.
from datetime import date

# Import the types from typing.
from typing import List


# Creating the Base class.
class Base(DeclarativeBase):
    pass


# Create the user model
class User(Base):
    __tablename__ = "user"
    id_user: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(45))
    email: Mapped[str] = mapped_column(String(45))
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(45))

    analyses: Mapped[List["Analysis"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id_user={self.id_user}, name={self.name}, email={self.email}, role={self.role})"


# Create the analysis model
class Analysis(Base):
    __tablename__ = "analysis"
    id_analysis: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    answer: Mapped[str] = mapped_column(String(255))
    pos: Mapped[float] = mapped_column(Float)
    neg: Mapped[float] = mapped_column(Float)
    neu: Mapped[float] = mapped_column(Float)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id_question"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id_user"))

    question: Mapped["Question"] = relationship(back_populates="analyses")
    user: Mapped["User"] = relationship(back_populates="analyses")

    def __repr__(self) -> str:
        return f"Analysis(id_analysis={self.id_analysis}, pos={self.pos}, neg={self.neg}, neu={self.neu}, question_id={self.question_id}, user_id={self.user_id}), question={self.question}, user={self.user}"


# Create the question model
class Question(Base):
    __tablename__ = "question"
    id_question: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question: Mapped[str] = mapped_column(String(255))
    date: Mapped[str] = mapped_column(Date, default=date.today())

    analyses: Mapped["Analysis"] = relationship(back_populates="question")

    def __repr__(self) -> str:
        return f"Question(id_question={self.id_question}, question={self.question}, date={self.date})"

