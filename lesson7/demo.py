# Создать атрибут класса categories
class Categories:
    def __str__(self):
        return f'{self.categories}'
    def __init__(self, categories: list[str]):
        self.categories = categories

    # 3.1 Написать метод класса add принимающий на вход название категории, если такой
    # категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
    # индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
    # исключение ValueError
    def add(self, new_categori: str):
        for item in range(0,len(self.categories)):
            if new_categori not in self.categories:
                self.categories.append(new_categori)
                return f"Категория {new_categori} добавлена и находится по индексу {self.categories.index(new_categori)}"
            else:
                raise ValueError(f"Категория есть по индексу {self.categories.index(new_categori)}")


    # 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
    # категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
    # IndexError
    def get(self, index: int):
        if index in range(0, len(self.categories)):
            return self.categories[index]
        elif index not in range(0, len(self.categories)):
            raise IndexError("Такого индекса не существует")
    # 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
    # удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
    # индексе, ничего не делать, метод ничего возвращать не должен
    def delete(self , index: int):
        if index in range(0,len(self.categories)):
            self.categories.pop(index)

    # 3.4 Написать метод класса update принимающий индекс категорий и новое название
    # категории, если нет элемента на таком индексе, то новая категория должна добавляться с
    # учетом того, что имена категорий уникальны, если новое имя категории нарушает
    # уникальность в списке категорий, вызвать исключение ValueError
    def update(self, index: int , new_categori : str ):
        if index> len(self.categories)-1:
            self.add(new_categori)
            return f"Категория добавлена в конец так как такого индекса нет"
        for item in self.categories:
            if new_categori not in self.categories:
                # self.categories.pop(index)
                self.categories[index] = new_categori
                return f"Категория {new_categori} добавлена и находится по указаному индексу {self.categories.index(new_categori)}"
            else:
                raise ValueError(f"Категория есть ")

moda = Categories(categories=["Hight","Medium","For_ALL"])
print(moda.add("Rich"))
print(moda.get(3))
print(moda.delete(3))
print(moda.update(3,"fun"))
print(moda)
