# 9'10

# SQLite je light-db i izbor malih app-sova kao npr za phones i tablets

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)
# [{'id': 1, 'title': 'Terminator', 'year': 1989}, {'id': 2, 'title': 'Kindergarten Cop', 'year': 1993}]
# sad zelimo ovu listu spremiti u sqlite3 db

# Tloc nije ovako i mislim da je ovo ok i bolje!
# ? with sqlite3.connect("db.sqlite3") as conn:
# ?     command = "INSERT INTO Movies VALUES(?, ?, ?)"
# ?     for movie in movies:
# ?         conn.execute(command, tuple(movie.values()))
# ?     conn.commit()
# sqlite3.OperationalError: no such table: Movies
# Gornji kod daje gresku nepostojanja tablice pa nas Ath vodi u browser pretragu za "db browser for sqlite" i stranicu https://sqlitebrowser.org sa koje trebamo dld-ati executable za nas OS. (stvar koju vec posjedujem na lx-u!!) i aktivirati i pokazati da nema nikakve tablice u stvorenom fajlu db.sqlite.
# Kreiramo tablicu kroz ovaj externi program
# Potom ponovo pokrecemo kod i ovaj put nema greske
# Ponovo u db browser app i vidimo da je kod upisao filmove!

# Kako citati podatke i db-ia
# Sve je skoro isto osim SQL-dijela i dodavanja cursora, commit je takodjer visak jer ga trebamo samo za pisanje u db (probao sa nekomentiranim dijelom za pisanje pa greska!)
# ? with sqlite3.connect("db.sqlite3") as conn:
# ?     command = "SELECT * FROM Movies"
# ?     cursor = conn.execute(command)
# ?     for row in cursor:
# ?         print(row)

# (1, 'Terminator', 1989)
# (2, 'Kindergarten Cop', 1993)

# ako hocemo imamo mogucnost i primjene metoda fetchall uz prehodno komanje loop-a

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # ? for row in cursor:
    # ?     print(row)
    movies = cursor.fetchall()
    print(movies)
    # [(1, 'Terminator', 1989), (2, 'Kindergarten Cop', 1993)]
