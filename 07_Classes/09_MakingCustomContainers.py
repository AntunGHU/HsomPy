# 6'55

# ponekad zelimo stvoriti svoje "custom" container-tipove podataka

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)   # {'python': 3}

cloud.add("Python")
cloud.add("python")
print(cloud["python"])  # 5
cloud.add("python")
cloud["python"] = 10
print(cloud["python"])  # 10
print(cloud.tags)   # {'python': 5, 'Python': 1} a poslije {'python': 6}
print(len(cloud))   # 1

for k in cloud:
    print(k)

# tipicni dict se ponasa ovako tj  casesensitive. No, smisao pravljenja custom klase je da je ucini pametnijom od standarne tj da na to ne obraca paznju. To Ath cini dalje tako da ubacuje u definiciju customa metod "lower()". I sad nema posebnog unosa za veliko-malo, sve je isto
