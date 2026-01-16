import random

# Always cooperates
def always_cooperate(opponent_history):
    return "C"

# Always defects
def always_defect(opponent_history):
    return "D"

# Tit for Tat strategy
def tit_for_tat(opponent_history):
    if not opponent_history:
        return "C"
    return opponent_history[-1]

# Random strategy
def random_strategy(opponent_history):
    return random.choice(["C", "D"])
