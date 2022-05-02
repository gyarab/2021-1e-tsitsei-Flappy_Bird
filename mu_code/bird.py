import pgzrun
import random
import math

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 650

GAP = 200
GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3

game_over = Actor("game_over.png", (75, 200))
pause = Actor("pause.png", (75, 200))
bird = Actor("bird.png", (75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

pipe_top = Actor("pipe_2.png", anchor=("left", "bottom"), pos=(-100, 0))
pipe_bottom = Actor("pipe.png", anchor=("left", "top"), pos=(-100, 0))
music.play("music.wav")

f = False
time = 0
ttime = 0


def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)


def update_pipes():
    if bird.dead:
        return
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        bird.score += 1


def update_bird():
    global time, ttime
    uy = bird.vy
    bird.y += (uy + bird.vy) / 2
    bird.x = 75
    bird.vy += math.sqrt(time - ttime) * GRAVITY

    if not bird.dead:
        if bird.vy < -3:
            bird.image = "bird1.png"
        else:
            bird.image = "bird.png"

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        if not bird.dead:
            sounds.sound.play()
        bird.dead = True
        bird.image = "birddead.png"

    if not 0 < bird.y < HEIGHT + 12:
        if bird.dead == False:
            sounds.sound.play()
        bird.dead = True
        bird.image = "birddead.png"


def update():
    bird.y = min(bird.y, HEIGHT + 12)
    global time, ttime
    if f == True:
        return
    time = time + 0.05
    update_pipes()
    update_bird()


def on_key_down(key):
    global f, time, ttime
    if bird.dead == True:
        bird.dead = False
        bird.y = 200
        bird.score = 0
        bird.vy = 0
        time = 0
        ttime = 0
        reset_pipes()
        return
    if key == keys.ESCAPE:
        f ^= True
        return
    if not bird.dead and key == keys.SPACE:
        bird.vy = -FLAP_STRENGTH
        time = 0
        ttime = 0


def draw():
    screen.blit("background.png", (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(
        str(bird.score),
        color="white",
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1),
    )
    if f == True and bird.dead == False:
        pause.x = WIDTH / 2
        pause.y = HEIGHT / 3
        pause.draw()

    if bird.dead == True and f==False:
        game_over.x = WIDTH / 2
        game_over.y = HEIGHT / 3
        game_over.draw()


pgzrun.go()
