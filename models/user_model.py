# Description: User model class to the database.
# Author: Sebastián Gámez Ariza

# Import the types from typing.
from typing import List

# Import the base and analysis class.
from models.base_model import Base
from models.analysis_model import Analysis

# Importing the SQLAlchemy libraries.
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id_user: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(45))
    email: Mapped[str] = mapped_column(String(45))
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(45))

    analysis: Mapped[List["Analysis"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id_user={self.id_user}, name={self.name}, email={self.email}, role={self.role})"
