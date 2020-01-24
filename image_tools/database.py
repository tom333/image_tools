from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# class Database:
#     def __init__(self):
#         self.engine = create_engine('sqlite:///database.db', echo=True)
#         self.Base = declarative_base()
#         self.Base.metadata.create_all(self.engine)

#         Session = sessionmaker(bind=self.engine)
#         self.session = Session()


#     def __enter__(self):
#         return self.session

#     def __exit__(self, type_err, value, traceback):
#         pass