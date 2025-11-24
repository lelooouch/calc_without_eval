import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# cur.executescript('''
# DROP TABLE video_products2;
# ''')

# cur.executescript('''
# CREATE TABLE IF NOT EXISTS product_types(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL
# );
# CREATE TABLE IF NOT EXISTS video_products2(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     type_id INTEGER NOT NULL,
#     FOREIGN KEY(type_id) REFERENCES product_types(id)
# );
# ''')

video_products = [
    (1, 'Безумные мелодии Луни Тюнз', 2),
    (2, 'Веселые мелодии', 2),
    (3, 'Кто подставил кролика Роджера', 3),
    (4, 'Хороший, плохой, злой', 3),
    (5, 'Последний киногерой', 3),
    (6, 'Она написала убийство', 4),
    (7, 'Миссис Харрис едет в Париж', 3),
]

product_types = [
    (1, 'Мультфильм'),
    (2, 'Мультсериал'),
    (3, 'Фильм'),
    (4, 'Сериал'),
]

# cur.executemany('INSERT INTO product_types VALUES(?, ?);', product_types)
# cur.executemany('INSERT INTO video_products2 VALUES(?, ?, ?);', video_products)

# results = cur.execute('''
# SELECT video_products2.name, product_types.name 
# FROM video_products2, product_types
# WHERE video_products2.type_id = product_types.id AND product_types.name = "Фильм";
# ''') 

# for result in results:
#     print(result)

cur.executescript('''
ALTER TABLE video_products2
RENAME TO video_products;
''')

con.commit()
con.close()

# cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
# cur.executemany('INSERT INTO video_products VALUES(?, ?, ?, ?);', video_products)

results = cur.execute('''
SELECT title,
release_year
FROM video_products
WHERE (release_year BETWEEN 1965 AND 2025) AND product_type LIKE '%ильм'
''')

for result in results:
    print(result)

con.commit()
con.close()
