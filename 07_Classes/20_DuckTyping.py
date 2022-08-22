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


# uvjet za to je da "(controls)" argument bude iterabilan i da ima draw metod, tj ako se glasa kao patka, ako lici kao patka onda je patka!!! tj ako imaju isti (draw) metod i ako su iterabilni, objekti ce biti prozvakani kroz funkciju draw koja ce i na njima biti polimorfna iako oni nisu potomci abstract-klasa!!!
# Py je dinamical-type of langugage i ne kontrolira type of object, samo gleda da objekt zadovoljava uvjete tj da ima trazeni metod (draw) i da je iterabilan. To ne znaci da ne bi smo rebali nastojati koristiti abc-klase jer njima prinudjavamo izradu subklasa sa unificiranim suceljem tj da svi imaju istu metodu (draw ovdje)!
