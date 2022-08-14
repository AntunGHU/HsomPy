# 3'40

# Hoce pokazati znacaj __dundera ili mangeling dunder-a. Sve skupa pada na ispitu namjeravane kratkoce i jednostavnosti. Da sam od njega poceo, odmah bi odustao od svega!
# pokazao i primjenio F2 tj renaming na tags u __tags


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
print(cloud.__dict__)   # {'_TagCloud__tags': {}} # name-mangeling
