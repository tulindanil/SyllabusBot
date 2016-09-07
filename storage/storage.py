import shelve

from os import makedirs

from os.path import expanduser
from os.path import join
from os.path import exists

STORAGE_DIR = expanduser('~/.syllabus_bot/')
PERSISTANCE_PATH = join(STORAGE_DIR, 'persistance')

class Storage:
    def folderize(f):
        def wrapper(self, *args, **kwargs):
            if not exists(STORAGE_DIR):
                makedirs(STORAGE_DIR)
            return f(self, *args, **kwargs)
        return wrapper

    @folderize
    def synchronize(f):
        def wrapper(self, *args, **kwargs):
            with shelve.open(PERSISTANCE_PATH) as shelf:
                value = f(self, shelf, *args, **kwargs)
            return value
        return wrapper

    @synchronize
    def get_token(self, shelf):
        return shelf['token']

    @synchronize
    def update_token(self, shelf, key):
        shelf['token'] = key

    @synchronize
    def add_new_user(self, shelf, user_id):
        user = str(user_id)
        if user in shelf:
            return False
        else:
            shelf[user] = ''
            return True
