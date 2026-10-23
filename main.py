from collections import defaultdict
import time


def load_data(filename: str) -> list[str]:
    """
    Load data from file
    """
    print(f"📂 Loading data from '{filename}'...")
    with open(filename, 'r') as f:
        content = f.read()

    raw_data = content.split()
    print(f"✅ Successfully loaded {len(raw_data)} fragments.")

    return raw_data


def build_graph(fragments: list[str]) -> list[list[int]]:
    """
    Creates dict where:
    key: first two digits of fragment
    value: list of fragments idx that start with these digits
    Ex: If chain needs '92' - can easy find it by using by_prefix['92']
    """
    print("⚙️ Building prefix index...")
    by_prefix = defaultdict(list)
    for idx, fragment in enumerate(fragments):
        by_prefix[fragment[:2]].append(idx)


    """
    Creates adjacency list for all fragments
    For each fragment take last 2 digits (suffix) and use 
    prefix idx to find all valid next options excluding self-references
    Ex: 1st fragment (0 idx) has sufix '17', fragment with prefix '17'
        has idx - 37, so in adjacency_list for first fragment we save
        this idx 37 as potential next fragment  
    """
    print("🔗 Building adjacency list (excluding self-references)...")
    adjacency_list = []
    for idx, fragment in enumerate(fragments):
        suffix = fragment[-2:]
        valid_options = by_prefix[suffix]
        not_self_reference = [i for i in valid_options if i != idx]
        adjacency_list.append(not_self_reference)

    """
    Sort adjacency list
    For each fragment sort its next candidate in 
    desc order based on number of their own outgoing branches 
    Ex: If adjacency_list[5] has options [12, 3, 45] with 2, 0, and 5 outgoing 
      branches respectively, sort them to [45, 12, 3] so 
      the algorithm explores the most promising branch first
    """
    print("⚡ Sorting adjacency list...")
    for i in range(len(fragments)):
        adjacency_list[i].sort(key=lambda j: len(adjacency_list[j]), reverse=True)

    print("✅ Graph successfully built.")

    return adjacency_list


def find_longest_chain(adjacency_list: list[list[int]], fragments: list[str]):
    """
    Finds the longest valid chain of fragments using DFS with backtracking

    How it works:
       - For each state, updates `best_path` if current path length exceeds it
       - Iterates through sorted neighbors (`adjacency_list[current_idx]`)
       - If a neighbor is not visited:
         * Marks it visited (`visited[next_idx] = True`)
         * Appends to path (`path.append(next_idx)`)
         * Recurses deeper (`dfs(next_idx, path)`)
         * Backtracks (`path.pop()`, `visited[next_idx] = False`) to explore other branches

    Ex:
       If graph has edges: 0 -> [1], 1 -> [2], 2 -> []
       - Starts at 0: path = [0], best_path = [0]
       - Moves to 1: path = [0, 1], best_path = [0, 1]
       - Moves to 2: path = [0, 1, 2], best_path = [0, 1, 2]
       - Backtracks step-by-step via pop() and un-visits elements to check other starts
    """
    n = len(fragments)
    best_path = []
    visited = [False] * n # boolean array tracking active path elements

    print(f"🚀 Starting DFS search across {n} possible start nodes...")

    def dfs(current_idx, path):
        nonlocal best_path

        if (len(path)) > len(best_path):
            best_path = list(path)
            print(f"\nℹ️New best chain length found: {len(best_path)} fragments")

        for next_idx in adjacency_list[current_idx]:
            if not visited[next_idx]:
                visited[next_idx] = True
                path.append(next_idx)
                dfs(next_idx, path)
                path.pop()
                visited[next_idx] = False

    for start_idx in range(n):
        progress = (start_idx + 1) / n
        bar_length = 20
        filled_length = int(bar_length * progress)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)

        print(f"\r[{bar}] {progress * 100:.1f}% | Start {start_idx + 1}/{n} (fragment: {fragments[start_idx]})")
        visited[start_idx] = True
        dfs(start_idx, [start_idx])
        visited[start_idx] = False

    print(f"✅ Search completed! Longest chain length: {len(best_path)}")
    return best_path


if __name__ == "__main__":
    total_start = time.time()

    # 1. Load data from file
    filename = "data.txt"
    fragments = load_data(filename)

    # 2. Build graph
    adjacency_list = build_graph(fragments)

    # 3. Searching the longest chain (return list with idx)
    best_indices = find_longest_chain(adjacency_list, fragments)

    # 4. Convert idx back to number fragments
    best_chain = "".join(fragments[i] for i in best_indices)

    # 5. Show result
    total_elapsed = time.time() - total_start
    print(f"🎯Chain length: {len(best_chain)} \n Chain: {best_chain}")
    print(f"\n⏱️ Total execution time: {total_elapsed:.4f}s")
