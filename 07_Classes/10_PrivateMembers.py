# 3'40

# Hoce pokazati znacaj __dundera ili mangeling dunder-a.
# pokazao i renaming na tags u __tags kao nacin da se useru kaze "Hey, don't touch this!" Colt je tu ulogu dao jednostrukom _tags!?


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)   # {'_TagCloud__tags': {}}     # moja klasa ima samo 1 atrib: __tags i vrijednost mu je {}
# __dict__ je metod dobavljac svih atributa neke klase!!
print(cloud._TagCloud__tags)    # {}
# py za razliku od C# ili Java, nema koncept private-members i sve je dohvatljivo a __ je pokusaj sprecavanja slucajnog pristupa!