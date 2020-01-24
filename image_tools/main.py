import logging

from database import session
from image_tools.collection.updater import CollectionUpdater
# from models import Collection, Image

# col = Collection(name="Collection 1", folder="/media/sf_D_DRIVE/Perso")
# session.add(col)

# img = Image(name='photo1.jpg', file='photo1.jpg', collection=col)

# session.add(img)
# session.commit()
import logging.config

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'INFO',
        },
        'image_tools': {
            'level': 'DEBUG',
        },
    }
}
logging.config.dictConfig(DEFAULT_LOGGING)

CollectionUpdater(session).update()