# Performance report
1. In order to solve n439-k37 CVRP, PyVRP runs 40.38 seconds with 0.9% worse than right sol while routingblocks runs 3 minutes with 6.9% worse
2. Although PyVRP are better than routingblocks in time and accuracy, but I think it is responsibility from algorithm. The official CVRP plugin provided by routingblocks use a random alg, which seems worse than alg in pyVRP
3. Routingblocks provides a powerful set of tool, allowing us to customize our own CVRP algorithm. However, pyVRP doesn't give us enough interface to develop plugin

# PyVRP
1. This module is different with "pyvrp" in week1 and week2 although their names are same.
2. Installation
   1. `pip install pyvrp`
   2. installing from source to get the lateset version `pip install 'pyvrp @ git+https://github.com/PyVRP/PyVRP'`
   3. run examples from repository (you can skip it if you don't care about run examples provided by author)
      1. clone `git clone https://github.com/PyVRP/PyVRP.git`
      2. `pip install --upgrade poetry`
      3. `cd` to this project file and build it with `poetry`: `poetry install --with examples`
      4. open jupyter notebook`poetry run jupyter notebook`
3. Code
   1. create model(the first step if you want use PyVRP): `m = Model()`
   2. add vehicles: `m.add_vehicle_type(VehicleType)`
      1. parameters：
            ```python
                class VehicleType(
                    num_available: int = 1, 
                    capacity: int = 0, 
                    depot: int = 0, 
                    fixed_cost: int = 0, 
                    tw_early: int | None = None, 
                    tw_late: int | None = None, 
                    max_duration: int | None = None, 
                    name: str = '')
            ```
      2. example: `m.add_vehicle_type(4, capacity=15)`
   3. add data manually
      1. add depot:`m.add_depot(x: int, y: int, tw_early: int = 0, tw_late: int = 0, name: str = '')`
         1. x,y are coordinate of depot
      2. add client:`m.add_client(x: int, y: int, demand: int = 0, service_duration: int = 0, tw_early: int = 0, tw_late: int = 0, release_time: int = 0, prize: int = 0, required: bool = True, name: str = '')`
      3. add edge:`add_edge(frm: Client, to: Client, distance: int, duration: int = 0)`
   4. read VRPLIB file to add data:
      1. import read module: `from pyvrp import Model, read`
      2. read: `read(where: str | Path, instance_format: str = 'vrplib', round_func: str | Callable[[ndarray], ndarray] = 'none') `
         1. `instance_format`:File format of the instance to read, one of 'vrplib' (default) or 'solomon' 
         2. `round_func`: Optional rounding function. Will be applied to round data if the data is not already integer. This can either be a function or a string:
            1. `round` rounds the values to the nearest integer;
            2. `trunc` truncates the values to be integral;
            3. `trunc1` or `dimacs` scale and truncate to the nearest decimal;
            4. `none` does no rounding. This is the default.
      3. write to model:`model = Model.from_data(INSTANCE)`: INSTANCE is a return vale from function `read()`
   5. solve:`solve(stop: StoppingCriterion, seed: int = 0)`
      1. StoppingCriterion:
         1. import(use maxRunTime as instance): `from pyvrp.stop import MaxRuntime`
         2. `MaxIterations(int)`: stops after a maximum number of iterations
         3. `MaxRuntime(float)`: stops after a maximum number of iterations
         4. `MultipleCriteria(list[StoppingCriterion])`: Simple aggregate class that manages multiple stopping criteria at once
         5. `NoImprovement(int)`: stops if the best solution has not been improved for a fixed number of iterations.
   6. read solution file in VRPLIB:`read_solution(where: str | Path)`
   7. Plotting:
      1. create plot:
         1. `import matplotlib.pyplot as plt`
         2. `_, ax = plt.subplots(figsize=(8, 8))`
      2. coordinates:
         1. `from pyvrp.plotting import plot_coordinates`
         2. `plot_coordinates(m.data(), ax=ax)`
      3. solution:
         1. `from pyvrp.plotting import plot_solution`
         2. `plot_solution(res.best, m.data(), ax=ax)`: res is the return value of `solve`
      4. plot CVRPLib file
         1. import 
            1. `from pyvrp.plotting import(plot_instance,plot_result)`
            2. `import matplotlib.pyplot as plt`
         2. plot overview of data(INSTANCE is return of `read()`):
            1. `fig = plt.figure(figsize=(12, 6))`
            2. `plot_instance(INSTANCE, fig)`
         3. plot solve result:
            1. `fig = plt.figure(figsize=(15, 9))`
            2. `plot_result(result, INSTANCE, fig)`
            3. `fig.tight_layout()`
4. Tips:
   1. if you want to use read function, please follow `vrplib` format: https://pyvrp.org/dev/supported_vrplib_fields.html
   2. if you want to use CVRPlib, you may need a program to change it to `vrplib` format
5. Reference: 
   1. Wouda, N.A., L. Lan, and W. Kool (2024). PyVRP: a high-performance VRP solver package. INFORMS Journal on Computing, forthcoming. https://doi.org/10.1287/ijoc.2023.0055.
   2. https://pyvrp.org/examples/quick_tutorial.html

# routingblocks
1. install:
   1. `pip install routingblocks`
   2. latest version: `pip install git+https://github.com/tumBAIS/RoutingBlocks`
   3. install CVRP extension (version 0.1.2): 
      1. git clone https://github.com/tumBAIS/routingblocks-native-extension-example.git
      2. go to `<dirctory>/pyproject.toml`, modify the `name` in [project] to `name = "routingblocks_cvrp"`
      3. pip install `<dirctory>`
2. use:
   1. pip install -r `<dirctory>/example/requirements.txt`
   2. python `<dirctory>/example/usage.py X-n101-k25`
   3. you can modify the `<dirctory>/src/CVRPEvaluation.cpp` to make your own CVRP plugin
   4. in this lab, we only use alg provided by routingblocks