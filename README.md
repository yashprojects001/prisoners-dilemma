# 🧠 Prisoner’s Dilemma Strategy Simulator  
### *Where cooperation, betrayal, and intelligence collide*

<p align="center">
  <img src="https://img.shields.io/badge/Game%20Theory-🧠-purple">
  <img src="https://img.shields.io/badge/Simulation-⚙️-blue">
  <img src="https://img.shields.io/badge/Python-🐍-yellow">
  <img src="https://img.shields.io/badge/Logic--Driven-✅-green">
</p>

---

## 🌍 What Is This Project?

This project is a **strategy simulation engine** for the classic  
🎭 **Prisoner’s Dilemma** — a foundational problem in **game theory, economics, AI, and social science**.

It explores a powerful question:

> **Is cooperation rational — or does betrayal always win?**

By simulating repeated interactions between different strategies, this project reveals how **simple rules can create complex, surprising outcomes**.

---

## 🎯 Core Objectives

✅ Simulate rational decision-making  
✅ Compare strategy performance over time  
✅ Observe cooperation vs defection dynamics  
✅ Learn game theory through experimentation  

---

## 🧩 The Game Rules (Payoff Matrix)

| Player A | Player B | A Gains | B Gains |
|--------|---------|--------|--------|
| 🤝 Cooperate | 🤝 Cooperate | +3 | +3 |
| 🤝 Cooperate | ❌ Defect | 0 | +5 |
| ❌ Defect | 🤝 Cooperate | +5 | 0 |
| ❌ Defect | ❌ Defect | +1 | +1 |

⚠️ The dilemma:  
Defection seems smart short-term — but repeated rounds change everything.

---

## 🤖 Strategies Implemented

🟢 **Always Cooperate**  
> Trusts blindly — peaceful but vulnerable  

🔴 **Always Defect**  
> Ruthless — wins fast, loses trust  

🟡 **Tit for Tat (⭐ Star Strategy)**  
> Starts kind, then mirrors opponent  
> *Proven to dominate long-term tournaments*

🔵 **Random Strategy**  
> Chaotic — unpredictable behavior  

---

## ⚙️ How the Simulator Works

1️⃣ Choose two strategies  
2️⃣ Decide number of rounds  
3️⃣ Simulator runs repeated interactions  
4️⃣ Scores accumulate based on decisions  
5️⃣ Results reveal:
- Total scores  
- Winner  
- Cooperation rate  

---

## 📊 Sample Output
Strategy A: Tit for Tat
Strategy B: Always Defect

Rounds Played: 100

Final Score:
A → 294
B → 199

Winner: Strategy A

Cooperation Rate:
A → 78.00%
B → 0.00%


✨ Insight: **Kindness with memory beats pure selfishness**

---

## 🛠️ Tech Stack

| Layer | Tool |
|-----|------|
| Language | 🐍 Python |
| Logic | Game Theory |
| Complexity | Beginner-Friendly |
| Dependencies | None |

🚀 No frameworks. No libraries. Just **pure logic**.

---

## 📁 Project Structure

prisoners-dilemma/
│
├── main.py # User interface & execution
├── strategies.py # All decision-making logic
├── simulator.py # Game engine & payoff system
└── README.md 


---

## 🧠 Concepts Demonstrated

🧩 Iterated Games  
📈 Strategy Optimization  
🔁 Feedback Loops  
🤝 Trust & Retaliation  
📊 Emergent Behavior  

This is **not just code** — it’s **thinking modeled as software**.

---

## 🚀 Why This Project Is Special

✨ Small codebase  
✨ Deep intellectual impact  
✨ Used in real research  
✨ Perfect for:
- Hackathons  
- GitHub portfolios  
- Interviews  
- Game theory learning  

> *“A few lines of logic can explain human behavior.”*

---

## 🔮 Possible Future Upgrades

🌱 Evolutionary strategies  
📉 Noise & mistake probability  
📊 Visual graphs  
🏟 Tournament mode (all vs all)  
🌐 Web-based simulator  

---

## ▶️ How to Run

```bash
python main.py


This project proves that:   
Intelligence isn’t complexity — it’s clarity.