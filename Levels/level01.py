from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# App/Window
app = Ursina()

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Jump Block Class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Speed Block Class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 8),
            color = "#53FFF5",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Slow Block Class
class SlowBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 15),
            color = "#FF453F",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Player
player = FirstPersonController()
player.speed = 6
player.jump_height = 4

# Sky
sky = Sky(texture = "../assets/sky")

# Lighting
light = PointLight(parent = camera, position = (0, 1.1, -1.5))
light.color = color.white

AmbientLight(color = color.rgba(100, 100, 100, 0.1))

#Level01

block_1 = NormalBlock(position = (0, 1, 9))
block_1_1 = NormalBlock(position = (0, 2, 14))
block_1_2 = NormalBlock(position = (0, 3, 19))
block_1_3 = NormalBlock(position = (0, 4, 24))
block_1_4 = NormalBlock(position = (5, 5, 24))
block_1_5 = NormalBlock(position = (10, 6, 24))
block_1_6 = JumpBlock(position = (17, 2, 24))
block_1_7 = NormalBlock(position = (25, 10, 24))
block_1_8 = SpeedBlock(position = (25, 10, 33))

ground_1 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
finishBlock_1 = Entity(model = "cube", scale_x = 5, scale_z = 5, collider = "box", texture = "white_cube", color = "#CACACA", position = (25, 10, 45))

def speed():
    player.speed = 6

def update():
    # Escape button quits
    if held_keys["escape"]:
        application.quit()

    # Stops the player from falling forever
    if player.position.y <= -50:
        player.position = Vec3(0, 20, 0)
        player.speed = 6
        player.jump_height = 4

    # Restart the level
    if held_keys["g"]:
        player.position = Vec3(0, 0, 0)
        player.speed = 6
        player.jump_height = 4

    # What entity the player hits
    hit = raycast(player.position, player.down, distance=2, ignore=[player,])
    
    if hit.entity == block_1_6:
        player.jump_height = 20
    elif hit.entity != block_1_6:
        player.jump_height = 4

    if hit.entity == block_1_8:
        player.speed = 20
        invoke(speed, delay=3)

app.run()
