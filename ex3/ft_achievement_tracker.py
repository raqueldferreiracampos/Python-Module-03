import random


def gen_player_achievements() -> set:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
    nbr_achi = random.randint(2, 7)
    random_achi = random.sample(achievements, nbr_achi)
    return set(random_achi)


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    achievements = set(['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'])
    only_alice = set.difference(alice, bob, dylan, charlie)
    only_bob = set.difference(bob, alice, charlie, dylan)
    only_charlie = set.difference(charlie, alice, bob, dylan)
    only_dylan = set.difference(dylan, alice, bob, charlie)
    missing_alice = set.difference(achievements, alice)
    missing_bob = set.difference(achievements, bob)
    missing_charlie = set.difference(achievements, charlie)
    missing_dylan = set.difference(achievements, dylan)
    all_achi = set.union(alice, bob, charlie, dylan)
    common_achi = set.intersection(alice, bob, charlie, dylan)

    print("=== Achievement Tracker System ===")
    print()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {all_achi}")
    print()
    print(f"Common achievements: {common_achi}")
    print()
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()
    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")    
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")


if __name__ == "__main__":
    main()
