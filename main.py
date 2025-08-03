import pygame
import numpy as np
from pygame.examples.cursors import image
import sys
import Algos
import MapGenerator
from MapGenerator import MapGen, PointmapGen
import PlanetViewer
from PlanetViewer import planet


# start pygame, set source paths
pygame.init()
pygame.display.set_caption("Martian Pathfinders")
scale = 1
screen_width, screen_height = 1440,820
screen = pygame.display.set_mode((screen_width, screen_height))
base_font = pygame.font.Font(None,32)
b = pygame.image.load("elements/nasa_mars_map_001.png")
source_path_1 = "Mars/MarsAdjaListLR100.csv" # Source Path for the Adjacency List
source_path_2 = "Mars/MarsPolarLR100.csv" # Source Path for Polar Coordinates
source_path_3 = "Mars/MarsCartesianLR100.csv" # Source Path for Cartesian Coordinates


# Initialize text used to input destination coordinates
lon_from_text = ""
lat_from_text = ""
lon_to_text = ""
lat_to_text = ""

# Load data structures for use in graphs
adjalist = np.loadtxt(source_path_1, delimiter=",", dtype=np.int32)
pol_coords = np.loadtxt(source_path_2, delimiter=",", dtype=np.float64)
car_coords = np.loadtxt(source_path_3, delimiter=",", dtype=np.int32)

# Setting button rect objects
from_txt_rect = pygame.Rect(50,760,100,32)
lon_from_rect = pygame.Rect(120,760,100,32)
lat_from_rect = pygame.Rect(230,760,100,32)
to_txt_rect = pygame.Rect(340,760,40,32)
lon_to_rect = pygame.Rect(380,760,100,32)
lat_to_rect = pygame.Rect(490,760,100,32)
adjalist_rect = pygame.Rect(620,760,130,32)
dijkstra_rect = pygame.Rect(930,760,100,32)
astar_rect = pygame.Rect(1040,760,100,32)
start_rect = pygame.Rect(1200,760,70,32)
viewer_rect = pygame.Rect(1300,760,90,32)

# Button colors
rect_color_active = pygame.Color("Green")
rect_color_passive = (0,0,0)

# Button activation states
lon_from_active = False
lat_from_active = False
lon_to_active = False
lat_to_active = False
dijkstra_active = False
astar_active = False
adjalist_active = False
start_active = False
viewer_active = False

# Menu states
prompt_state = True
planet_state = False

# Map loop
# This is where the user will enter coordinates, set coordinates, choose what algo they want to use
# and create the map
while prompt_state:
    for event in pygame.event.get():
        # when user quits
        if event.type == pygame.QUIT:
            prompt_state = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse button interactions

            # coordinate interactions
            # From coords
            if lon_from_rect.collidepoint(event.pos) and lat_from_active==False and lon_to_active == False and lat_to_active == False:
                lon_from_active = True
            else:
                lon_from_active = False

            if lat_from_rect.collidepoint(event.pos) and lon_from_active==False and lon_to_active==False and lat_to_active==False:
                lat_from_active = True
            else:
                lat_from_active = False

            # To coords
            if lon_to_rect.collidepoint(event.pos) and lat_from_active==False and lon_from_active == False and lat_to_active == False:
                lon_to_active = True
            else:
                lon_to_active = False

            if lat_to_rect.collidepoint(event.pos) and lon_from_active==False and lon_to_active==False and lat_from_active==False:
                lat_to_active = True
            else:
                lat_to_active = False

            # algorithm interactions
            if dijkstra_rect.collidepoint(event.pos):
                dijkstra_active = True
                astar_active = False
            if astar_rect.collidepoint(event.pos):
                astar_active = True
                dijkstra_active = False

            # button interactions
            if adjalist_rect.collidepoint(event.pos):
                adjalist_active = True
            if start_rect.collidepoint(event.pos):
                start_active = True
            if viewer_rect.collidepoint(event.pos):
                viewer_active = True
                planet_state = True
        if event.type == pygame.MOUSEBUTTONUP:
            # Finding the closest points in data set to where user enters
            if adjalist_active:
                starting_point, ending_point = Algos.point_finder(np.array([np.float64(lon_from_text),np.float64(lat_from_text)]),np.array([np.float64(lon_to_text),np.float64(lat_to_text)]),pol_coords)
                point_index = [(float(lon_from_text),float(lat_from_text)),(float(lon_to_text),float(lat_to_text))]
                print(point_index)
                PointmapGen(point_index) # Generates new image based off locked in coords
                b = pygame.image.load("output/mars_index.png") # sets background to be new image
                adjalist_active = False

            # Start button interactions
            if start_active:
                # What happens if dijkstra is chosen when start
                if dijkstra_active:
                    path = Algos.Dijkstras(starting_point,ending_point,adjalist, pol_coords)
                    MapGen(path)
                    b = pygame.image.load("output/mars_path.png")# Generates new image with path traversed
                    dijkstra_active = False
                start_active = False
                # What happens if Astar is chosen when start
                if astar_active:
                    path = Algos.AStar(starting_point,ending_point,adjalist, pol_coords, car_coords)
                    MapGen(path)
                    b = pygame.image.load("output/mars_path.png")# Generates new image with path traversed
                    astar_active = False
        if event.type == pygame.KEYDOWN:
            # User keyboard interactions

            # To type in 'from' coords
            if lon_from_active:
                if event.key == pygame.K_BACKSPACE:
                    lon_from_text = lon_from_text[:-1]
                elif event.key == pygame.K_RETURN:
                    lon_from_active = False
                    lat_from_active = True
                else:
                    lon_from_text += event.unicode

            elif lat_from_active:
                if event.key == pygame.K_BACKSPACE:
                    lat_from_text = lat_from_text[:-1]
                elif event.key == pygame.K_RETURN:
                    lat_from_active = False
                    lon_to_active = True
                else:
                    lat_from_text += event.unicode

            # To type in 'to' coords
            elif lon_to_active:
                if event.key == pygame.K_BACKSPACE:
                    lon_to_text = lon_to_text[:-1]
                elif event.key == pygame.K_RETURN:
                    lon_to_active = False
                    lat_to_active = True
                else:
                    lon_to_text += event.unicode

            elif lat_to_active:
                if event.key == pygame.K_BACKSPACE:
                    lat_to_text = lat_to_text[:-1]
                elif event.key == pygame.K_RETURN:
                    lat_to_active = False
                else:
                    lat_to_text += event.unicode

    # Color changing based off activity state
    if lon_from_active:
        lon_from_rect_color = rect_color_active
    else:
        lon_from_rect_color = rect_color_passive
    if lat_from_active:
        lat_from_rect_color = rect_color_active
    else:
        lat_from_rect_color = rect_color_passive
    if lon_to_active:
        lon_to_rect_color = rect_color_active
    else:
        lon_to_rect_color = rect_color_passive
    if lat_to_active:
        lat_to_rect_color = rect_color_active
    else:
        lat_to_rect_color = rect_color_passive
    if dijkstra_active:
        dijkstra_rect_color = rect_color_active
    else:
        dijkstra_rect_color = rect_color_passive
    if astar_active:
        astar_rect_color = rect_color_active
    else:
        astar_rect_color = rect_color_passive
    if adjalist_active:
        adjalist_color = rect_color_active
    else:
        adjalist_color = rect_color_passive
    if start_active:
        start_color = rect_color_active
    else:
        start_color = rect_color_passive
    if viewer_active:
        viewer_color = rect_color_active
    else:
        viewer_color = rect_color_passive
    # Pygame drawing rects
    screen.fill((254, 254, 254))
    pygame.draw.rect(screen,(255,255,255),from_txt_rect)
    pygame.draw.rect(screen,lon_from_rect_color,lon_from_rect,2)
    pygame.draw.rect(screen,lat_from_rect_color,lat_from_rect,2)
    pygame.draw.rect(screen,(255,255,255),to_txt_rect)
    pygame.draw.rect(screen, lon_to_rect_color, lon_to_rect, 2)
    pygame.draw.rect(screen, lat_to_rect_color, lat_to_rect, 2)
    pygame.draw.rect(screen,adjalist_color,adjalist_rect,2)
    pygame.draw.rect(screen,dijkstra_rect_color,dijkstra_rect,2)
    pygame.draw.rect(screen,astar_rect_color,astar_rect,2)
    pygame.draw.rect(screen,start_color,start_rect,2)
    pygame.draw.rect(screen,viewer_color,viewer_rect,2)
    # Pygame display draw
    screen.blit(b, b.get_rect(topleft=(0, 0)))

    # Pygame rendering text on screen
    from_txt_surface = base_font.render("From:",True,(0,0,0))
    lon_from_surface = base_font.render(lon_from_text,True,(0,0,0))
    lat_from_surface = base_font.render(lat_from_text,True,(0,0,0))
    to_txt_surface = base_font.render("To:",True,(0,0,0))
    lon_to_surface = base_font.render(lon_to_text, True, (0, 0, 0))
    lat_to_surface = base_font.render(lat_to_text, True, (0, 0, 0))
    adjalist_surface = base_font.render("Set points",True,(0,0,0))
    dijkstra_surface = base_font.render("Dijkstra",True,(0,0,0))
    astar_surface = base_font.render("Astar",True,(0,0,0))
    start_surface = base_font.render("Start",True,(0,0,0))
    viewer_surface = base_font.render("Viewer",True,(0,0,0))

    # Pygame displays all rect surfaces and formats text within them
    screen.blit(from_txt_surface,(from_txt_rect.x+5,from_txt_rect.y+5))
    screen.blit(lon_from_surface,(lon_from_rect.x+5,lon_from_rect.y+5))
    screen.blit(lat_from_surface,(lat_from_rect.x+5,lat_from_rect.y+5))
    screen.blit(to_txt_surface,(to_txt_rect.x+5,to_txt_rect.y+5))
    screen.blit(lon_to_surface,(lon_to_rect.x+5,lon_from_rect.y+5))
    screen.blit(lat_to_surface, (lat_to_rect.x + 5, lat_from_rect.y + 5))
    screen.blit(adjalist_surface,(adjalist_rect.x+5,adjalist_rect.y+5))
    screen.blit(dijkstra_surface,(dijkstra_rect.x+5,dijkstra_rect.y+5))
    screen.blit(astar_surface,(astar_rect.x+5,astar_rect.y+5))
    screen.blit(start_surface,(start_rect.x+5,start_rect.y+5))
    screen.blit(viewer_surface,(viewer_rect.x+5,viewer_rect.y+5))
    pygame.display.flip()

    # Displays planet surface with drawn path
    if planet_state:
        planet("output/mars_path.png")