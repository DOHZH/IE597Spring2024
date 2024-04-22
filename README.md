# IE597Spring2024
## Update 4/22/2024
1. week 14 folder: read paper: https://doi.org/10.1016/j.cor.2018.05.023

## Update 4/15/2024
1. week 12-13 folder: read paper:https://doi.org/10.1016/j.tre.2024.103447
## Update 4/8/2024
1. week 12 folder: read paper:https://doi.org/10.1016/j.tre.2024.103447

## Update 4/1/2024
1. week 10-11 folder: read paper: https://doi.org/10.1016/j.cor.2023.106353 ; https://doi.org/10.1287/trsc.2016.0729

## Update 3/18/2024
1. I have already read the paper refered last meeting: New benchmark instances for the inventory routing problem
2. Week8-9 folder:
   1. note.md: reading note
   2. pic: pictures in note 

## Update 3/3/2024:
1. This week, I finished the paper reading "Inventory routing problems: an introduction"
2. Find some program of IRP solver
   1. many open source IRP solvers in the github are based on the Gurobi, OR tools
   2. Hexaly Optimizer: a commercial optimizer, not open source
   3. A competition of IRP: we may find some effective alg from the IRP competition http://dimacs.rutgers.edu/programs/challenge/vrp/papers-videos/

## Update 2/26/2024:
1. update presentation pdf
2. week 6 folder
   1. pic: picture in note
   2. `note.md`: not finish 
      1. Bertazzi, L., & Speranza, M. G. (2012). Inventory routing problems: an introduction. EURO Journal on Transportation and Logistics, 1, 307-326.
      2. Burns, L. D., Hall, R. W., Blumenfeld, D. E., & Daganzo, C. F. (1985). Distribution Strategies that Minimize Transportation and Inventory Costs. Operations Research, 33(3), 469–490. http://www.jstor.org/stable/170552
   3. `pre.pdf`: presentation


## Update 2/19/2024:
1. prepare the presentation
2. week 5 folder
   1. data:Uchoa et al. (2014), http://vrp.atd-lab.inf.puc-rio.br/index.php/en/
   2. `code.ipynb`: run the performance comparison
   3. `pre.pdf`: presentation

## Update 2/11/2024:
1. compare with PyVRP and routingblocks.
   1. In order to solve n439-k37 CVRP, PyVRP runs 40.38 seconds with 0.9% worse than right sol while routingblocks runs 3 minutes with 6.9% worse
   2. Although PyVRP are better than routingblocks in time and accuracy, but I think it is responsibility from algorithm. The official CVRP plugin provided by routingblocks use a random alg, which seems worse than alg in pyVRP
   3. Routingblocks provides a powerful set of tool, allowing us to customize our own CVRP algorithm. However, pyVRP doesn't give us enough interface to develop plugin
2. week 4 folder
   1. `data`: data from https://github.com/PyVRP/Instances.git, vrplib format
   2. `code.ipynb`: code
   3. `note.md`: learning note of PyVRP and routingblocks. You may meet some problem during installing routingblocks CVRP plugin, please read this note to help you solve problem

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