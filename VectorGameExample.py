import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the clock
clock = pygame.time.Clock()

# Define the object's position and velocity vectors
pos = pygame.math.Vector2(screen_width/2, screen_height/2) #sets the position of the ball in the middle of the screen
vel = pygame.math.Vector2(0, 0)

# Define the object's speed and acceleration
speed = 5
acceleration = 0.5

# Define a function to update the object's position and velocity
def update_position(vel, pos):
    
    # Apply acceleration to the velocity vector
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vel += pygame.math.Vector2(0, -acceleration) # you might be confused why this is negative
    if keys[pygame.K_DOWN]:                          # since y position is 0 at the top of the screen instead of the bottom, it will be opposite
        vel += pygame.math.Vector2(0, acceleration)  # this is different from what you have learned in math classes so far
    if keys[pygame.K_LEFT]:
        vel += pygame.math.Vector2(-acceleration, 0)
    if keys[pygame.K_RIGHT]:
        vel += pygame.math.Vector2(acceleration, 0)
    
    # Limit the speed of the velocity vector so it doesnt go at infinite speed, this is how it works in a lot of games too
    if vel.length() > speed:
        vel.scale_to_length(speed)
    
    # Update the position vector based on the velocity vector
    pos += vel

# Define a function to draw the object on the screen
def draw_object():
    # Draw a circle at the object's position
    pygame.draw.circle(screen, (255, 255, 255), (int(pos.x), int(pos.y)), 20)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Update the object's position and velocity
    update_position(vel, pos)
    
    # Draw the object on the screen
    draw_object()
    
    # Update the display
    pygame.display.update()
    
    # Limit the frame rate
    clock.tick(60)
