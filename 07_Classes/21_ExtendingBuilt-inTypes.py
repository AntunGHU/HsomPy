# 2'26

# u Py inheritance mozemo raditi sa built-in types klasama!

# nasljedjuje sve od "str" klase ali onda joj jos mozemo stosta svoga dodati!, npr dupliciranje!
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
# i sad kad potrazujemo metode duplicate se pojavljuje!!
print(text.duplicate())  # PythonPython


# sad primjer prosirenja append-metoda (ala Tloc)
class TrackableList(list):
    def append(self, object):
        print("Append called!")     # prosirenje!
        super().append(object)      # zvanje standardnih osobina appenda!


list = TrackableList()
list.append("1")        # Append called!
