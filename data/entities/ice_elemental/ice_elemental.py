import math
from scripts.entities import ShooterEnemy
from scripts.particle import Particle
import random

class IceElemental(ShooterEnemy):
    E_TYPE = 'ice_elemental'
    BASE_HP = 600
    XP_REWARD = 600
    RESISTANCES = {'piercing': 0.6, 'blunt': 1.2, 'slashing': 0.6, 'ice': 0.2, 'fire': 1.3}
    SPEED = 0.6
    BASE_ATTACK_DAMAGE = 60
    DAMAGE_TYPE = 'ice'

    ATTACK_COOLDOWN_TIME = 200
    ATTACK_WINDUP = 120
    SHOOT_FRAME = 10
    CHASE_RANGE = 250
    ATTACK_RANGE = 160

    PROJECTILE_SPEED = 6

    LOOT_TABLE = [
        {"item_id": "ice_shards", "chance": 1},
    ]

    def __init__(self, game, pos, size, level=1):
        super().__init__(game, pos, size, e_type=self.E_TYPE, level=level)

    def attack(self):
        player_pos = self.game.player.rect().center
        enemy_pos = self.rect().center
        
        angle = math.atan2(player_pos[1] - enemy_pos[1], player_pos[0] - enemy_pos[0])
        velocity = [math.cos(angle) * self.PROJECTILE_SPEED, math.sin(angle) * self.PROJECTILE_SPEED]
        
        self.game.projectiles.append({
            'type': 'ice',
            'pos': list(enemy_pos),
            'velocity': velocity,
            'timer': 240,
            'damage': self.attack_damage,
            'damage_type': self.damage_type,
            'asset': 'ice'
        })

    def on_death(self):
        super().on_death()
        for i in range(20):
            self.game.particles.append(
                Particle(self.game, 'particle', self.rect().center,
                         velocity=[random.random() * 4 - 2, random.random() * -3],
                         frame=random.randint(0, 7))
            )

