import pygame
import os
# 스크린 전체 크기 지정

SCREEN_WIDTH = 1200
SCREEN_HEIGHT  = 500 

# pygame 초기화

pygame.init()

 

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("인간공학 실험_Dual Task")

 

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

 

# 이미지 로딩 및 크기 변경

player = pygame.image.load("Player.png")
player = pygame.transform.scale(player, (80, 40))

tunnel = pygame.image.load("Tunnel.png")
tunnel = pygame.transform.scale(tunnel, (400, 60))
 

# 이미지의 Rect 정보를 저장

player_Rect = player.get_rect()
tunnel_Rect = tunnel.get_rect()
 

# 이미지가 가운데 올 수 있도록 좌표값 수정

# python 3.8 이상에서 integer가 필요한 곳에 float가 들어가면 DeprecationWarning이 나옴.

# 따라서 round() 처리를 해준다.

player_Rect.centerx = round(SCREEN_WIDTH)

player_Rect.centery = round(SCREEN_HEIGHT / 2)

tunnel_Rect.centerx = round(400)

tunnel_Rect.centery = round(SCREEN_HEIGHT / 2) 

def pause():                # 일시정지 기능 만들기

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.K_KP_ENTER:
                paused = True
            if event.type == pygame.MOUSEBUTTONDOWN:         #마우스 버튼 클릭시 다시 시작
                paused = False

playing = True
while playing:

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("enter")
            pause()
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

 

    # 스크린 배경색 칠하기

    SCREEN.fill((255, 255, 255))

    

    # 이미지의 x 좌표값을 5씩 증가

    player_Rect.x -= 5

    # 이미지가 화면을 벗어나면 다시 초기위치로 움직임
    
    if player_Rect.x < 0:
        player_Rect.x = 1200

    # 또는

    # player_Rect.bottom = 0

    # 스크린의 원하는 좌표에 이미지 복사하기, 좌표값은 Rect를 이용

    SCREEN.blit(player, player_Rect)
    SCREEN.blit(tunnel, tunnel_Rect)

 

    # 작업한 스크린의 내용을 갱신하기

    pygame.display.flip()

 

    # 1초에 60번의 빈도로 순환하기

    clock.tick(60)