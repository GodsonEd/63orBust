import pygame as pg

pg.init()
screen = pg.display.set_mode((1300, 650))
pg.display.set_caption('Heroes expand')
pg.mouse.set_visible(1)

class TestText():

    def sixty(self):
        background = pg.image.load("Textures/background.jpg")
        background = pg.transform.smoothscale(background, (1300, 650))

        my_font = pg.font.SysFont('Comic Sans MS', 25)
        text = ''

        My_red_color = (255, 0, 0)
        My_blue_color = (0, 0, 255)
        My_green_color = (0, 255, 0)
        My_yellow_color = (255, 255, 0)
        WHITE_WHITE_HOORAY = (255, 255, 255)
        My_light_red_color = (255, 180, 180)
        My_light_blue_color = (190, 190, 255)

        input_box = pg.Rect((0,0,250,250))
        clicked = False

        clock = pg.time.Clock()
        done = 0
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

                screen.blit(background, (0, 0))

                text_surface1 = my_font.render("Name: "+text, False, My_blue_color)

                pg.draw.rect(screen, My_red_color, input_box)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        clicked = True

                if clicked == True:
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            print (text)
                            text = ''
                            clicked = False
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-2]
                        else:
                            text += event.unicode
                screen.blit(text_surface1,(0,0))

                clock.tick(60)
                pg.display.update()
name = TestText()
name.sixty()