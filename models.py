from typing import List
from typing import Optional
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database import engine


class Base(DeclarativeBase):
    pass


class Curator(Base):
    __tablename__ = "curator"
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))

    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.firstname!r}, fullname={self.lastname!r})"


class Departments(Base):
    __tablename__ = "departments"
    id: Mapped[int] = mapped_column(primary_key=True)
    finances: Mapped[float]
    name: Mapped[str]
    faculty_id: Mapped[int] = mapped_column(ForeignKey("faculty.id"))
    faculty: Mapped["Faculty"] = relationship(back_populates="departments")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.name!r})"


class Faculty(Base):
    __tablename__ = "faculty"
    id: Mapped[int] = mapped_column(primary_key=True)
    finances: Mapped[float]
    name: Mapped[str]
    department_id: Mapped[int] = mapped_column(ForeignKey("faculty.id"))
    department: Mapped["Departments"] = relationship(back_populates="faculty")

    departments: Mapped[List["Departments"]] = relationship(
        back_populates="faculty", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.name!r})"


association_table = Table(
    "association_table",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id")),
    Column("lection_id", ForeignKey("lections.id")),
)


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    finances: Mapped[float]
    year: Mapped[int]
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
    department: Mapped["Faculty"] = relationship(back_populates="groups")



class Lection(Base):
    __tablename__ = "lections"
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str]
    cabinet: Mapped[int]
    group: Mapped[List[Group]] = relationship(
        secondary=association_table, back_populates="lection"
    )


Base.metadata.create_all(engine)