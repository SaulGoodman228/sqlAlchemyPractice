from sqlalchemy import Table, Column, Integer, create_engine, MetaData, String

engine=create_engine('sqlite+pysqlite:///:memory:',echo=True)
meta=MetaData()

user_table=Table("users",meta,
                 Column('id',Integer,primary_key=True),
                 Column('name',String(30))

)
PEQPQPEPQEPEPPQPEQ{ELKLWKGJ
                   slfkngldkfng


df;gkldkfjglkjdflgkjd
d;fkgjldkfjgl}
# git init - инициализирует локальный репозиторий
# git remote add origin https://github.com/SaulGoodman228/sqlAlchemyPractice.git - привязывает локальный репозиторий к облачному
# --------
#
# git add -A - смотрит есть ли изменения
# git commit -m"tables created" - сохраняеь т изменения в коде ЛОКАЛЬНО
# git push origin master - отправит все изменения в облако (на github)
