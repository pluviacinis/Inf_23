#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
        if (self.width * self.height) >= 0:
            return(self.width * self.height / 2)
        else:
            return(0)
    
class Rectangle(Shape):
    def area(self):
        if (self.width * self.height) >= 0:
            return(self.width * self.height)
        else:
            return(0)
x = Rectangle(5, 10)
y = Triangle(25, 100)
print(x.area())
print(y.area())


# In[1]:


class Mother:
    def __init__(self):
        pass
    def __str__(self):
        return ("Mother")
class Daughter(Mother):
    def __init__(self):
        self.value = 'abc'
    def __str__(self):
        return ("Daughter")
x = Mother()
y = Daughter()
print(x)
print(y)


# In[10]:


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animal):
    def __str__(self):
        return(str(self.name)+", Zebra, "+str(self.age)+' years old')
    
class Dolphin(Animal):
    def __str__(self):
        return(str(self.name)+", Dolphin, "+str(self.age)+' years old')

a = Dolphin('Alex', 8)
j = Zebra('Joe', 11)
print(a)
print(j)


# In[ ]:


1) В чем разница между объектом class и объектом instance? 
2) Что означает аргумент self в методах класса? 
3) Как указать superclass для данного class? 
get_ipython().set_next_input('4) Зачем используется перегрузка операторов');get_ipython().run_line_magic('pinfo', 'операторов')

Объект class содержит общее описание методов(функций) и атрибутов(значений) объектов, которые в нем содержаться. 
Объект instance - это элемент класса, имеющий конкретные значения атрибутов, к котором можно обратиться с каким-либо из методов.

Аргумент self означает обращение элемента класса к самому себе. В частности, таким образом значения атрибутов присваиваются к конкретному объекту.

При объявлении класса можно указать родительский класс в скобках, тогда будет реализовано наследование методов и атрибутов из родительского надкласса. Их можно дополнить, объявив новые, или переопределить, объявив заново с тем же названием.

Перегрузка оператора может быть использована для переопределения/доопределения какого-либо встроенного оператора по отношению к классу. Например, оператор '+', '/' и тд. В частности, можно дополнить какой-либо встроенный класс.

