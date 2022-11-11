import pygame


#screen
screenHeight = 1000
screenWidth = 1000

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ocarina of Time Randomizer Tracker - Ven519")

#lists for map tracker
abs_required_items=["bow_1", "light_arrows", "magic_1", "master_sword"]
song_locations=["zl", "eponas", "sarias", "suns", "time", "storms", "minuet", "preulde", "bolero", "serenade", "requiem", "nocturne"]
dungeon_rewards = ["deku", "dc", "jabu", "forest", "fire", "water", "spirit", "shadow", "free"]
dungeon_locations = ["deku", "dc", "jabu", "forest", "fire", "water", "spirit", "shadow", "well", "gtg", "ice"]
vanilla_dungeon_keys = [0, 0, 0, 5, 8, 6, 9, "???", 3, 9, 0]
master_quest_keys = [0, 0, 0, 6, 5, 6, 9, "???", 3, 9, 0]

#image loading
  #background (not yet)
OoT_bg = pygame.image.load("assets/images/OoT/bg/OoT_bg.png").convert_alpha()
item_bg = pygame.image.load("assets/images/OoT/bg/items.png").convert_alpha()
  #default item loading
default_hookshot = pygame.image.load("assets/images/OoT/items/hookshot/hookshot_0.png").convert_alpha()
default_bow = pygame.image.load("assets/images/OoT/items/bow/no.png").convert_alpha()
  
  #obtained item loading
hookshot = pygame.image.load("assets/images/OoT/items/hookshot/hookshot.png").convert_alpha()
longshot = pygame.image.load("assets/images/OoT/items/hookshot/longshot.png").convert_alpha()

  #dungeon reward loading - medallions
default_light = pygame.image.load("assets/images/OoT/medallions/light_gray.png").convert_alpha()
clicked_light = pygame.image.load("assets/images/Oot/medallions/light.png").convert_alpha()

default_forest = pygame.image.load("assets/images/OoT/medallions/forest_gray.png").convert_alpha()
clicked_forest = pygame.image.load("assets/images/OoT/medallions/forest.png").convert_alpha()

default_fire = pygame.image.load("assets/images/OoT/medallions/fire_gray.png").convert_alpha()
clicked_fire = pygame.image.load("assets/images/OoT/medallions/fire.png").convert_alpha()

default_water = pygame.image.load("assets/images/OoT/medallions/water_gray.png").convert_alpha()
clicked_water = pygame.image.load("assets/images/OoT/medallions/water.png").convert_alpha()

default_spirit = pygame.image.load("assets/images/OoT/medallions/spirit_gray.png").convert_alpha()
clicked_spirit = pygame.image.load("assets/images/OoT/medallions/spirit.png").convert_alpha()

default_shadow = pygame.image.load("assets/images/OoT/medallions/shadow_gray.png").convert_alpha()
clicked_shadow = pygame.image.load("assets/images/OoT/medallions/shadow.png").convert_alpha()


#classes for defining image, scale, and location
class imageScaling():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
     screen.blit(self.image, (self.rect.x, self.rect.y))
start = True
run = True
OoT_bg = imageScaling(0, 0, OoT_bg, 4)
item_bg = imageScaling(0, 0, item_bg, 0.75)

#item scaling - default items
default_hookshot = imageScaling(100, 100, default_hookshot, 0.2)
default_bow = imageScaling(240, 0, default_bow, 0.2)
#item scaling - clicked forms
hookshot = imageScaling(100, 100, hookshot, 0.2)
longshot = imageScaling(100, 100, longshot, 0.2)


#variables - drawing items (item states for progressive items)
hookshotState = 0
bottleState = 0
bombState = 0
slingshotState = 0
stickState = 0
nutState = 0
shieldState = 0 #needs to allow both left and right click events to change image
bowState = 0
tunicState = 0 #needs to allow both goron and zora tunic to be displayed
bootState = 0 #needs to allow both iron and hover

#dungeons and skulltula
forest_keyState = 0
fire_keyState = 0
water_keyState = 0
spirit_keyState = 0
shadow_keyState = 0
gtg_keyState = 0
botw_keyState = 0
skulltulaState = 0

#support for dungeon entrance rando
forest_entranceState = 0
fire_entranceState = 0
water_entranceState = 0
spirit_entranceState = 0
shadow_entranceState = 0
gtg_entranceState = 0
botw_entranceState = 0
ice_entranceState = 0

#dungeon reward states
deku_rewardState = 0
dc_rewardState = 0
jabu_rewardState = 0
forest_rewardState = 0
fire_rewardState = 0
water_rewardState = 0
spirit_rewardState = 0
shadow_rewardState = 0
light_rewardState = 0


#rectangles, the bane of my existence
hookshot_rect = pygame.Rect(100, 100, 50, 50) #50, 50 is the absolute rect size for hook
while run == True:
  while start == True:
    OoT_bg.draw()
    item_bg.draw()
    if hookshotState == 0:
          default_hookshot.draw()
    if hookshotState == 1:
          hookshot.draw()
    if hookshotState == 2:
          longshot.draw()
    if bowState == 0:
          default_bow.draw()
    start = False
    pygame.display.update()
  for event in pygame.event.get():
      #pygame.quit() will run and close window
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
              x, y = event.pos
              if hookshot_rect.collidepoint(x, y) and hookshotState == 1:
                    hookshotState = 0
              elif hookshot_rect.collidepoint(x, y) and hookshotState == 2:
                    hookshotState = 1
              start = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click event
          x, y = event.pos
          if hookshot_rect.collidepoint(x, y) and hookshotState == 0:
                hookshotState = 1
                print("hookshot")
                start = True
                break
          if hookshot_rect.collidepoint(x, y) and hookshotState == 1:
                hookshotState = 2
                print("longshot")
                start = True
        if event.type == pygame.QUIT:
          run = False