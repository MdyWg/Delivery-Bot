import math
import random
import pygame
import rclpy
import threading
from expression import Expression


pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

#colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

#fonts
free_serif = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 250)
noto = pygame.font.Font("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 200)
def event_continue():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def fit_shrink(font, text, color, max_width):
    width, height = font.size(text)
    f = font.render(text, True, color)
    if width <= max_width: 
        return f
    scale = max_width / width
    return pygame.transform.smoothscale(f, (round(width * scale), round(height * scale)))

def idle():
    face = fit_shrink(free_serif, "◜▿◝", WHITE, screen.get_width() * .9)
    face_rect = face.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    star = fit_shrink(free_serif, "⛦", YELLOW, screen.get_width() * .1)
    star_rect = star.get_rect(midright=(face_rect.left, screen.get_height()/2))
    screen.fill(BLACK)
    screen.blit(star, star_rect)
    screen.blit(face, face_rect)
    pygame.display.flip()

def happy():
    face = fit_shrink(free_serif, "⸜( > ᵕ < )⸝", WHITE, screen.get_width() * .7)
    face_rect = face.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    heart = fit_shrink(free_serif, "♡", RED, screen.get_width() * .1)
    heart_rect = heart.get_rect(midleft=(face_rect.right, screen.get_height()/2))
    screen.fill(BLACK)
    screen.blit(face, face_rect)
    screen.blit(heart, heart_rect)
    pygame.display.flip()

def confused():
    face = fit_shrink(free_serif, "  ๑  ๑  ", WHITE, screen.get_width() * .9)
    blush = fit_shrink(free_serif," ⸝⸝       ⸝⸝ ", PINK, screen.get_width() * .9)
    mouth = fit_shrink(noto, "﹏", WHITE, screen.get_width() * .9)
    face_rect = face.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    blush_rect = blush.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    mouth_rect = mouth.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.fill(BLACK)
    screen.blit(face, face_rect)
    screen.blit(blush, blush_rect)
    screen.blit(mouth, mouth_rect)
    pygame.display.flip()

def tired():
    face = fit_shrink(free_serif, "..zzZZ", WHITE, screen.get_width() * .4)
    eyes = fit_shrink(noto, "￣   ￣", WHITE, screen.get_width() * .5)
    mouth = fit_shrink(free_serif, "ρ", BLUE, screen.get_width() * .1)
    eyes_rect = eyes.get_rect(midleft=(screen.get_width()/2 * .1, screen.get_height()/2))
    face_rect = face.get_rect(midleft=(eyes_rect.right, screen.get_height()/2))
    mouth_rect = mouth.get_rect(midleft=(noto.size("￣")[0], screen.get_height()/2))
    screen.fill(BLACK)
    screen.blit(face, face_rect)
    screen.blit(eyes, eyes_rect)
    screen.blit(mouth, mouth_rect)
    pygame.display.flip()

def sad():
    face = fit_shrink(free_serif, "╥  ╥", WHITE, screen.get_width() * .9)
    mouth = fit_shrink(noto, "﹏", WHITE, screen.get_width() * .9)
    face_rect = face.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    mouth_rect = mouth.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.fill(BLACK)
    screen.blit(face, face_rect)
    screen.blit(mouth, mouth_rect)
    pygame.display.flip()

def silly():
    face = fit_shrink(free_serif, "¯\_(͡° ͜ʖ ͡°)_/¯", WHITE, screen.get_width() * .9)
    face_rect = face.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.fill(BLACK)
    screen.blit(face, face_rect)
    pygame.display.flip()

def main(args=None):
    rclpy.init(args=args)
    expression_node = Expression()

    thread = threading.Thread(target=rclpy.spin, args=(expression_node), daemon=True)
    thread.start()

    HOLD_TIME = 4000
    last_status = None
    next = 0

    running = True
    while running:
        running = event_continue()
        if not running: 
            break
        
        now = pygame.time.get_ticks()

        if expression_node.status != last_status:
            last_status = expression_node.status
            next = now + HOLD_TIME
        
        if expression_node.status != "idle" and now >= next:
            expression_node.status = "idle"
            last_status = "idle"

        if expression_node.status == "idle":
            idle()
        elif expression_node.status == "happy":
            happy()
        elif expression_node.status == "confused":
            confused()
        elif expression_node.status == "tired":
            tired()
        elif expression_node.status == "sad":
            sad()
        elif expression_node.status == "silly":
            silly()
        
        clock.tick(60)


    pygame.quit()