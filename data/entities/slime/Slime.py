import pygame
import math
import random

from scripts.particle import Particle
from scripts.entities import MeleeEnemy

from scripts.particle import Particle
import random

class Slime(MeleeEnemy):
    E_TYPE = 'slime'

    BASE_HP = 20
    XP_REWARD = 20
    RESISTANCES = {'slashing': 0.8, 'piercing': 0.8, 'blunt': 1.4}

    SPEED = 0.6
    CHASE_RANGE = 100
    ATTACK_RANGE = 24

    BASE_ATTACK_DAMAGE = 20
    DAMAGE_TYPE = 'poison'


    WINDUP_FRAMES = 30
    RECOVERY_FRAMES = 30
    ATTACK_IMPACT_FRAME = 6
    
    ATTACK_HIT_RADIUS = 40

    LOOT_TABLE = [ 
        {"item_id": "weak_mana_potion", "chance": 0.1},
        {"item_id": "slime_ball", "chance": 0.5}
    ]

    def __init__(self, game, pos, size, e_type=None, level=1):
        super().__init__(game, pos, size, e_type=e_type, level=level)


        self.action_offsets.update({
            "idle": (0, 0),
            "run":  (0, 0),
            "attack": (0, 0),
            "jump": (0, 0),
        })
        self.WINDUP_FRAMES = self.WINDUP_FRAMES - (level * self.WINDUP_SCALE_PER_LEVEL)
        print(self.WINDUP_FRAMES)
        
        self.set_action(self.action)

    def on_death(self):
        super().on_death()
        for i in range(20):
            self.game.particles.append(
                Particle(self.game, 'particle', self.rect().center,
                         velocity=[random.random() * 4 - 2, random.random() * -3],
                         frame=random.randint(0, 7))
            )
    
