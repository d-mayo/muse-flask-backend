# import * means import everything from peewee

from peewee import *
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('muse-flask-backend', host='localhost', port=5432)

class Song(Model):
    title = CharField()
    artist = CharField()
    album = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Song], safe=True)
    print("TABLES Created")
    DATABASE.close()