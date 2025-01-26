from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.types = self.get_types()
        self.weightheight = self.get_weight_height()
        self.level = self.get_level()
        self.hp = randint(1,100)
        self.power = randint(1,100)
        Pokemon.pokemons[pokemon_trainer] = self
    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        return None
    
    def get_types(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [t['type']['name'] for t in data['types']]
        return ['unknown']
    # Метод класса для получения информации

    def get_weight_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['height'], data['weight']
        return None, None

    def get_level(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['base_experience']
        return None
    def info(self):
        return f"Имя твоего покеомона: {self.name}, его тип: {', '.join(self.types)}, вес: {self.weightheight[1]}, высота: {self.weightheight[0]}, уровень: {self.get_level()}, hp: {self.hp}, power: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


class Wizard(Pokemon):
    """Подкласс Pokemon, представляющий покемона-волшебника."""

    def info(self):
        """Возвращает информацию о покемоне-волшебнике."""
        return "У тебя покемон-волшебник \n\n" + super().info()

class Fighter(Pokemon):
    """Подкласс Pokemon, представляющий покемона-бойца."""

    def attack(self, enemy):
        """Атака с использованием супер-удара."""
        super_power = randint(5, 15)  # Генерируем дополнительную силу атаки
        self.power += super_power  # Увеличиваем силу атаки перед ударом
        result = super().attack(enemy)  # Вызываем стандартную атаку
        self.power -= super_power  # Возвращаем силу атаки к изначальному значению
        return result + f"\nБоец применил супер-атаку силой: {super_power} "

    def info(self):
        """Возвращает информацию о покемоне-бойце."""
        return "У тебя покемон-боец \n\n" + super().info()

# Создаём двух покемонов: волшебника и бойца
wizard = Wizard("username1")
fighter = Fighter("username2")

# Выводим информацию о покемонах
print(wizard.info())
print("#" * 10)
print(fighter.info())
print("#" * 10)

# Проводим сражение между покемонами
print(wizard.attack(fighter))
print(fighter.attack(wizard))
