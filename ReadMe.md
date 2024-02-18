# Week 5 Progress
We implemented questions 1-4 of the Pac-Man Project. For DFS we implemented it using a stack to keep track of nodes to explore. BFS used a queue to maintain the order of exploration. We learned that it guarantees finding the shortest path, but can be computationally expensive for large mazes. We also implemented Uniform Cost Search (UCS) which prioritizes expanding nodes with the lowest total cost. We used a priority queue based on cost. We learned that it finds an optimal path concerning cost, but may not be the shortest in terms of distance. We finally implemented A* Search which combines BFS with a heuristic function that estimates the remaining cost to the goal. We used UCS with the heuristic added to the priority. We learned that it balances optimality and efficiency, often finding short paths quickly, but requiring careful heuristic design.

## Question 1
### Does Pacman visit all the explored nodes?
No Pacman only visits the nodes that lead him to his goal.

## Question 2
### Is DFS a least-cost solution? Explain your answer.
DFS is not the least-cost solution here because it prioritizes exploration over cost. DFS explores one path deeply before backtracking and trying another which can lead it down long, expensive paths even if shorter, cheaper ones exist elsewhere.

# Week 6 Progress
We implemented questions 5 and 6 during this week. For question 5 we created a 4-element binary array to represent whether or not the corners have been visited. We then initialize all values in the array to false. Then we modify each element in the array to True only if the starting position matches the position of any of the corners. Finally, we update a class variable called starting state to a tuple containing the starting position and the cornersVisited array. For our goal state check, we check to see if all the elements in the corners array have been marked with true. In the get successors function we update our position and check whether or not our new position hits a wall. If the position is not a wall then we iterate over the cornersVisted array and mark a corner as True if the new position matches the corner position. Finally, we return to the new position and the new cornersVistied arra

For question 6 the heuristic we use is the maximum distance from the current position to any of the unvisited corners. Our heuristic is admissible since we only take the maximum distance of all the possible unvisited corners. Because of this design choice, our heuristic always returns a value that is less than the actual cost to the goal state. Our heuristic is also consistent since if we choose a path that leads right to a corner, then the actual cost C drops the heuristic by at most C.


# Output

## Question 1:
 
 <img width="314" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/1c8577dd-d457-476e-8db0-ee783852ae1e">
 
 <img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/8e5fb912-e663-457e-b7da-a9e8b071a05e">



## Question 2:

 <img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/ad7f254e-cd0e-454d-8dc0-62b16b2b39c4">

 <img width="376" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/cc3b55e7-6666-4c8a-97df-b0df9946a95f">


 

## Question 3:

<img width="386" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/f1bfaf45-0141-40f7-8150-f511ca97679f">


<img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/36ff7f2b-efd4-417d-af2e-634ab2e2fa9f">



## Question 4:

 <img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/fbe8edc7-7735-4b1f-8cca-a0b918ed97bc">

<img width="452" alt="image" src="https://github.com/mallie2000/CS205/assets/66195989/cee123f1-f11c-465d-95a5-2e04a19c8939">

## Question 5:
![q5](https://github.com/mallie2000/CS205/assets/90886440/d8ae636f-7813-4ce9-ab22-bff18c39c4d2)

## Question 6:
![q6](https://github.com/mallie2000/CS205/assets/90886440/6029976e-3f53-4724-a5fe-b36acb1c512e)



