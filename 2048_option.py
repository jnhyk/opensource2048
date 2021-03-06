import pygame

PIXEL = 135
SCORE_PIXEL = 185
SIZE = 4

pygame.init()
screen_width = PIXEL * SIZE
screen_height = PIXEL * SIZE + SCORE_PIXEL

screen = pygame.display.set_mode((screen_width, screen_height))#배경
pygame.display.set_caption("2048 OPTION")
background = pygame.image.load("C:/Users/hth09/OneDrive/바탕 화면/desktop/2048/background.png")
screen.blit(background, (0,0))

option_font = pygame.font.Font(None, 100)#상단option글씨
option = option_font.render("OPTION", True, (137, 114, 84))
screen.blit(option, (PIXEL, SCORE_PIXEL // 2))

bgm_emoji = pygame.image.load("C:/Users/hth09/OneDrive/바탕 화면/desktop/2048/sound.png")#왼쪽 배경음 버튼
bgm_button = pygame.Rect(PIXEL , PIXEL * 2 - 50, PIXEL //3 * 2 , PIXEL // 3 * 2)
pygame.draw.rect(screen,(137, 114, 84), bgm_button,45,15)
screen.blit(bgm_emoji, (PIXEL + 10, PIXEL * 2 -40))


sound_emoji = pygame.image.load("C:/Users/hth09/OneDrive/바탕 화면/desktop/2048/sound2.png")#오른쪽 효과음 버튼
sound_button = pygame.Rect(PIXEL + PIXEL // 3 * 4, PIXEL * 2 - 50, PIXEL //3 * 2 , PIXEL // 3 * 2)
pygame.draw.rect(screen,(137, 114, 84), sound_button,45,15)
screen.blit(sound_emoji, (PIXEL + PIXEL // 3 * 4 + 10, PIXEL * 2 - 40))

restart_button = pygame.Rect(PIXEL, PIXEL * (SIZE - 1),PIXEL * 2 , PIXEL // 3 * 2)#restart버튼
pygame.draw.rect(screen,(137, 114, 84), restart_button,45,15)
restart_font = pygame.font.Font(None, 50)
restart = restart_font.render("RESTART", True, (0, 0, 0))
screen.blit(restart, (PIXEL + PIXEL // 3 + 10, PIXEL * (SIZE - 1) + PIXEL // 4))

quit_button = pygame.Rect(PIXEL, PIXEL * SIZE, PIXEL * 2 , PIXEL // 3 * 2)#종료 버튼
pygame.draw.rect(screen,(137, 114, 84), quit_button,45,15)
quit_font = pygame.font.Font(None, 50)
quit = quit_font.render("QUIT", True, (0, 0, 0))
screen.blit(quit, (PIXEL + PIXEL // 3 * 2, PIXEL * SIZE + PIXEL // 4))

running = True
while running:
  click_pos = None

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP:
      click_pos = pygame.mouse.get_pos()

  if click_pos != None:
    if quit_button.collidepoint(click_pos):
      running = False
  
  pygame.display.update()

pygame.quit()
