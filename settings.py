import pygame

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 16)


width, height = 400, 400
screen = pygame.display.set_mode((width, height))

step = 40

# TRUCK SETTINGS

# garbage truck params
# truck location x and y
x = 0
y = 0
# height and width of the truck
car_width = 40
car_height = 40
# Truck image
# car = pygame.image.load('resources/car.png')
# car = pygame.transform.scale(car, (car_width, car_height))


car_n = pygame.image.load('resources/car_n.png')
car_s = pygame.image.load('resources/car_s.png')
car_e = pygame.image.load('resources/car_e.png')
car_w = pygame.image.load('resources/car_w.png')

car_s = pygame.transform.scale(car_s, (car_width, car_height))
car_n = pygame.transform.scale(car_n, (car_width, car_height))
car_e = pygame.transform.scale(car_e, (car_width, car_height))
car_w = pygame.transform.scale(car_w, (car_width, car_height))

global truck_capacity
global max_capacity
truck_capacity = 0
max_capacity = 8

capacity_options = []
for cap in range(20):
    capacity_options.append(cap + 1)

# Kierunek smieciari
global direction
direction = 'S'

# Budynek

building = pygame.image.load('resources/building.png')
building = pygame.transform.scale(building, (car_width, car_height))



# ustawienia smieci

# plastiki, szkło, papier, mieszane
# dzień wywożenia śmieci - każdy typ w osobne dni
# czy kontener ze śmieciami jest pełny czy pusty

trash_types = [
    'plastic',
    'glass',
    'municipal',
    'paper',
]

trash_fillings = [
    'empty',
    'half',
    'full',
]

can_red = pygame.image.load('resources/trash_red.png')
can_red = pygame.transform.scale(can_red, (car_width, car_height))

can_green = pygame.image.load('resources/trash_green.png')
can_green = pygame.transform.scale(can_green, (car_width, car_height))

can_yellow = pygame.image.load('resources/trash_yellow.png')
can_yellow = pygame.transform.scale(can_yellow, (car_width, car_height))



# dni
days = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]


schedule = {
    'monday': ['glass', 'municipal', ],
    'tuesday': ['municipal', 'plastic', ],
    'wednesday': ['paper', 'glass', ],
    'thursday': ['plastic', 'glass', ],
    'friday': ['glass', 'municipal'],
    'saturday': ['paper', 'plastic'],
    'sunday': ['glass', ],
}
