# Progress
We implemented questions 1-4 of the Pac-Man Project. For DFS we implemented it using a stack to keep track of nodes to explore. BFS used a queue to maintain the order of exploration. We learned that it guarantees finding the shortest path, but can be computationally expensive for large mazes. We also implemented Uniform Cost Search (UCS) which prioritizes expanding nodes with the lowest total cost so far. We used a priority queue based on cost. We learned that it finds an optimal path with respect to cost, but may not be the shortest in terms of distance. We finally implemented A* Search which combines BFS with a heuristic function that estimates the remaining cost to the goal. We used UCS with the heuristic added to the priority. We learned that it balances optimality and efficiency, often finding short paths quickly, but requiring careful heuristic design.

## Question 1
### Does Pacman visit all the explored nodes?
No Pacman only visits the nodes that lead him to his goal.

## Question 2
### Is DFS a least-cost solution? Explain your answer.
No, DFS is not the least-cost solution here because it prioritizes exploration over cost. DFS explores one path deeply before backtracking and trying another which can lead it down long, expensive paths even if shorter, cheaper ones exist elsewhere.

Question 1:
 
 <img width="314" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/1c8577dd-d457-476e-8db0-ee783852ae1e">
 
 <img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/8e5fb912-e663-457e-b7da-a9e8b071a05e">



Question 2:

 <img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/ad7f254e-cd0e-454d-8dc0-62b16b2b39c4">

 <img width="376" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/cc3b55e7-6666-4c8a-97df-b0df9946a95f">


 

Question 3:

<img width="386" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/f1bfaf45-0141-40f7-8150-f511ca97679f">


<img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/36ff7f2b-efd4-417d-af2e-634ab2e2fa9f">


 
 







Question 4:

 <img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/fbe8edc7-7735-4b1f-8cca-a0b918ed97bc">

<img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/cee123f1-f11c-465d-95a5-2e04a19c8939">

