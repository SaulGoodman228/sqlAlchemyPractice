from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
)

from sqlalchemy.sql import select,and_

# субб+драйвер://юзер:пароль"хост:порт/база
engine=create_engine('sqlite+pysqlite:///:memory:')
meta=MetaData()
conn = engine.connect()



# git init - инициализирует локальный репозиторий
# git remote add origin https://github.com/SaulGoodman228/sqlAlchemyPractice.git - привязывает локальный репозиторий к облачному
# --------
#
# git add -A - смотрит есть ли изменения
# git commit -m"tables created" - сохраняеь т изменения в коде ЛОКАЛЬНО
# git push origin master - отправит все изменения в облако (на github)
