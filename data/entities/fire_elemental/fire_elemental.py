import math
from scripts.entities import ShooterEnemy
from scripts.particle import Particle
import random

class FireElemental(ShooterEnemy):
    E_TYPE = 'fire_elemental'
    BASE_HP = 200
    XP_REWARD = 200
    RESISTANCES = {'piercing': 0.8, 'blunt': 1.0, 'slashing': 0.8, 'ice': 1.5}
    SPEED = 0.8
    BASE_ATTACK_DAMAGE = 40
    DAMAGE_TYPE = 'fire'

    CHASE_RANGE = 250
    ATTACK_RANGE = 160

    ATTACK_COOLDOWN_TIME = 300
    ATTACK_WINDUP = 120
    SHOOT_FRAME = 12

    JUMP_STRENGTH_2 = 3.5

    PROJECTILE_SPEED = 3.5

    LOOT_TABLE = [
        {"item_id": "fire_shards", "chance": 0.6},
    ]

    def __init__(self, game, pos, size, level=1):
        super().__init__(game, pos, size, e_type=self.E_TYPE, level=level)

    def attack(self):
        player_pos = self.game.player.rect().center
        enemy_pos = self.rect().center
        
        angle = math.atan2(player_pos[1] - enemy_pos[1], player_pos[0] - enemy_pos[0])
        velocity = [math.cos(angle) * self.PROJECTILE_SPEED, math.sin(angle) * self.PROJECTILE_SPEED]
        
        self.game.projectiles.append({
            'type': 'fire',
            'pos': list(enemy_pos),
            'velocity': velocity,
            'timer': 240,
            'damage': self.attack_damage,
            'damage_type': self.damage_type,
            'asset': 'fire'
        })

    def on_death(self):
        super().on_death()
        for i in range(20):
            self.game.particles.append(
                Particle(self.game, 'particle', self.rect().center,
                         velocity=[random.random() * 4 - 2, random.random() * -3],
                         frame=random.randint(0, 7))
            )

