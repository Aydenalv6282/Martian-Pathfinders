import pygame

pygame.init()
scale = 1
screen_width, screen_height = 1440,820
screen = pygame.display.set_mode((screen_width, screen_height))
base_font = pygame.font.Font(None,32)
b = pygame.image.load("elements/nasa_mars_map_001.png")

lon_from_text = ""
lat_from_text = ""
lon_to_text = ""
lat_to_text = ""

lon_from_rect = pygame.Rect(50,760,100,32)
lat_from_rect = pygame.Rect(160,760,100,32)
lon_to_rect = pygame.Rect(270,760,100,32)
lat_to_rect = pygame.Rect(380,760,100,32)
start_rect = pygame.Rect(1300,760,70,32)

rect_color_active = pygame.Color("Green")
rect_color_passive = (0,0,0)

lon_rect_color = rect_color_passive
lat_rect_color = rect_color_passive

lon_from_active = False
lat_from_active = False
lon_to_active = False
lat_to_active = False

prompt_state = True

while prompt_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prompt_state = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lon_from_rect.collidepoint(event.pos) and lat_from_active==False and lon_to_active == False and lat_to_active == False:
                lon_from_active = True
            else:
                lon_from_active = False

            if lat_from_rect.collidepoint(event.pos) and lon_from_active==False and lon_to_active==False and lat_to_active==False:
                lat_from_active = True
            else:
                lat_from_active = False

            if lon_to_rect.collidepoint(event.pos) and lat_from_active==False and lon_from_active == False and lat_to_active == False:
                lon_to_active = True
            else:
                lon_to_active = False

            if lat_to_rect.collidepoint(event.pos) and lon_from_active==False and lon_to_active==False and lat_from_active==False:
                lat_to_active = True
            else:
                lat_to_active = False

            if start_rect.collidepoint((event.pos)):
                pass
        if event.type == pygame.KEYDOWN:
            if lon_from_active:
                if event.key == pygame.K_BACKSPACE:
                    lon_from_text = lon_from_text[:-1]
                else:
                    lon_from_text += event.unicode

            if lat_from_active:
                if event.key == pygame.K_BACKSPACE:
                    lat_from_text = lat_from_text[:-1]
                else:
                    lat_from_text += event.unicode

            if lon_to_active:
                if event.key == pygame.K_BACKSPACE:
                    lon_to_text = lon_to_text[:-1]
                else:
                    lon_to_text += event.unicode

            if lat_to_active:
                if event.key == pygame.K_BACKSPACE:
                    lat_to_text = lat_from_text[:-1]
                else:
                    lat_to_text += event.unicode

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
    screen.fill((254, 254, 254))
    pygame.draw.rect(screen,lon_from_rect_color,lon_from_rect,2)
    pygame.draw.rect(screen,lat_from_rect_color,lat_from_rect,2)
    pygame.draw.rect(screen, lon_to_rect_color, lon_to_rect, 2)
    pygame.draw.rect(screen, lat_to_rect_color, lat_to_rect, 2)
    pygame.draw.rect(screen,(0,0,0),start_rect,2)
    screen.blit(b, b.get_rect(topleft=(0, 0)))

    lon_from_surface = base_font.render(lon_from_text,True,(0,0,0))
    lat_from_surface = base_font.render(lat_from_text,True,(0,0,0))
    lon_to_surface = base_font.render(lon_to_text, True, (0, 0, 0))
    lat_to_surface = base_font.render(lat_to_text, True, (0, 0, 0))
    start_surface = base_font.render("Start",True,(0,0,0))

    screen.blit(lon_from_surface,(lon_from_rect.x+5,lon_from_rect.y+5))
    screen.blit(lat_from_surface,(lat_from_rect.x+5,lat_from_rect.y+5))
    screen.blit(lon_to_surface,(lon_to_rect.x+5,lon_from_rect.y+5))
    screen.blit(lat_to_surface, (lat_to_rect.x + 5, lat_from_rect.y + 5))
    screen.blit(start_surface,(start_rect.x+5,start_rect.y+5))
    pygame.display.flip()