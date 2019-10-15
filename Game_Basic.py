import pygame
from Player import *
from Bullet import *
from Enemy import *

pygame.init()

display_width = 852
display_height = 500

bg = pygame.image.load(r'bg.jpg')

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Shooter Game")

clock = pygame.time.Clock()

retry = True
crashed = True

man = Player(362, 416, 64, 64) 
enemies = []
score = 0
enemyTrack = 1
enemies.append(Enemy(416, 64, 64))

global bullets
shotCoolDown = 0
prevScore = 0

highscore = 0
f = open(r"scores.txt", "r")
highscr = f.read()
f.close()

highscore = int(highscr)

fontT = pygame.font.SysFont("Comic Sans", 30, True)
fontS = pygame.font.SysFont("Comic Sans", 30, False, True)
fontH = pygame.font.SysFont("Times New Roman", 60, True, True)
fontP = pygame.font.SysFont("Times New Roman", 45, True)
fontD = pygame.font.SysFont("Times New Roman", 45, True)
Play = fontP.render("PLAY", 1, (32, 36, 204))
Heading = fontH.render("Shooter Game", 1, (162,39,171))
Dead = fontD.render("GAME OVER", 1, (255, 64, 64))

def redrawGameWindow():
    gameDisplay.blit(bg, (0,0))
    Title = fontT.render("Score: ", 1, (0,255,0))
    Title1 = fontT.render("High Score: ", 1, (0,255,0))
    Score = fontS.render(str(score), 1, (255,0,0))
    Score1 = fontS.render(str(highscore), 1, (255,0,0))
    pygame.draw.rect(gameDisplay, (255,0,0), (100, 30, 500, 10))
    pygame.draw.rect(gameDisplay, (0,128,0), (100, 30, man.health, 10))
    gameDisplay.blit(Title, (700, 30))
    gameDisplay.blit(Score, (785, 30))
    gameDisplay.blit(Title1, (650, 60))
    gameDisplay.blit(Score1, (785, 60))
    man.draw(gameDisplay)
    
    for i in range(0, len(enemies)):
        enemies[i].draw(gameDisplay, man)

    for bullet in bullets:
        bullet.draw(gameDisplay)

    pygame.display.update()


def introGameWindow():
    gameDisplay.blit(bg, (0, 0))
    
    gameDisplay.blit(Heading, ((display_width - Heading.get_width())//2, 80))
    
    
    pygame.draw.rect(gameDisplay, (255, 128, 255), ((display_width - Play.get_width())//2, 230, Play.get_width(), Play.get_height()))
    gameDisplay.blit(Play, ((display_width - Play.get_width())//2, 230))
    pygame.display.update()

while retry:
    scoreCount = 1
    introGameWindow()
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > (display_width - Play.get_width())//2 and mouse_pos[0] < (display_width + Play.get_width())//2 and mouse_pos[1] > 230 and mouse_pos[1] < 230 + Play.get_height():
        if pygame.mouse.get_pressed() == (True, False, False):
            crashed = False
            man.alive = True
            man.health = 500
            scoreCount = 0
            score = 0
            enemyTrack = 1
            enemies = []
            enemies.append(Enemy(416, 64, 64))

    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
                retry = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                crashed = False
    
    while not crashed:

        if man.alive == False:
            gameDisplay.blit(Dead, ((display_width - Dead.get_width())//2, (display_height - Dead.get_height())//2))
            pygame.display.update()
            i = 0
            while i < 200:
                pygame.time.delay(20)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()
            crashed = True
        else:
            if shotCoolDown > 0:
                shotCoolDown += 1
            if shotCoolDown > 3:
                shotCoolDown = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    retry = False
    
            for i in range(0, len(enemies)):
        
                for bullet in bullets:
                    if bullet.y - bullet.radius < enemies[i].hitbox[1] + enemies[i].hitbox[3] and  bullet.y + bullet.radius > enemies[i].hitbox[1]:
                        if bullet.x + bullet.radius > enemies[i].hitbox[0] and bullet.x - bullet.radius < enemies[i].hitbox[0] + enemies[i].hitbox[2]:
                            enemies[i].hit()
                            bullets.pop(bullets.index(bullet))
                            score += 1
        
                    if bullet.x < display_width and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))

            for i in range(0, len(enemies)):
                if man.hitbox[1] + man.hitbox[3] < enemies[i].hitbox[1] + enemies[i].hitbox[3] and  man.hitbox[1] + man.hitbox[3] > enemies[i].hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > enemies[i].hitbox[0] and man.hitbox[0] + man.hitbox[2] < enemies[i].hitbox[0] + enemies[i].hitbox[2]:
                        man.hit()
    
            key_pressed = pygame.key.get_pressed()

            if key_pressed[pygame.K_s] and shotCoolDown == 0:
                facing = 1
        
                if len(bullets) < 6:
                    bullets.append(Bullet(round(man.x_player + man.width//2), round(man.y_player + man.height//2), 6, (0,0,0), facing))

                shotCoolDown = 1

            elif key_pressed[pygame.K_a] and shotCoolDown == 0:
                facing = -1
        
                if len(bullets) < 6:
                    bullets.append(Bullet(round(man.x_player + man.width//2), round(man.y_player + man.height//2), 6, (0,0,0), facing))

                shotCoolDown = 1

            if key_pressed[pygame.K_LEFT] and man.x_player > 0:
                man.x_player -= man.vel
                man.left = True
                man.right = False
                man.standing = False
            elif key_pressed[pygame.K_RIGHT] and man.x_player < display_width - man.width:
                man.x_player += man.vel
                man.left = False
                man.right = True
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0

            if not man.isJump:
                if key_pressed[pygame.K_SPACE]:
                    man.isJump = True
            
            else:
                if man.jumpCount >= -10:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.y_player -= (man.jumpCount ** 2) * 0.375 * neg
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10
    
            if score > 20 and enemyTrack == 1:
                enemyTrack = 2
                enemies.append(Enemy(416, 64, 64))
                #print(enemies)
            if score > 50 and enemyTrack == 2:
                enemyTrack = 3
                enemies.append(Enemy(416, 64, 64))
                #print(enemies)
            if score > 100:
                for i in range(0, len(enemies)):
                    enemies[i].vel = 4
            if score > 250:
                for i in range(0, len(enemies)):
                    enemies[i].vel = 5
            if score > 400 and enemyTrack == 3:
                enemyTrack = 4
                enemies.append(Enemy(416, 64, 64))
                #print(enemies)
                prevScore = 400
            if score > 700:
                if score - prevScore >= 300:
                    prevScore = score
                    enemies.append(Enemy(416, 64, 64))

        redrawGameWindow()
        clock.tick(27)
    
    if scoreCount == 0:
        f = open(r"scores.txt", "r")
        highscr = f.read()
        f.close()
        f = open(r"scores.txt", "w")
        if int(highscr) < score:
            f.write(str(score))
            highscore = score
        else:
            f.write(str(highscr))
            highscore = highscore
        f.close()
        #print(score)
        scoreCount = 1

pygame.quit()
quit()


