from sqlalchemy import (
    create_engine,
    select,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey
)

from main import meta, engine

authors = Table('Authors', meta,
                Column('id_author', Integer, primary_key=True),
                Column('name', String(250), nullable=False))

# столбец в которм указан primary_key является главным

books = Table('Books', meta,
              Column('id_book', Integer, primary_key=True),
              Column('title', String(250), nullable=False),
              Column('author_id', Integer, ForeignKey('Authors.id_author')),
              Column('genre', String(250)),
              Column('price', Integer))
# тут мы записываем данные в нашу мету
meta.create_all(engine)