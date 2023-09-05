import pygame
import sqlite3
import os

# Инициализация PyGame
pygame.init()

# Основные константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Класс для главного персонажа
class Player(pygame.sprite.Sprite)
    def __init__(self)
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Красный квадрат - персонаж
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH  2, SCREEN_HEIGHT  2)
        self.speed = 5
        self.score = 0  # Инициализация счета

    def update(self, keys)
        if keys[pygame.K_LEFT]
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]
            self.rect.x += self.speed
        if keys[pygame.K_UP]
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]
            self.rect.y += self.speed

# Класс для ведения базы данных
class Database
    def __init__(self)
        self.conn = sqlite3.connect(scores.db)  # Подключение к базе данных
        self.cursor = self.conn.cursor()
        self.cursor.execute(CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER))
        self.conn.commit()

    def insert_score(self, name, score)
        self.cursor.execute(INSERT INTO scores VALUES (, ), (name, score))
        self.conn.commit()

    def get_top_scores(self)
        self.cursor.execute(SELECT name, score FROM scores ORDER BY score DESC LIMIT 5)
        return self.cursor.fetchall()

def main()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(My Game)
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    db = Database()

    # Запрос имени пользователя перед началом игры
    user_name = input(Введите ваш никнейм )

    running = True
    while running
        for event in pygame.event.get()
            if event.type == pygame.QUIT
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    # Вставка результата в базу данных и вывод топ-5 игроков
    db.insert_score(user_name, player.score)
    top_scores = db.get_top_scores()
    print(Топ-5 игроков)
    for i, (name, score) in enumerate(top_scores, start=1)
        print(f{i}. {name} {score} очков)

    pygame.quit()

if __name__ == __main__
    main()
