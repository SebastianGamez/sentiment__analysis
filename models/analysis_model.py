# Description: Analysis model class to the database.
# Author: Sebastián Gámez Ariza


# Import the base, user and question class.
from models.base_model import Base
from models.user_model import User
from models.question_model import Question

# Importing the SQLAlchemy libraries.
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Analysis(Base):
    __tablename__ = "analysis"
    id_analysis: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pos: Mapped[str] = mapped_column(Float)
    neg: Mapped[str] = mapped_column(Float)
    neu: Mapped[str] = mapped_column(Float)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id_question"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id_user"))

    question: Mapped["Question"] = relationship(back_populates="analysis")
    user: Mapped["User"] = relationship(back_populates="analysis")

    def __repr__(self) -> str:
        return f"Analysis(id_analysis={self.id_analysis}, pos={self.pos}, neg={self.neg}, neu={self.neu}, question_id={self.question_id}, user_id={self.user_id})"
