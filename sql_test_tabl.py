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

from main import conn
from tables import authors, books

spis_avt = ('Pushkin', 'Gogol', 'Welsh', 'Balakirev', 'Oleg')
# список авторов
spisproizv = (('Zoltaya ribka', 1, 'skazki', 500), ('Na Igle', 3, 'triller', 1200), ('Oleg', 5, 'Oleg', 100),
              ('Kapitanskaya Dochka', 1, 'skazki', 1000))
# список произведений


for name_av in spis_avt:
    ins_author_guery = authors.insert().values(name=name_av)
    conn.execute(ins_author_guery)
# добавляем в таблицу строки
for blok in spisproizv:
    ins_books = (books.insert().values(title=blok[0], author_id=blok[1], genre=blok[2], price=blok[3]))
    conn.execute(ins_books)


books_bi_1000 = authors.select()
result = conn.execute(books_bi_1000)
for i in result:
    print(i, end=' ')
print()

books_bi_1000 = books.select()
result = conn.execute(books_bi_1000)
for i in result:
    print(i)
