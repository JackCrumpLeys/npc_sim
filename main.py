from enum import Enum
import random

import names


class gender(Enum):
    male = 'male'
    female = 'female'


class simulation:
    def __init__(self):
        self.npcs = generate_npcs(20)


class npc:
    def __init__(self, name=None, _gender=gender.male):
        if name is None:
            name = names.get_full_name(_gender)
        self.relationship = None
        self.name = name
        self.gender = _gender

    def update(self, _simulation: simulation):
        print(f"updating npc: {self.name}")
        single_npcs = get_single_combatible_npcs(_simulation, self.gender)
        if self.relationship is None and bool(random.getrandbits(1)) and len(single_npcs) != 0:
            for n in single_npcs:
                if random.randint(1, 100) >= 95:
                    self.relationship = n
                    n.relationship = self
                    print(f"{self.name}: starting relationship with {n.name}")
                    break
        if random.randint(1, 100) >= 98 and self.relationship is not None:
            print(f"{self.name}: making baby...")
            _simulation.npcs.append(npc())


def get_single_combatible_npcs(_simulation, _gender):
    single_npcs = []
    for n in _simulation.npcs:
        if n.relationship is None and n.gender != _gender:
            single_npcs.append(n)
    return single_npcs


def generate_npcs(amount):
    npcs = []
    for i in range(amount):
        npcs.append(npc(_gender=[e.value for e in gender][random.randint(0, 1)]))
    return npcs


def build():
    return simulation()


def update(_tick, _simulation):
    print(f"running update, tick: {_tick}")
    for n in _simulation.npcs:
        n.update(_simulation)
    return _tick < 100


if __name__ == '__main__':
    tick = 0
    print("builing for first tick.")
    simulation = build()
    running = True
    while running:
        running = update(tick, simulation)
        tick += 1
    print(len(simulation.npcs))
