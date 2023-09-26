import pygame
import pandas as pd
import time
velocity = int(input())
v0 = velocity
step = v0

data = {
    'Reaction Distance' : [],
}
next = 0
df = pd.DataFrame(data)
# 스크린 전체 크기 지정

SCREEN_WIDTH = 2400
SCREEN_HEIGHT  = 1000 

# pygame 초기화

pygame.init()

 

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dual Task")

 

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

 

# 이미지 로딩 및 크기 변경

player = pygame.image.load("Player.png")
player = pygame.transform.scale(player, (80, 40))

tunnel = pygame.image.load("Tunnel.png")
tunnel = pygame.transform.scale(tunnel, (400, 60))

# tunnel = pygame.image.load("Tunnel2.png")
# tunnel = pygame.transform.scale(tunnel, (400, 60))
            
point = pygame.image.load("point.png")
point = pygame.transform.scale(point, (20,60))

text = pygame.image.load("text.png")
text = pygame.transform.scale(text, (900, 150))

# 이미지의 Rect 정보를 저장

player_Rect = player.get_rect()
tunnel_Rect = tunnel.get_rect()
point_Rect = point.get_rect()
text_Rect = text.get_rect()


# 이미지가 가운데 올 수 있도록 좌표값 수정

# python 3.8 이상에서 integer가 필요한 곳에 float가 들어가면 DeprecationWarning이 나옴.

# 따라서 round() 처리를 해준다.

player_Rect.centerx = round(SCREEN_WIDTH)

player_Rect.centery = round(SCREEN_HEIGHT / 2)

tunnel_Rect.centerx = round(400)

tunnel_Rect.centery = round(SCREEN_HEIGHT / 2) 

point_Rect.centerx = round(200)

point_Rect.centery = round(SCREEN_HEIGHT / 2 - 80) 

text_Rect.centerx = round(SCREEN_WIDTH / 2)

text_Rect.centery = round(100) 

paused = False

def pause():                # 일시정지 기능 만들기
    global paused
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:         #마우스 버튼 클릭시 다시 시작
                    tunnel = pygame.image.load("Tunnel2.png")
                    tunnel = pygame.transform.scale(tunnel, (400, 60))
                    SCREEN.fill((255, 255, 255))
                    SCREEN.blit(player, player_Rect)
                    SCREEN.blit(tunnel, tunnel_Rect)
                    SCREEN.blit(point, point_Rect)
                    SCREEN.blit(distance, (100, 100))
                    SCREEN.blit(text, text_Rect)
                    pygame.display.flip()
                    time.sleep(0.5)
                    paused = False


playing = True
decrease = False
while playing:
    if decrease and velocity >0:
        velocity -= step
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            df.to_csv("result", sep='\t', encoding="utf-8")
            pygame.quit()
            
        elif velocity <= 0:
                re_time = abs(200 - player_Rect.x)
                print(re_time)
                df.loc[next] = re_time
                next = next + 1
                font = pygame.font.SysFont("arial", 30, True, True)
                distance = font.render(f"Distance : {re_time}", True, (0,0,0), (0, 255, 0))
                SCREEN.blit(distance, (100, 100))
                pygame.display.flip()
                pause()
                velocity = v0
                decrease = False
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER:  # 엔터 키를 땠을때
                decrease = False
        elif event.type == pygame.KEYDOWN:
            # breakpoint()
            if event.key == pygame.K_KP_ENTER:  # 엔터 키를 눌렀을 때
                decrease = True
            
            elif event.key == pygame.K_UP:
                step = v0/30
                tunnel = pygame.image.load("Tunnel2.png")
                tunnel = pygame.transform.scale(tunnel, (400, 60))
                SCREEN.blit(tunnel, tunnel_Rect)
                pygame.display.flip()

            elif event.key == pygame.K_DOWN:
                step = v0
                # breakpoint()
                tunnel = pygame.image.load("Tunnel.png")
                tunnel = pygame.transform.scale(tunnel, (400, 60))
                SCREEN.blit(tunnel, tunnel_Rect)
                pygame.display.flip()
            # elif event.key == pygame.K_RIGHT:
            #     breakpoint()
    # 스크린 배경색 칠하기

    SCREEN.fill((255, 255, 255))

    

    # 이미지의 x 좌표값을 5씩 증가

    player_Rect.x -= velocity

    # 이미지가 화면을 벗어나면 다시 초기위치로 움직임
    
    if player_Rect.x < 0:
        player_Rect.x = SCREEN_WIDTH

    # 또는

    # player_Rect.bottom = 0

    # 스크린의 원하는 좌표에 이미지 복사하기, 좌표값은 Rect를 이용

    SCREEN.blit(player, player_Rect)
    SCREEN.blit(tunnel, tunnel_Rect)
    SCREEN.blit(point, point_Rect)
    SCREEN.blit(text, text_Rect)

 

    # 작업한 스크린의 내용을 갱신하기

    pygame.display.flip()

 

    # 1초에 60번의 빈도로 순환하기

    clock.tick(60)