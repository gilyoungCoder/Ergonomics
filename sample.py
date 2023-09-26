import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((400, 300))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 엔터 키를 눌렀을 때
                print("엔터 키가 눌렸습니다.")

# Pygame 종료
pygame.quit()
sys.exit()
