import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((600, 600))

BG_img = pg.image.load("bg.png")

R = pg.image.load("rock.png")
R = pg.transform.scale(R, (150, 150))

S = pg.image.load("scissors.png")
S = pg.transform.scale(S, (150, 150))

P = pg.image.load("paper.png")
P = pg.transform.scale(P, (150, 150))

RSP = [R, S, P]

random_computer = random.choice(RSP)

font = pg.font.SysFont('malgungothic', 60)

text_surface_win = font.render("승리!", True, (255, 255, 255), None)
text_surface_lose = font.render("패배...", True, (255, 255, 255), None)
text_surface_tie = font.render("무승부!", True, (255, 255, 255), None)

running = True

while running:
    
    screen.blit(BG_img, BG_img.get_rect())
    scissors_pos = screen.blit(S, (50, 100))
    rock_pos = screen.blit(R, (200, 100))
    paper_pos = screen.blit(P, (350, 100))
    
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
        
            if scissors_pos.collidepoint(pg.mouse.get_pos()) :
                screen.blit(BG_img, BG_img.get_rect())
                
                screen.blit(S, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                if random_computer == R :
                    screen.blit(text_surface_lose, (200, 150))
                elif random_computer == S :
                    screen.blit(text_surface_tie, (200, 150))
                else:
                    screen.blit(text_surface_win, (200, 150))
                
                pg.display.update()
                pg.time.wait(3000)
                random_computer = random.choice(RSP)
                
                running = False

            elif rock_pos.collidepoint(pg.mouse.get_pos()) :
                screen.blit(BG_img, BG_img.get_rect())
                
                screen.blit(R, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                if random_computer == R :
                    screen.blit(text_surface_tie, (200, 150))
                elif random_computer == S :
                    screen.blit(text_surface_win, (200, 150))
                else:
                    screen.blit(text_surface_lose, (200, 150))
                
                pg.display.update()
                pg.time.wait(3000)
                random_computer = random.choice(RSP)

                running = False
                
            elif paper_pos.collidepoint(pg.mouse.get_pos()):
                screen.blit(BG_img, BG_img.get_rect())
                
                screen.blit(P, (80, 320))
                screen.blit(random_computer, (350, 320))
                
                if random_computer == R :
                    screen.blit(text_surface_win, (200, 150))
                elif random_computer == S :
                    screen.blit(text_surface_lose, (200, 150))
                else:
                    screen.blit(text_surface_tie, (200, 150))
                
                pg.display.update()
                pg.time.wait(3000)
                random_computer = random.choice(RSP)
                
                running = False
                
    pg.display.update()
    
pg.quit()