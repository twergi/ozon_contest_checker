from source import config
from solver.solver import solve
from source.utility import get_filenames, tgreen, tyellow, clear_directory
from os.path import join, exists
from os import remove
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Callable


if TYPE_CHECKING:
    from io import TextIOWrapper


class Input:
    def __init__(self, filepath: str) -> None:
        self.lines: list[str] = None
        self.current_line: int = 0

        with open(filepath) as file:
            self.lines = file.readlines()

    def get_input(self) -> str | None:
        if self.current_line == len(self.lines):
            return None

        self.current_line += 1

        return self.lines[self.current_line - 1]


def create_output(res: "TextIOWrapper") -> Callable[[str], None]:
    def print_to_file(line: str = "", *args, **kwargs) -> None:
        print(line, *args, **kwargs, file=res)

    return print_to_file


def timer(func: Callable[[], None]) -> Callable[[], None]:
    td = timedelta(milliseconds=1)

    def run_with_timer(filepath: str) -> None:
        s = datetime.now()

        func(filepath)

        e = datetime.now()

        print(f"{filepath:>4} {(e-s)//td:6d} ms")

    return run_with_timer


@timer
def solve_to_file(filepath: str) -> None:
    inp_path = join(config.INPUTS_FOLDER, filepath)
    inp = Input(inp_path).get_input

    res_path = join(config.RESULTS_FOLDER, filepath)

    if exists(res_path):
        remove(res_path)

    with open(res_path, "x") as res:
        out = create_output(res)

        solve(inp, out)

        res.truncate(res.tell() - 1)  # remove last newline


@timer
def solve_to_stdout(filepath: str) -> None:
    inp_path = join(config.INPUTS_FOLDER, filepath)
    inp = Input(inp_path).get_input
    out = print

    solve(inp, out)


def main() -> None:
    inp_filenames = get_filenames(config.INPUTS_FOLDER)

    run_solver = None
    if config.PRINT_FLAG:
        run_solver = solve_to_stdout
    else:
        run_solver = solve_to_file
        clear_directory(config.RESULTS_FOLDER)

    for inp_filename in inp_filenames:
        run_solver(inp_filename)

    print(tgreen("All done"))

    if not config.PRINT_FLAG:
        print()
        print(
            tyellow(
                f'Output can be set to STDOUT using "{config.PRINT_ARG_VALUE}" flag'
            )
        )
