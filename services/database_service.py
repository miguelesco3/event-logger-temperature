from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataBaseService:

    def __init__(self,
                 host: str,
                 port: str,
                 username: str,
                 password: str,
                 database: str):

        self.engine = create_engine(f'postgres+psycopg2://{username}:{password}@{host}:{port}/{database}')
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.session()
