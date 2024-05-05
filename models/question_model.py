# Description: Question model class to the database.
# Author: Sebastián Gámez Ariza


# Import the base class.
from models.base_model import Base

# Importing the SQLAlchemy libraries.
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Question(Base):
    __tablename__ = "question"
    id_question: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question: Mapped[str] = mapped_column(String(255))
    date: Mapped[str] = mapped_column(Date)

    def __repr__(self) -> str:
        return f"Question(id_question={self.id_question}, question={self.question}, date={self.date})"

