from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Collection(Base):
    __tablename__ = "collection"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    folder = Column(String)
    images = relationship("Image", back_populates="collection")
    def __repr__(self):
        return "Collection<id=%s, name=%s, file=%s>" % (self.id, self.name, self.folder)

class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file = Column(String)
    collection_id = Column(Integer, ForeignKey('collection.id'))
    collection = relationship("Collection", back_populates='images')

    def __repr__(self):
        return "Image<id=%s, name=%s, file=%s, collection=%s>" % (self.id, self.name, self.file, self.collection)

