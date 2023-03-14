class Task1:

    def __init__(self, french, pianists, swimmers):
        self.french = french
        self.pianists = pianists
        self.swimmers = swimmers

    def special_students(self):
        """swimmers-pianists not learning French"""
        return (set((self.swimmers.intersection(self.pianists)).difference(self.french)))


class Task2:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def get_unique_list_1(self):
        """return unique elements of the first list"""
        s1 = set(self.list_1)
        return (len(s1))

    def get_unique_both_lists(self):
        """return unique elements of the both lists"""
        s3 = set(self.list_1+self.list_2)
        return (len(s3))


class Task3:

    def __init__(self, films):
        self.films = films

    def get_results(self):
        """return dict with counts"""
        top = dict()
        for film in films:
            if top.get(film) == None:
                top[film] = 1
            else:
                top[film] += 1
        return (sorted(top.items(), key=lambda item: item[1], reverse = True))


class Task4:

    def __init__(self, text):
        self.text = text

    def word_counter(self):
        """word counter dict in descending order"""
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.lower()
        LoW = text.split()
        ToF = {}
        for word in LoW:
            if ToF.get(word) == None:
                ToF[word] = 1
            else:
                ToF[word] += 1
                
        return (sorted(ToF.items(), key=lambda item: item[1], reverse = True)


class Task5:

    def __init__(self, family):
        self.family = family

    def parents(self, name):
        """ returns list of parents """
        return (self.family[name])

    def grandparents(self, name):
        """ returns list of grandmothers and grandfathers """
        grand = []
        for person in self.parents(name):
            grand.append((self.parents(person)))
        return (grand)

    def siblings(self, name):
        siblings = []
        for person in self.family:
            if self.parents(person) == self.parents(name) and person != name:
                siblings.append(person)
        return siblings

    
    def children(self, name):
        children = []
        for person in self.family:
            if name in self.parents(person):
                children.append(person)
        return children


    def grandchildren(self, name):
        grandchildren = []
        children = self.children(name)
        for person in children:
            grandchildren.extend(self.children(person))
        return grandchildren
