# 2'50

# Ovdje zelimo istaci cinjenicu da osnova polimorfmnosti primjera u 19. - klasa "UIControl" nije nuzna za polimorfizam. Ovdje tu klasu brisemo i jos uvjek zadrzavamo polimorfno ponasanje!

from abc import ABC, abstractmethod


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


# uvjet za to je da "(controls)" argument bude iterabilan i da ima draw metod, tj ako se glasa kao patka, ako lici kao patka onda je patka!!!
