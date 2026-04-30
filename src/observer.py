import weakref

class Publisher:
    def __init__(self):
        # Используем WeakSet вместо обычного set или list
        self._subscribers = weakref.WeakSet()

    def subscribe(self, observer):
        self._subscribers.add(observer)

    def notify(self, data):
        for observer in self._subscribers:
            observer.update(data)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"{self.name} получил: {data}")

    def __del__(self):
        print(f"--- {self.name} был удален из памяти ---")

# Тестируем
pub = Publisher()
sub1 = Subscriber("Подписчик 1")

pub.subscribe(sub1)
pub.notify("Первое событие")

print("Удаляем Подписчика 1...")
del sub1 # Больше сильных ссылок нет

# При следующем уведомлении список будет уже пуст сам по себе
print("Рассылаем второе событие...")
pub.notify("Второе событие")
