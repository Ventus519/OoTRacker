#import
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
vanilla_dungeon_keys = [0, 0, 0, "?", "?", 6, "?", "?", 3, "?", 0]

#image loading
  #background (not yet)

  #default item loading


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