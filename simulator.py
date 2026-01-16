# Payoff matrix
def payoff(move_a, move_b):
    if move_a == "C" and move_b == "C":
        return 3, 3
    elif move_a == "C" and move_b == "D":
        return 0, 5
    elif move_a == "D" and move_b == "C":
        return 5, 0
    else:
        return 1, 1


def simulate(strategy_a, strategy_b, rounds):
    history_a = []
    history_b = []

    score_a = 0
    score_b = 0

    for _ in range(rounds):
        move_a = strategy_a(history_b)
        move_b = strategy_b(history_a)

        a, b = payoff(move_a, move_b)

        score_a += a
        score_b += b

        history_a.append(move_a)
        history_b.append(move_b)

    return {
        "score_a": score_a,
        "score_b": score_b,
        "history_a": history_a,
        "history_b": history_b
    }
