from strategies import (
    always_cooperate,
    always_defect,
    tit_for_tat,
    random_strategy
)
from simulator import simulate

strategies = {
    "1": ("Always Cooperate", always_cooperate),
    "2": ("Always Defect", always_defect),
    "3": ("Tit for Tat", tit_for_tat),
    "4": ("Random", random_strategy)
}

print("\nPrisoner's Dilemma Simulator\n")

print("Choose Strategy A:")
for k, v in strategies.items():
    print(f"{k}. {v[0]}")
choice_a = input("Enter choice: ")

print("\nChoose Strategy B:")
for k, v in strategies.items():
    print(f"{k}. {v[0]}")
choice_b = input("Enter choice: ")

rounds = int(input("\nEnter number of rounds: "))

name_a, strategy_a = strategies[choice_a]
name_b, strategy_b = strategies[choice_b]

result = simulate(strategy_a, strategy_b, rounds)

print("\n--- RESULTS ---")
print(f"Strategy A: {name_a}")
print(f"Strategy B: {name_b}")
print(f"Rounds Played: {rounds}\n")

print(f"Final Score A: {result['score_a']}")
print(f"Final Score B: {result['score_b']}")

if result["score_a"] > result["score_b"]:
    print("Winner: Strategy A")
elif result["score_b"] > result["score_a"]:
    print("Winner: Strategy B")
else:
    print("Result: Draw")

coop_rate_a = result["history_a"].count("C") / rounds * 100
coop_rate_b = result["history_b"].count("C") / rounds * 100

print(f"\nCooperation Rate A: {coop_rate_a:.2f}%")
print(f"Cooperation Rate B: {coop_rate_b:.2f}%")
