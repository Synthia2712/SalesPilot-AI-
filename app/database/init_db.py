from app.database.database import Base
from app.database.database import engine

from app.database import models


def create_database():

    Base.metadata.create_all(bind=engine)