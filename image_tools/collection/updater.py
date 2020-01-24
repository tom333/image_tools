import os
import glob
import logging 
from pathlib import Path

from image_tools.models import Collection, Image


class CollectionUpdater:

    extensions = r"**/*.[png][jpg]*"

    def __init__(self, session):
        self.session = session

    def update(self):
        cpt = 0
        for col in self.session.query(Collection):
            logging.info("mise à jour de la collection %s ", col.name)
            for f in Path(col.folder).rglob('*.*'):
                if '.png' in f.suffix: 
                    cpt += self.create_or_update_image(f, col)
        
        self.session.commit()
        logging.info("%s images ajoutées dans la base" % cpt)

    def create_or_update_image(self, f, col):
        img = self.session.query(Image).filter_by(name=f.name, file=str(f.parents[0]), collection=col)
        if img is None:
            self.session.add(Image(name=f.name, file=str(f.parents[0]), collection=col))
            return 1
        return 0
