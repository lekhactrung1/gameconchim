import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 30, 30  # Adjusted bird dimensions
PIPE_WIDTH = 75  # Increased pipe width
PIPE_HEIGHT = 500  # Default height
PIPE_GAP = 200  # Increased gap between pipes for better balance
PIPE_DISTANCE = 300  # Horizontal distance between pipes
GRAVITY = 0.5
BIRD_JUMP = -8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))  # Resize bird
pipe_img = pygame.image.load("pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))  # Resize pipe

# Font settings
font = pygame.font.SysFont(None, 40)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = BIRD_JUMP

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 350)  # Adjusted height to ensure logical placement
        self.top = self.height - PIPE_HEIGHT
        self.bottom = self.height + PIPE_GAP
        self.passed = False  # New attribute to check if the bird has passed the pipe

    def draw(self):
        screen.blit(pipe_img, (self.x, self.top))
        screen.blit(pipe_img, (self.x, self.bottom))

    def update(self):
        self.x -= 3

# Display start screen
def display_start_screen():
    screen.fill((135, 206, 235))  # Sky blue background
    text = font.render("Press any key to start", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Display score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game function
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(WIDTH + 100), Pipe(WIDTH + 100 + PIPE_DISTANCE)]
    running = True
    score = 0  # Initialize score

    # Show start screen before game begins
    display_start_screen()

    while running:
        clock.tick(30)  # Frame rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        bird.update()

        # Update pipes and check for score
        for pipe in pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                new_pipe = Pipe(WIDTH)
                pipes.append(new_pipe)

            # Check if bird has passed the pipe
            if not pipe.passed and bird.x > pipe.x + PIPE_WIDTH:
                pipe.passed = True
                score += 1  # Increase score when bird passes the pipe

        # Draw background and elements
        screen.fill((135, 206, 235))  # Sky blue color

        for pipe in pipes:
            pipe.draw()
        bird.draw()

        # Display score
        display_score(score)

        pygame.display.update()

        # Check for collisions
        for pipe in pipes:
            if bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.height + PIPE_GAP:
                    running = False

        if bird.y + BIRD_HEIGHT > HEIGHT:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 30, 30  # Adjusted bird dimensions
PIPE_WIDTH = 50  # Increased pipe width
PIPE_HEIGHT = 500  # Default height
PIPE_GAP = 200  # Increased gap between pipes for better balance
PIPE_DISTANCE = 300  # Horizontal distance between pipes
GRAVITY = 0.5
BIRD_JUMP = -8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))  # Resize bird
pipe_img = pygame.image.load("pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))  # Resize pipe

# Font settings
font = pygame.font.SysFont(None, 40)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = BIRD_JUMP

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 350)  # Adjusted height to ensure logical placement
        self.top = self.height - PIPE_HEIGHT
        self.bottom = self.height + PIPE_GAP
        self.passed = False  # New attribute to check if the bird has passed the pipe

    def draw(self):
        screen.blit(pipe_img, (self.x, self.top))
        screen.blit(pipe_img, (self.x, self.bottom))

    def update(self):
        self.x -= 3

# Display start screen
def display_start_screen():
    screen.fill((135, 206, 235))  # Sky blue background
    text = font.render("Press any key to start", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Display score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game function
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(WIDTH + 100), Pipe(WIDTH + 100 + PIPE_DISTANCE)]
    running = True
    score = 0  # Initialize score

    # Show start screen before game begins
    display_start_screen()

    while running:
        clock.tick(30)  # Frame rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        bird.update()

        # Update pipes and check for score
        for pipe in pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                new_pipe = Pipe(WIDTH)
                pipes.append(new_pipe)

            # Check if bird has passed the pipe
            if not pipe.passed and bird.x > pipe.x + PIPE_WIDTH:
                pipe.passed = True
                score += 1  # Increase score when bird passes the pipe

        # Draw background and elements
        screen.fill((135, 206, 235))  # Sky blue color

        for pipe in pipes:
            pipe.draw()
        bird.draw()

        # Display score
        display_score(score)

        pygame.display.update()

        # Check for collisions
        for pipe in pipes:
            if bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.height + PIPE_GAP:
                    running = False

        if bird.y + BIRD_HEIGHT > HEIGHT:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
