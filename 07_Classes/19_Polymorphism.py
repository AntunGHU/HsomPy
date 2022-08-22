# 3'56

from abc import ABC, abstractmethod

  
class UIControl(ABC): # abstractClassa samo propisuje sto bi njeni derivati trebali sljediti
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# ? def draw(control):
# ?     control.draw()


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
# ? print(isinstance(ddl, UIControl))  # True
# ? draw(ddl)       # DropDownList
# ? draw(textbox)       # TextBox

draw([ddl, textbox])  # DropDownList; TextBox

# dakle propisujuci sa osnovnom klasom "UIControl" ponasanje derivata mi smo dobili da se funkcija draw ponasa polimorfno!
