# 1'01

# recimo da je nasa podmapa "ecommerce" narasla i ima puno fajlova-paketa pa je odlucimo urediti dodavanjem njenih subdir-ova, npr "shoping" i muvamo sales.py u nj.
# postupamo isto: unutar mape "shoping" pravimo fajl "__init__.py"
# prica se ponavlja: py ponovo ne moze naci sales pa u pozivanja moramo uvrstiti sada i mapu shoping
from ecommerce.shoping import sales
