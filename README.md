# IE597Spring2024

## Update 2/04/2024:
1. read paper: Bock, A., & Sanità, L. (2015). The capacitated orienteering problem. Discrete Applied Mathematics, 195, 31-42.
2. Week3 folder
   1. `PaperNote.md`：reading note
   2. pic: the figures in the note

## Update 1/28/2024:
1. Use bigger dataset to solve and compare pyVRP and VRPSolver
2. week2 folder
   1. data: this dataset contains 101 consumers and 1 depot; 8 trucks with same type (capacity 200, 1 variable cost and no fixed cost)
   2. pic: picture for `note.md`
   3. pyVRP: a solver library
   4. `BaPTree.dot`: file created by VRPSolver
   5. `code.ipynb`: code of pyVRP and VRPSolver
   6. `note.md`: study notes

## Update 1/21/2024:
1. learnt pyVRP and VRPSolver to solve CVRP
2. To run VRPSolver, you should install VRPSolver: https://vrpsolver.math.u-bordeaux.fr/
3. week1 folder:
   1. data: CVRP dataset, this dataset contains 21 consumers and 1 depot; 4 trucks with same type (capacity 6000, 1 variable cost and no fixed cost)
      1.  `VRP-01-CVRP-Coordinates.txt`: coordinates of consumer and depot. The first point is coordinate
      2.  `VRP-01-CVRP-Parameters.txt`: each point's parameter, contains: demand and timewidow
          1.  demand: depot's demand value equals to 0
          2.  TW_early: if the client has a time window, this parameter indicates the earliest time that a vehicle can arrive. 
          3.  TW_late: if the client has a time window, this parameter indicates the latest time that a vehicle can arrive.
          4.  TW_service_time: arriving at client how much time is needed to the vehicle unload the goods	
          5.  TW_wait_cost: cost/time or penalty/time for a vehicle that spends time waiting to a client to be available.
   2. pic: picture for `note.md`
   3. pyVRP: a solver library
   4. result: result report from pyVRP
   5. `BaPTree.dot`: file created by VRPSolver
   6. `code.ipynb`: code of pyVRP and VRPSolver
   7. `note.md`: study notes