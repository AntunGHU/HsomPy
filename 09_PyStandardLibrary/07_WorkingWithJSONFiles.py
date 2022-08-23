# 3'57
from pathlib import Path
import json

# ? movies = [
# ?     {"id": 1, "title": "Terminator", "year": 1989},
# ?     {"id": 2, "title": "Kindergarten Cop", "year": 1993}
# ? ]

# ? data = json.dumps(movies)
# ? print(data)
# ? [{"id": 1, "title": "Terminator", "year": 1989}, {"id": 2, "title": "Kindergarten Cop", "year": 1993}]

# ? Path("movies.json").write_text(data)
# kao rezultat pojavio nam se file "movies.json" u project-folderu!

# recimo sad da smo dobili odnekud .json file, kako ga procitati i spremiti u varijablu
data = Path("movies.json").read_text()
# potom je transformamo u json objekt kojeg zovemo movies
movies = json.loads(data)
# printamo ga
print(movies)   # [{'id': 1, 'title': 'Terminator', 'year': 1989}, {'id': 2, 'title': 'Kindergarten Cop', 'year': 1993}]

# podaci lice na one koje smo unijeli ali sada su zaista lista i mi mozemo selektirati npr citav ili naziv
print(movies[0])    # {'id': 1, 'title': 'Terminator', 'year': 1989}
print(movies[0]["title"])   # Terminator
