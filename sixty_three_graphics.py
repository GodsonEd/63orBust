import pygame as pg

pg.init()
screen = pg.display.set_mode((1300, 650))
pg.display.set_caption('Heroes expand')
pg.mouse.set_visible(1)

class sixty_three_graphics():

    def sixty(self):


        background = pg.image.load("Textures/background.jpg")
        background = pg.transform.smoothscale(background,(1300, 650))

        card_List = [["2_of_clubs", 2], ["2_of_diamonds", 2], ["2_of_hearts", 2], ["2_of_spades", 2],
                     ["3_of_clubs", 3], ["3_of_diamonds", 3], ["3_of_hearts", 3], ["3_of_spades", 3],
                     ["4_of_clubs", 4], ["4_of_diamonds", 4], ["4_of_hearts", 4], ["4_of_spades", 4],
                     ["5_of_clubs", 5], ["5_of_diamonds", 5], ["5_of_hearts", 5], ["5_of_spades", 5],
                     ["6_of_clubs", 6], ["6_of_diamonds", 6], ["6_of_hearts", 6], ["6_of_spades", 6],
                     ["7_of_clubs", 7], ["7_of_diamonds", 7], ["7_of_hearts", 7], ["7_of_spades", 7],
                     ["8_of_clubs", 8], ["8_of_diamonds", 8], ["8_of_hearts", 8], ["8_of_spades", 8],
                     ["9_of_clubs", 9], ["9_of_diamonds", 9], ["9_of_hearts", 9], ["9_of_spades", 9],
                     ["10_of_clubs", 10], ["10_of_diamonds", 10], ["10_of_hearts", 10], ["10_of_spades", 10],
                     ["jack_of_clubs", 11], ["jack_of_diamonds", 11], ["jack_of_hearts", 11], ["jack_of_spades", 11],
                     ["king_of_clubs", 12], ["king_of_diamonds", 12], ["king_of_hearts", 12], ["king_of_spades", 12],
                     ["queen_of_clubs", 13], ["queen_of_diamonds",13], ["queen_of_hearts", 13], ["queen_of_spades", 13],
                     ["ace_of_clubs", 1], ["ace_of_diamonds", 1], ["ace_of_hearts", 1], ["ace_of_spades", 1]
                     ]

        My_red_color = (255, 0, 0)
        My_blue_color = (0, 0, 255)
        My_green_color = (0, 255, 0)
        My_yellow_color = (255, 255, 0)
        My_purple_color = (148, 0, 211)
        WHITE_WHITE_HOORAY = (255, 255, 255)
        My_light_red_color = (255, 180, 180)
        My_light_blue_color = (190, 190, 255)

        input_box = pg.Rect((0, 0, 250, 250))
        intro_exit = pg.Rect((1100,550,200,100))

        Loaded_Image_List = []
        Rect_List = []

        text = ''

        drag = 0
        total = 0
        position = 0
        clicked = False
        intro_done = False

        my_font = pg.font.SysFont('Comic Sans MS', 25)
        text_surface1 = my_font.render('63 or Bust', False, My_red_color)
        text_surface2 = my_font.render('Player 1', False, My_red_color)
        text_surface3 = my_font.render('Player 2', False, My_red_color)
        text_surface5 = my_font.render('Exit', False, My_red_color)

        for x in range(len(card_List)):
            Loaded_Image_List.append(
                [pg.image.load("Textures/PNG-cards-1.3/" + card_List[x][0] + ".png").convert(), card_List[x][1]])

        for x in range(len(card_List)):
            Rect_List.append(autoDraw("null",Loaded_Image_List[x][0],"null",525,235,125,181,2))



        clock = pg.time.Clock()
        done = 0
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

                screen.blit(background,(0,0))


                if(intro_done!=True):
                    text_surface4 = my_font.render("Name: " + text, False, My_blue_color)

                    pg.draw.rect(screen, My_purple_color, input_box)
                    pg.draw.rect(screen,My_green_color, intro_exit)

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            clicked = True

                    if clicked == True:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                print(text)
                                text = ''
                                clicked = False
                            elif event.key == pg.K_BACKSPACE:
                                text = text[:-2]
                            else:
                                text += event.unicode

                    screen.blit(text_surface4, (0, 0))
                    screen.blit(text_surface5, (1200,600))

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if intro_exit.collidepoint(event.pos):
                            intro_done = True
                else:
                    text_surface4 = my_font.render("total: "+str(total), False, My_light_blue_color)

                    if event.type == pg.MOUSEBUTTONDOWN:
                        mx, my = event.pos
                        for x in range(len(Rect_List)):
                            if Rect_List[x].collidepoint(mx, my):
                                position = x
                                autoDraw("null", Loaded_Image_List[x][0], "null", mx, my, 125, 181, 3)
                                drag = True
                    elif event.type == pg.MOUSEBUTTONUP:
                        if(drag == True):
                            drag = False
                            fx, fy = event.pos
                            Rect_List[position] = autoDraw("null", Loaded_Image_List[position][0], "null", fx, fy, 125, 181, 3)
                            if Rect_List[position].colliderect(pg.Rect((0, 0, 250, 250))):
                                total += Loaded_Image_List[position][1]
                                Loaded_Image_List.remove(Loaded_Image_List[position])
                                Rect_List.remove(Rect_List[position])
                    elif event.type == pg.MOUSEMOTION:
                        if(drag):
                            mx, my = event.pos
                            Rect_List[position] = autoDraw("null", Loaded_Image_List[position][0], "null", mx, my, 125, 181, 3)

                    for x in range(len(Loaded_Image_List)):
                        autoDraw("null", Loaded_Image_List[x][0], "null", Rect_List[x].x, Rect_List[x].y, 125, 181, 2)

                    pg.draw.rect(screen, My_red_color, pg.Rect((0,0,250,250)))
                    screen.blit(text_surface4,(1000,0))
                    screen.blit(text_surface1,(625, 0))

            clock.tick(60)
            pg.display.update()


#type(0) = online image, type(1) = all in one area, type(2) = drawing individual cards, type(3) = same as type(2) but returns only the rect, type(4) = draws a rectangle
def autoDraw(images, image, num_of_times, x1, y1, length, width, type):
    if type == 0:
        for x in range(num_of_times):
            Loaded_Image = pg.transform.smoothscale(images[x], (length, width))
            if x < 6:
                screen.blit(Loaded_Image, (x * x1, y1))
                rect = Loaded_Image.get_rect()
                rect = rect.move((x * x1, y1))
                return rect
            elif x >= 6:
                screen.blit(Loaded_Image, ((x * x1) - 1320, y1+150))
                rect = Loaded_Image.get_rect()
                rect = rect.move(((x * x1) - 1320, y1+150))
                return rect
    if type == 1:
        for x in range(num_of_times):
            Loaded_Image = pg.transform.smoothscale(images[x], (length, width))
            screen.blit(Loaded_Image, (x * x1, y1))
            rect = Loaded_Image.get_rect()
            rect = rect.move((x * x1, y1))
            return rect
    if type == 2:
        Loaded_Image = pg.transform.smoothscale(image, (length, width))
        screen.blit(Loaded_Image, (x1, y1))
        rect = Loaded_Image.get_rect()
        rect = rect.move((x1, y1))
        return rect
    if type == 3:
        Loaded_Image = pg.transform.smoothscale(image, (length, width))
        rect = Loaded_Image.get_rect()
        rect = rect.move((x1, y1))
        return rect
name = sixty_three_graphics()
name.sixty()