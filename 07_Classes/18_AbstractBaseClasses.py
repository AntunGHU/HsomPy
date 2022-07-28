# 4'50
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


stream = MemoryStream()

# TypeError: Can't instantiate abstract class Stream with abstract methods read
# stream = Stream()

stream.open()

# Imamo nekoliko isseuesa ovdje!
# mi mozemo svoriti instancu klase Stream ali sto to znaci!?!? Dakle nebi trebali moci ako nema smisla! Trebali bi uvijek subclassed a onda create AN INSTANCE OF SUBLASS. Dakle Stream ce biti base class-a koju cemo koristiti unutar raznih vrsta stream-sa.
# drugi: u oba stream-Class imamo read metod! Ako sutra pozelimo dodati novi stream-Class moramo tocno takav read metod dodati i njemu.
# i tu dolazi apstractbaseclass-koncept! polupeceni kolac namjenjen da omoguci neki zajednicki kod radi stvaranja derivativa!
# To cinimo imortajuci ABC i abstractmethod iz abc klase. Vidi gore!
# kad je klasa postala abstractklass ne mozemo je vise instantirati - komamo stream
# ako pokusamo stvoriti novu StreamClass-u (MemoryStream) to cemo moci tek ako joj obavezno kreiramo read-metod kako nalaze abstract klasa koju nasljedjuje! a tek onda mozemo istu instantirati!
