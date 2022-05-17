import random
import pygame


def display_start_screen():
  pygame.display.set_caption("2048 START")
  global start_button
  background = pygame.image.load("start_screen.jpg")
  screen.blit(background, (0,0))
  start_button = pygame.Rect(146, 549, 250 , 100)#종료 버튼

def display_game_screen():
  pygame.display.set_caption("2048")
  global option_button
  global undo_button
  global score_button
  background = pygame.image.load("main.jpg")
  block_c = pygame.image.load("block_c.png")
  screen.blit(background, (0,0))
  option_button = pygame.Rect(460, 130, 50 , 50)
  undo_button = pygame.Rect(367, 128, 54, 54)
  score_button = pygame.Rect(355, 74, 53, 29) 

  for i in range(0,4):
    y = 211 + 118 * i
    for j in range(0,4):
      x = 37 + 119 * j
      block[i].append((x,y))
    block.append([])

  screen.blit(block_c, block[loc1_x][loc1_y])
  screen.blit(block_c, block[loc2_x][loc2_y])

  


def display_rank_screen():
  global rank_quit_button
  pygame.display.set_caption("2048 RANKING")
  background = pygame.image.load("Ranking.png")
  screen.blit(background, (0,0))
  rank_quit_button = pygame.Rect(387, 660, 132, 42)

def display_option_screen():
  pygame.display.set_caption("2048 OPTION")
  global option_quit_button
  global bgm_button
  global sound_button
  global restart_button
  background = pygame.image.load("option.png")
  screen.blit(background, (0,0))

  bgm_button = pygame.Rect(130,216,94,94)
  sound_button = pygame.Rect(316, 410, 94, 94)
  restart_button = pygame.Rect(130, 404, 280, 93)#restart버튼
  option_quit_button = pygame.Rect(130, 541, 280, 93)#종료 버튼

pygame.init()
block = []
block.append([])
loc1_x = random.randrange(0,4)
loc1_y = random.randrange(0,4)
loc2_x = random.randrange(0,4)
loc2_y = random.randrange(0,4)
while loc1_x != loc2_x and loc1_y != loc2_y:
  loc2_x = random.randrange(0,4)
  loc2_y = random.randrange(0,4)
screen_width = 540
screen_height = 725

screen = pygame.display.set_mode((screen_width, screen_height))#배경

start = False
running = True
option = False
rank = False
while running:
  click_pos = None

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP:
      click_pos = pygame.mouse.get_pos()
      print(click_pos)

  if click_pos:
    if start_button.collidepoint(click_pos):
      start = True
  
  if start:
    if option:
      display_option_screen()

      if click_pos:
        if option_quit_button.collidepoint(click_pos):
          option = False

    elif rank:
        display_rank_screen()

        if click_pos:
          if rank_quit_button.collidepoint(click_pos):
            rank = False

    else:
      display_game_screen()

    
      if click_pos:
          if option_button.collidepoint(click_pos):
            option = True
          elif score_button.collidepoint(click_pos):
            rank = True

  else:
    display_start_screen()

  
  pygame.display.update()

pygame.quit()
