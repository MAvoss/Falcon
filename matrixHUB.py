import pygame
import random
import requests
# Initialize Pygame
pygame.init()
# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
# Set up the font
font_size = 24
font = pygame.font.Font(None, font_size)
# Make a GET request to the GitHub API URL
response = requests.get('https://api.github.com/repos/MAvoss/Falcon/commits')
# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    # Extract the commit messages
    commit_messages = [commit['commit']['message'] for commit in json_data]

    # Use the commit messages as your source for the text
    source_text = '\n'.join(commit_messages)
else:
    # Handle the error case
    print('Error: Failed to retrieve data from GitHub API')
# Split the text into lines
lines = text.split("\n")
# Create a list to hold the text surfaces and their positions
text_surfaces = []
text_positions = []
# Create a vertical offset for each line of text
vertical_offset = 0

# Loop through the lines of text
for line in lines:
    # Render the text surface
    text_surface = font.render(line, True, (255, 255, 255))
    # Rotate the text surface
    text_surface = pygame.transform.rotate(text_surface, 90)
    # Choose a random speed for the text
    speed = random.randint(1, 5)
    # Calculate the initial position of the text surface
    x = random.randint(0, screen_width - text_surface.get_width())
    y = -text_surface.get_height() - vertical_offset
    # Add the text surface and position to the lists
    text_surfaces.append(text_surface)
    text_positions.append((x, y, speed))
    # Increase the vertical offset for the next line of text
    vertical_offset += font_size * 2
# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((0, 0, 0))
    # Loop through the text surfaces and their positions
    for i in range(len(text_surfaces)):
        # Get the current position and speed of the text
        x, y, speed = text_positions[i]
        
        # Update the position of the text based on its speed
        y += speed
        
        # If the text has moved off the bottom of the screen, reset its position
        if y > screen_height:
            y = -text_surfaces[i].get_width()
            x = random.randint(0, screen_width - text_surface.get_width())
        
        # Check if the current text surface overlaps with any of the others
        overlapping = False
        for j in range(i):
            if text_positions[j][1] + text_surfaces[j].get_width() > y and y + text_surfaces[i].get_width() > text_positions[j][1]:
                overlapping = True
                break
        
        # If the text does not overlap with any others, blit it to the screen
        if not overlapping:
            screen.blit(text_surfaces[i], (x, y))
        
        # Update the position of the text in the list
        text_positions[i] = (x, y, speed)
    
    # Update the screen
    pygame.display.flip()
    
    # Wait for the next frame
    clock.tick(60)

# Clean up
pygame.quit()
