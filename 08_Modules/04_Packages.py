# 2'27

# Kako projekt raste tako i broj fajlova raste te ih uobicajenom praksom  organiziramo u subdirse.
# Ath pravi dir "ecommerce" i seli sales.py u njega
# sada linija import pocrveni jer py ne moze naci modul sales.

# ? import sales

# popravak promlema ide kroz kreiranje fajla "__init__.py"  u mapi "ecommerce" sto ce pretvoriti mapu u package
# potom nas import upotpunimo

from ecommerce import sales
from ecommerce.sales import calculate_shipping
import ecommerce.sales

# pozivanje se takodjer mora upotpuniti i postaje

ecommerce.sales.calculate_shipping()

# ako nam je to naporno svaki put pisati onda koristimo "from ecommerce.sales import calculate_shipping" (sa zarezom ako imamo vise)

# nakon cega pozivamo funkciju kao i lokalnu

calculate_shipping()

# ako nam je "from..." predugacak sa svim mogucim zarezima tada samo importamo sales "from ecommerce import sales" ali tada pozivanje ide sa sales

sales.calculate_shipping()
