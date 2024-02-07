# OZON Contest Checker
## Set answers and inputs
- Download test examples
- Place `.zip` file with inputs and answers to `raw` folder (archive contents must be `1` for inputs and `1.a` for answers)
- Run `run.py` file with `unzip` argument


## Run solver
- Place your solution in `solver.py` `solve` function
- Input and output with `input` and `output` function parameters
- Run `run.py` file with `solve` argument
- By default results are written in `results` folder (to use STDOUT use `--print` flag)


## Check results
- Run `run.py` file with `check` argument
- Each `answer` and `result` file line can be trimmed with `--strip` flag