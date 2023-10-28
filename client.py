from ursina import *
from random import uniform

app = Ursina()

# Initialize the game level
ground = Entity(model='plane', scale=(100, 1, 100), color=color.green)
camera.position = (0, 5, -10)

# Aiming cursor
cursor = Entity(parent=camera.ui, model='quad', color=color.green, scale=.02)

# Generate some enemies (red cubes)
enemies = []
enemy_pool = []

for i in range(10):
    enemy = Entity(model='cube', color=color.red, scale=(0.5, 0.5, 0.5), enabled=False)
    enemy_pool.append(enemy)

def spawn_enemy():
    for enemy in enemy_pool:
        if not enemy.enabled:
            enemy.position = (uniform(-5, 5), 0.25, uniform(5, 20))
            enemy.enabled = True
            enemies.append(enemy)
            break

# Shooting logic
def input(key):
    if key == 'left mouse down':
        for enemy in enemies:
            if mouse.hovered_entity == enemy:
                enemy.enabled = False
                enemies.remove(enemy)
                break

# Move enemies towards the camera
def update():
    for enemy in enemies:
        enemy.z -= time.dt * 2
        if enemy.z < camera.z:
            enemy.enabled = False
            enemies.remove(enemy)

    if len(enemies) < 10:
        spawn_enemy()

app.run()
