from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String)

    website = Column(String)

    score = Column(Integer)

    industry = Column(String)

    summary = Column(Text)

    email = Column(Text)