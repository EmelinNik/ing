import pygame
from player import Player
from database import Database

# Основные константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)  # Передаем SCREEN_WIDTH и SCREEN_HEIGHT
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    db = Database()

    user_name = input("Введите ваш никнейм: ")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    db.insert_score(user_name, player.score)
    top_scores = db.get_top_scores()
    print("Топ-5 игроков:")
    for i, (name, score) in enumerate(top_scores, start=1):
        print(f"{i}. {name}: {score} очков")

    pygame.quit()

if __name__ == "__main__":
    main()
