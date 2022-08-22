# 7'30

# ? class Product:
# ?     def __init__(self, price):
# ?         self.price = price

# Ath zeli skrenuti paznju da sa ovim standardnim nacinom definiranja atributa mozemo mi kao i neko drugi vrijednosti naseg atributa postaviti na minus! Ali kako to sprijeciti?


# ? product = Product(-50)

# jedno od rijesenja je da se atribut dodavanjem double-single (mangeln) dundera ucini privatnim i dodaju geter i setter a u constructoru (initu) umjesto direktnog proklamiranja atributa stavimo ga preko setera!


# ? class Product:
# ?     def __init__(self, price):
# ?         self.set_price(price)           # ?

# ?     def get_price(self):
# ?         return self.__price             # ?

# ?     def set_price(self, value):
# ?         if value < 0:
# ?             raise ValueError("Price cannot be negative!")
# ?         self.__price = value            # ?

# ?     price = property(get_price, set_price)


# ? product = Product(-50)  # ValueError: Price cannot be negative!

# ali ovaj nacin je unpythonic
# pythonic nacin bi bio to use property (vidi gore) poslije kojeg sa ala property-nacinom ocitavamo ali i postavljamo vrijednost. Ako negativna --> raise..
# postaje mi jasno da attribut i property nije isto!!! Atribut je ono sto sam do sada oznacavao s propsi!

# "Property is an object that sits in front of an attribut and allows us to get and set a value of an attribute. Mosh"
#-----1.Definiramo cls-attribut sa idealnim imenom - gore "price"
#-----2.pozivamo builtin func property koja uzima 4 parametra koji su svi opcijski (prvi je fun za geting, drugi fun za seting, treci fun za delanje a cetvrti za  documentation)
#-----3.Mi cemo postaviti prva dva koja smo vec definirali: get_price i set_price. !!! Mi ne zovemo metod property, samo se referenciramo na nj! a kad ga budemo pozvali(u sklopu atributiranja) on ce nam vratiti property-objekt koji ce koristiti funkcije get_price i set_price za getanje i setanje
# ? product = Product(100)
# ? product.price = -1  # ValueError: Price cannot be negative!
# ? print(product.price)    # 100

# iako su metodi geter i setter "rjesili" problem, ipak oni oneciscuju interface naseg objekata jer se pojavljuju kao opcije poslije tocke. Malo sredjivanje toga bilo bi da se getter i setter privatiziraju u __get_price itd. Medjutim bolji nacin je da se koriste "decoratori" (ono sto mi je Tloc ostao duzan!) i pretvaranje instance-metoda u class-metod sa "@property". Vidi verzija dole!


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value


# ? product = Product(-100)
# ? print(product.price)    # ValueError: Price cannot be negative!

product = Product(100)
print(product.price)  # 100

# za kraj napomena da ne moramo uvjek imati i getter i setter. Npr, ako u gornjem kodu komamo setter imat cemo samo readonly class ali ce raditi! Hmm
