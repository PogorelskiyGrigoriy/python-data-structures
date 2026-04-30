from abc import ABC, abstractmethod
from typing import List

class Node(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Text(Node):
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return self.content

class Group(Node):
    def __init__(self) -> None:
        self.children: List[Node] = []

    def add(self, node: Node) -> None:
        if node is self:
            raise ValueError("Нельзя добавить группу в саму себя")
        self.children.append(node)

    def render(self) -> str:
        return ''.join(child.render() for child in self.children)
    
class Document(Group):
    def __init__(self, title: str):
        super().__init__()
        self.title = title

    def render(self) -> str:
        return f"<h1>{self.title}</h1>{super().render()}"
    
    # Создаем документ
doc = Document("Моя заметка")

# Добавляем обычный текст
doc.add(Text("Это содержание первой заметки."))

print("--- Пример 1 ---")
print(doc.render())
# Вывод: <h1>Моя заметка</h1>Это содержание первой заметки.

# Корень
report = Document("Годовой отчет")

# Раздел 1
intro_group = Group()
intro_group.add(Text("Введение: "))
intro_group.add(Text("В этом году мы достигли многого."))

# Раздел 2 (со списками)
stats_group = Group()
stats_group.add(Text("\nСтатистика: "))

list_items = Group() # Подгруппа внутри группы
list_items.add(Text("- Рост 10%; "))
list_items.add(Text("- Удержание 95%."))

stats_group.add(list_items)

# Собираем всё в документ
report.add(intro_group)
report.add(stats_group)

print("\n--- Пример 2 (Вложенность) ---")
print(report.render())

def print_node(node: Node):
    """Этой функции плевать на тип узла, она просто просит его отрисоваться."""
    print(f"Отрисовка узла: {node.render()}")

simple_text = Text("Я просто строка")
big_group = Group()
big_group.add(Text("Я "))
big_group.add(Text("часть "))
big_group.add(Text("группы"))

print("\n--- Пример 3 (Единообразие) ---")
print_node(simple_text)
print_node(big_group)