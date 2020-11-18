[Repository URL](https://github.com/FGRCL/COMP472)
# Installing a1
Use `poetry install` to install the environment then `poetry shell` to activate it  
or  
Install the following dependencies manually
```
pytest = "^5.2"
numpy = "*"
func-timeout = "*"
```
# Running a2
Activate your python environment if necessary

## Solving A Puzzle

***NOTE: Pre-generated solution, search, and metric files for each algorithm and heuristic can be found in the 'out' folder***

Use `main.py` to solve a any size sliding puzzle. The script has the following arguments.

```
-h, --help            show this help message and exit
--inputpuzzle/-in input puzzle
                      the path to the file containing the puzzles to solve
--solutiondirectory/-out solution directory
                      the path to the directory to output the puzzle solutions
--searchdirectory/-s search file
                      the path to the directory to output the algorithm's searched states
--metricsfile/-m metrics file
                      the path to the file to output the algorithm's metrics
--searchtimeout/-t timeout
                      the allotted time for a search algorithm to find a solution in seconds
--dimensions/-d dimensions
                      the dimensions of the puzzle in the format: {width}x{height}. ex.: 4x2
--algorithm/-a {ucs,gbfs,astar}
                      the search algorithm to use
--heuristic/-he {naive,manhattan,hamming,permutations}
                      the heuristic to use for GBFS and A*
```
Example: ` python3 a2/main.py -a gbfs -he manhattan -in in/puzzle1.txt -out out/solution/ -s out/search/ -m out/metrics/metrics.csv -t 60 -d 4x2 `

You can also use the convenient script `./create_output.sh` to run 5 different algorithms on a set of 50 4x2-size puzzles, a timeout of 60 seconds, and generate their respective metrics.  
These algorithms are :  
- Uniform Cost Search 
- Greedy Best First Search using Hamming heuristic
- Greedy Best First Search using Manhattan heuristic
- A* using Hamming heuristic
- A* using Manhattan heuristic
