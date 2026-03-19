import pygame
import math
import random

from scripts.particle import Particle
from scripts.entities import MeleeEnemy

from scripts.particle import Particle
import random

class Wolf(MeleeEnemy):
    E_TYPE = 'wolf'

    BASE_HP = 1
    XP_REWARD = 25
    RESISTANCES = {'slashing': 1.2, 'piercing': 1.0}

    SPEED = 1.2
    CHASE_RANGE = 100
    ATTACK_RANGE = 24

    BASE_ATTACK_DAMAGE = 15
    DAMAGE_TYPE = 'slashing'

    WINDUP_FRAMES = 30
    RECOVERY_FRAMES = 60
    ATTACK_IMPACT_FRAME = 4

    LOOT_TABLE = [
        {'item_id': 'short_sword', 'chance': 1},
        {'item_id': 'apprentice_staff', 'chance': 1}
    ]

    def on_death(self):
        super().on_death()
        for i in range(20):
            self.game.particles.append(
                Particle(self.game, 'particle', self.rect().center,
                         velocity=[random.random() * 4 - 2, random.random() * -3],
                         frame=random.randint(0, 7))
            )
    
