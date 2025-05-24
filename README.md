# A* Puzzle Solver

This Python project implements the **A\*** (A-star) search algorithm to solve the classic **NxN sliding tile puzzle**, also known as the N-puzzle. The solver finds the shortest sequence of legal moves to transform a given start state into a specified goal state using the A\* algorithm and **Manhattan distance** as the heuristic.

---

## 🧠 Algorithm Overview

- **A\* Search** is used to explore the most promising paths by combining:
  - `g(n)`: the cost to reach the current node.
  - `h(n)`: estimated cost to reach the goal (heuristic, Manhattan distance here).
- It prioritizes paths with the lowest combined cost: `f(n) = g(n) + h(n)`.
- The board is represented as a 1D list.

---

## 📁 File Structure

### `astar_solver.py`
Contains the main A* logic and utility functions:
- `legal_moves`: Calculates valid moves based on 0’s position.
- `generate_child`: Generates valid children (next states) from a given state.
- `manhattan`: Heuristic function using Manhattan distance.
- `f(g, h)`: State evaluation function.
- `astar`: A* algorithm implementation.
- `find_path`: Extracts the sequence of steps that lead to the goal.

### `astar_puzzle.py`
Handles the input/output and visualization of the solution.
- Accepts user input for start and goal state.
- Calls `astar` to find the solution.
- Prints each move and the resulting puzzle state step-by-step.

📌 **Note:** `astar_puzzle.py` must be in the **same folder** as `astar_solver.py`.

---

## 🖥️ How to Run

1. Place `astar_solver.py` and `astar_puzzle.py` in the same directory.
2. Run `astar_puzzle.py` in a Python environment:
   ```bash
   python astar_puzzle.py
3. Follow the on-screen prompts to:

Enter the puzzle size n (e.g., 3 for 8-puzzle).
Input the initial and goal states row-by-row.

Enter size of tile puzzle (integer greater that 0): 3  

Enter start state row by row (numbers delimited by white space):   
Enter Start state: row 1 : 1 2 3  
Enter Start state: row 2 : 4 0 6   
Enter Start state: row 3 : 7 5 8  

Enter goal state row by row (numbers delimited by white space):   
Enter Goal state: row 1 : 1 2 3  
Enter Goal state: row 2 : 4 5 6  
Enter Goal state: row 3 : 7 8 0  

## 📦 Requirements
Only built-in Python libraries are used.
No external installation required.

## 👨‍💻 Author
Ioannis Mastoras  
Created: 4 April 2020  

📜 License
This project is shared for educational purposes. Feel free to use or modify the code, but please credit the original author.
