

# import pygame
# import random
# from pygame.locals import *

# # Dimensões da tela
# SCREEN_WIDTH = 450
# SCREEN_HEIGHT = 800
# SPEED = 10
# GRAVITY = 1
# GAME_SPEED = 10

# # Dimensões do chão
# GROUND_WIDTH = 2 * SCREEN_WIDTH
# GROUND_HEIGHT = 100

# # Dimensões do cano
# PIPE_WIDTH = 80
# PIPE_HEIGHT = 500
# PIPE_GAP = 200

# # Cores
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# # Fontes
# pygame.font.init()
# FONTE_PONTOS = pygame.font.SysFont("arial", 30)  # Ajuste o tamanho da fonte
# FONTE_GAME_OVER = pygame.font.SysFont("arial", 50)  # Ajuste o tamanho da fonte
# FONTE_BOTAO = pygame.font.SysFont("arial", 25)  # Ajuste o tamanho da fonte

# class Bird(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.images = [
#             pygame.image.load("bluebird-upflap.png").convert_alpha(),
#             pygame.image.load("bluebird-midflap.png").convert_alpha(),
#             pygame.image.load("bluebird-downflap.png").convert_alpha(),
#         ]
#         self.speed = SPEED
#         self.current_image = 0
#         self.image = self.images[self.current_image]
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect = self.image.get_rect()
#         self.rect[0] = SCREEN_WIDTH / 2 - 10
#         self.rect[1] = SCREEN_HEIGHT / 2

#     def update(self):
#         self.current_image = (self.current_image + 1) % 3
#         self.image = self.images[self.current_image]
#         self.speed += GRAVITY
#         self.rect[1] += self.speed

#     def bump(self):
#         self.speed = -SPEED

# class Pipe(pygame.sprite.Sprite):
#     def __init__(self, inverted, xpos, ysize):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("pipe-red.png").convert_alpha()
#         self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
#         self.rect = self.image.get_rect()
#         self.rect[0] = xpos
#         if inverted:
#             self.image = pygame.transform.flip(self.image, False, True)
#             self.rect[1] = -(self.rect[3] - ysize)
#         else:
#             self.rect[1] = SCREEN_HEIGHT - ysize
#         self.mask = pygame.mask.from_surface(self.image)
#         self.passed = False

#     def update(self):
#         self.rect[0] -= GAME_SPEED

# class Ground(pygame.sprite.Sprite):
#     def __init__(self, xpos):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("base.png").convert_alpha()
#         self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect = self.image.get_rect()
#         self.rect[0] = xpos
#         self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

#     def update(self):
#         self.rect[0] -= GAME_SPEED

# def is_off_screen(sprite):
#     return sprite.rect[0] < -(sprite.rect[2])

# def get_random_pipes(xpos, previous_height=None):
#     size_options = [100, 150, 200, 250, 300, 350]
#     if previous_height is not None:
#         size_options.remove(previous_height)
#     size = random.choice(size_options)
#     pipe = Pipe(False, xpos, size)
#     pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
#     return (pipe, pipe_inverted), size

# def desenhar_tela(tela, pontos):
#     tela.blit(BACKGROUND, (0, 0))
#     bird_group.draw(tela)
#     pipe_group.draw(tela)
#     ground_group.draw(tela)
#     texto_pontos = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
#     tela.blit(texto_pontos, (SCREEN_WIDTH - 10 - texto_pontos.get_width(), 10))
#     pygame.display.update()

# def draw_text_centered(surface, text, font, color, center):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=center)
#     surface.blit(text_surface, text_rect)
#     return text_rect

# def draw_box(surface, rect, color, border_radius=0):
#     pygame.draw.rect(surface, color, rect, border_radius=border_radius)
#     pygame.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=border_radius)  # Borda

# def game_over(tela, pontos):
#     # Desenhar texto "Game Over"
#     draw_text_centered(tela, "Game Over", FONTE_GAME_OVER, (255, 0, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150))

#     # Definir o retângulo para a caixa contendo a pontuação e o botão
#     box_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50, 300, 200)
    
#     # Desenhar a caixa
#     draw_box(tela, box_rect, (255, 255, 255), border_radius=10)
    
#     # Desenhar pontuação dentro da caixa
#     draw_text_centered(tela, f"Pontos: {pontos}", FONTE_PONTOS, (0, 0, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30))
    
#     # Desenhar botão "Jogar Novamente" dentro da caixa com fundo verde
#     botao_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 30, 200, 50)
#     pygame.draw.rect(tela, GREEN, botao_rect, border_radius=10)
#     rect_reiniciar = draw_text_centered(tela, "Jogar Novamente", FONTE_BOTAO, (0, 0, 0), botao_rect.center)

#     pygame.display.update()

#     while True:
#         mouse_pos = pygame.mouse.get_pos()
#         mouse_over_button = botao_rect.collidepoint(mouse_pos)

#         if mouse_over_button:
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#             pygame.draw.rect(tela, GREEN, botao_rect.move(0, -2), border_radius=10)  # Desenhar botão elevado
#         else:
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
#             pygame.draw.rect(tela, GREEN, botao_rect, border_radius=10)  # Desenhar botão normal

#         rect_reiniciar = draw_text_centered(tela, "Jogar Novamente", FONTE_BOTAO, (0, 0, 0), botao_rect.center)

#         pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 exit()
#             if event.type == MOUSEBUTTONDOWN and mouse_over_button:
#                 return

# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# BACKGROUND = pygame.image.load("background-day.png")
# BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# pygame.mixer.init()
# jump_sound = pygame.mixer.Sound("passaro-voando.ogg")
# point_sound = pygame.mixer.Sound("pontos.ogg")
# die_sound = pygame.mixer.Sound("som-da-morte.ogg")

# def start_game():
#     global bird_group, pipe_group, ground_group

#     bird_group = pygame.sprite.Group()
#     bird = Bird()
#     bird_group.add(bird)

#     ground_group = pygame.sprite.Group()
#     for i in range(2):
#         ground = Ground(GROUND_WIDTH * i)
#         ground_group.add(ground)

#     pipe_group = pygame.sprite.Group()
#     previous_pipe_height = None
#     for i in range(2):
#         pipes, previous_pipe_height = get_random_pipes(SCREEN_WIDTH * i + 800, previous_pipe_height)
#         pipe_group.add(pipes[0])
#         pipe_group.add(pipes[1])

#     pontos = 0
#     passed_pipe_set = False
#     clock = pygame.time.Clock()

#     while True:
#         clock.tick(30)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_SPACE:
#                     bird.bump()
#                     jump_sound.play()

#         screen.blit(BACKGROUND, (0, 0))

#         if is_off_screen(ground_group.sprites()[0]):
#             ground_group.remove(ground_group.sprites()[0])
#             new_ground = Ground(GROUND_WIDTH - 20)
#             ground_group.add(new_ground)

#         if is_off_screen(pipe_group.sprites()[0]):
#             pipe_group.remove(pipe_group.sprites()[0])
#             pipe_group.remove(pipe_group.sprites()[0])
#             pipes, previous_pipe_height = get_random_pipes(SCREEN_WIDTH * 2, previous_pipe_height)
#             pipe_group.add(pipes[0])
#             pipe_group.add(pipes[1])

#         bird_group.update()
#         ground_group.update()
#         pipe_group.update()

#         if (
#             pygame.sprite.groupcollide(
#                 bird_group, ground_group, False, False, pygame.sprite.collide_mask
#             )
#             or pygame.sprite.groupcollide(
#                 bird_group, pipe_group, False, False, pygame.sprite.collide_mask
#             )
#         ):
#             die_sound.play()
#             desenhar_tela(screen, pontos)  # Desenhar a tela antes de exibir o "Game Over"
#             game_over(screen, pontos)
#             return

#         for cano in pipe_group:
#             if not cano.passed and bird.rect.right > cano.rect.left:
#                 cano.passed = True
#                 if not passed_pipe_set:
#                     pontos += 1
#                     point_sound.play()
#                     passed_pipe_set = True

#         for cano in pipe_group:
#             if cano.rect.right < 0:
#                 pipe_group.remove(cano)
#                 passed_pipe_set = False

#         if len(pipe_group) < 2:
#             pipes, previous_pipe_height = get_random_pipes(SCREEN_WIDTH * 2, previous_pipe_height)
#             pipe_group.add(pipes[0])
#             pipe_group.add(pipes[1])

#         desenhar_tela(screen, pontos)

# while True:
#     start_game()






import pygame
import random
from pygame.locals import *

# Dimensões da tela
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

# Dimensões do chão
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

# Dimensões do cano
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 200

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Fontes
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("arial", 30)  # Ajuste o tamanho da fonte
FONTE_GAME_OVER = pygame.font.SysFont("arial"
                                      , 50, bold=True)  # Fonte do Game Over
FONTE_BOTAO = pygame.font.SysFont("arial", 14)  # Ajuste o tamanho da fonte

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("bluebird-upflap.png").convert_alpha(),
            pygame.image.load("bluebird-midflap.png").convert_alpha(),
            pygame.image.load("bluebird-downflap.png").convert_alpha(),
        ]
        self.speed = SPEED
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2 - 10
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -SPEED

class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe-red.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize
        self.mask = pygame.mask.from_surface(self.image)
        self.passed = False

    def update(self):
        self.rect[0] -= GAME_SPEED

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("base.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_pipes(xpos, previous_height=None):
    size_options = [100, 150, 200, 250, 300, 350]
    if previous_height is not None:
        size_options.remove(previous_height)
    size = random.choice(size_options)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return (pipe, pipe_inverted), size

def desenhar_tela(tela, pontos):
    tela.blit(BACKGROUND, (0, 0))
    bird_group.draw(tela)
    pipe_group.draw(tela)
    ground_group.draw(tela)
    texto_pontos = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto_pontos, (SCREEN_WIDTH - 10 - texto_pontos.get_width(), 10))
    pygame.display.update()

def draw_text_centered(surface, text, font, text_color, center, outline_color=BLACK, outline_width=2):
    text_surface = font.render(text, True, text_color)
    outline_surface = font.render(text, True, outline_color)

    # Create a surface for the outline
    w, h = text_surface.get_size()
    outline_surface = pygame.Surface((w + outline_width * 2, h + outline_width * 2), pygame.SRCALPHA)
    outline_surface.fill((0, 0, 0, 0))  # Transparent background

    # Draw the outline
    outline_surface.blit(font.render(text, True, outline_color), (0, 0))
    outline_surface.blit(font.render(text, True, outline_color), (outline_width * 2, 0))
    outline_surface.blit(font.render(text, True, outline_color), (0, outline_width * 2))
    outline_surface.blit(font.render(text, True, outline_color), (outline_width * 2, outline_width * 2))

    # Draw the text surface in the center of the outline surface
    outline_surface.blit(text_surface, (outline_width, outline_width))

    # Get the rect of the outline surface and set its center
    outline_rect = outline_surface.get_rect(center=center)
    surface.blit(outline_surface, outline_rect)

    return outline_rect

def draw_box(surface, rect, color, border_color, border_width=2):
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, border_color, rect, border_width)

def game_over(tela, pontos):
    # Desenhar texto "Game Over" com contorno branco
    draw_text_centered(tela, "Game Over", FONTE_GAME_OVER, ORANGE, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150), outline_color=WHITE, outline_width=4)

    # Desenhar pontuação
    draw_text_centered(tela, f"Pontuação: {pontos}", FONTE_PONTOS, WHITE, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30))
    
    # Definir o retângulo para a caixa contendo a pontuação e o botão
    box_rect = pygame.Rect(SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 - 40, 240, 150)
    
    # # Desenhar a caixa transparente
    # s = pygame.Surface((240, 150))  # the size of your rect
    # s.set_alpha(128)  # alpha level
    # s.fill((255, 255, 255))  # this fills the entire surface
    # tela.blit(s, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 - 40))
    
    # Desenhar botão "Jogar Novamente" quadrado, vermelho com borda branca
    botao_rect = pygame.Rect(SCREEN_WIDTH / 2 - 60, SCREEN_HEIGHT / 2 + 30, 120, 30)
    draw_box(tela, botao_rect, RED, WHITE, border_width=4)
    draw_text_centered(tela, "Jogar", FONTE_BOTAO, WHITE, botao_rect.center)

    pygame.display.update()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_over_button = botao_rect.collidepoint(mouse_pos)

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN and mouse_over_button:
                return


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load("background-day.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.init()
jump_sound = pygame.mixer.Sound("passaro-voando.ogg")
point_sound = pygame.mixer.Sound("pontos.ogg")
die_sound = pygame.mixer.Sound("som-da-morte.ogg")

def start_game():
    global bird_group, pipe_group, ground_group

    bird_group = pygame.sprite.Group()
    bird = Bird()
    bird_group.add(bird)

    ground_group = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(GROUND_WIDTH * i)
        ground_group.add(ground)

    pipe_group = pygame.sprite.Group()
    previous_pipe_height = None
    for i in range(2):
        pipes, previous_pipe_height = get_random_pipes(SCREEN_WIDTH * i + 800, previous_pipe_height)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    pontos = 0
    passed_pipe_set = False
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bird.bump()
                    jump_sound.play()

        screen.blit(BACKGROUND, (0, 0))

        if is_off_screen(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDTH - 20)
            ground_group.add(new_ground)

        if is_off_screen(pipe_group.sprites()[0]):
            pipe_group.remove(pipe_group.sprites()[0])
            pipe_group.remove(pipe_group.sprites()[0])
            pipes, previous_pipe_height = get_random_pipes(SCREEN_WIDTH * 2, previous_pipe_height)
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])

        bird_group.update()
        ground_group.update()
        pipe_group.update()

        if (
            pygame.sprite.groupcollide(
                bird_group, ground_group, False, False, pygame.sprite.collide_mask
            )
            or pygame.sprite.groupcollide(
                bird_group, pipe_group, False, False, pygame.sprite.collide_mask
            )
        ):
            die_sound.play()
            desenhar_tela(screen, pontos)  # Desenhar a tela antes de exibir o "Game Over"
            game_over(screen, pontos)
            return

        for cano in pipe_group:
            if not cano.passed and bird.rect.right > cano.rect.left:
                cano.passed = True
                if not passed_pipe_set:
                    pontos += 1
                    point_sound.play()
                    passed_pipe_set = True

        for cano in pipe_group:
            if cano.rect.right < 0:
                pipe_group.remove(cano)
                passed_pipe_set = False

        if len(pipe_group) < 2:
            pipes, previous_pipe_height = get_random_pipes(SCREEN_WIDTH * 2, previous_pipe_height)
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])

        desenhar_tela(screen, pontos)

while True:
    start_game()



