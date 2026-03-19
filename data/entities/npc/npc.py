from scripts.entities import PhysicsEntity

class NPC(PhysicsEntity):
    def __init__(self, game, pos, size, dialogue_id, npc_type="old_man", animation='idle'):
        super().__init__(game, f"npc/{npc_type}", pos, size)
        self.dialogue_id = dialogue_id

        self.action_offsets = {
            "idle": (0, 0),
        }

        self.set_action(animation)

    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)

