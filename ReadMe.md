# Progress
We implemented questions 1-4 of the Pac-Man Project. For DFS we implemented it using a stack to keep track of nodes to explore. BFS used a queue to maintain the order of exploration. We learned that it guarantees finding the shortest path, but can be computationally expensive for large mazes. We also implemented Uniform Cost Search (UCS) which prioritizes expanding nodes with the lowest total cost so far. We used a priority queue based on cost. We learned that it finds an optimal path with respect to cost, but may not be the shortest in terms of distance. We finally implemented A* Search which combines BFS with a heuristic function that estimates the remaining cost to the goal. We used UCS with the heuristic added to the priority. We learned that it balances optimality and efficiency, often finding short paths quickly, but requiring careful heuristic design.

## Question 1
### Does Pacman visit all the explored nodes?
No Pacman only visits the nodes that lead him to his goal.

## Question 2
### Is DFS a least-cost solution? Explain your answer.
No, DFS is not the least-cost solution here because it prioritizes exploration over cost. DFS explores one path deeply before backtracking and trying another which can lead it down long, expensive paths even if shorter, cheaper ones exist elsewhere.
