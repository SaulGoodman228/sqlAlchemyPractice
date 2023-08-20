from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
)

from sqlalchemy.sql import select,and_


engine=create_engine('sqlite+pysqlite:///:memory:')
meta=MetaData(engine)  #нихуя не понял поч не раотает но мне надо загрузить прошлые данные
#создаем мету с уже записанной ранее базой данных

authors=Table('Authors',meta,autoload=True)
books=Table('Books',meta,autoload=True)

