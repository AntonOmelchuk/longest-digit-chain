# Graph-Based Sequence-Linking Puzzle Solver

An optimized Python solver designed to find the longest valid fragment-linking chain for sequence puzzles using depth-first search (DFS), backtracking, and a greedy adjacency heuristic.

## 🚀 Features

- **Optimized Graph Construction:** Builds an efficient prefix-indexed adjacency list in $O(N)$ time, skipping self-references.
- **Greedy Heuristic Sorting:** Sorts neighbor lists by branch count to explore high-probability paths first.
- **DFS with Backtracking:** Employs an $O(1)$ boolean `visited` state array for rapid state lookups during deep recursion.
- **Live Progress Visualization:** Real-time terminal progress bar and execution timers for monitoring workflow stages.
- **Precision Formatting:** Outputs the final result as a continuous concatenated string while safely preserving leading zeros.

## 🛠️ Requirements & Installation

No external third-party dependencies are required—the script relies entirely on Python's standard library (`collections`, `time`).

## ⚙️ How to Run

1. Place your input fragments in a file named `data.txt` in the root directory.
2. Run the solver script:

```bash
python main.py
