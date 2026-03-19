import math
from scripts.entities import ShooterEnemy
from scripts.particle import Particle
import random

class Spider(ShooterEnemy):
    E_TYPE = 'spider'
    BASE_HP = 25
    XP_REWARD = 40
    RESISTANCES = {'piercing': 0.8, 'blunt': 1.2, 'slashing': 1.2}
    SPEED = 0.6
    
    BASE_ATTACK_DAMAGE = 10
    DAMAGE_TYPE = 'poison'


    ATTACK_COOLDOWN_TIME = 300
    ATTACK_WINDUP = 120
    SHOOT_FRAME = 8

    PROJECTILE_SPEED = 3.0

    LOOT_TABLE = [
        {"item_id": "weak_health_potion", "chance": 0.1},
        {"item_id": "spider_legs", "chance": 0.5}
    ]

    def __init__(self, game, pos, size, e_type=None, level=1):
        super().__init__(game, pos, size, e_type=e_type, level=level)

    def attack(self):
        player_pos = self.game.player.rect().center
        enemy_pos = self.rect().center
        
        angle = math.atan2(player_pos[1] - enemy_pos[1], player_pos[0] - enemy_pos[0])
        velocity = [math.cos(angle) * self.PROJECTILE_SPEED, math.sin(angle) * self.PROJECTILE_SPEED]
        
        self.game.projectiles.append({
            'type': 'web',
            'pos': list(enemy_pos),
            'velocity': velocity,
            'timer': 240,
            'damage': self.attack_damage,
            'damage_type': self.damage_type,
            'asset': 'web'
        })

    def on_death(self):
        super().on_death()
        for i in range(20):
            self.game.particles.append(
                Particle(self.game, 'particle', self.rect().center,
                         velocity=[random.random() * 4 - 2, random.random() * -3],
                         frame=random.randint(0, 7))
            )

