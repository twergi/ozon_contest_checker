from source import config
from sys import argv


SOLVE = "solve"
CHECK = "check"
UNZIP = "unzip"


def check_option(run_type: str, option: str | None) -> None:
    if run_type == CHECK and option == config.STRIP_ARG_VALUE:
        config.STRIP_FLAG = True
        return

    if run_type == SOLVE and option == config.PRINT_ARG_VALUE:
        config.PRINT_FLAG = True
        return

    raise ValueError(f'Run type "{run_type}" doesn\'t have "{option}" argument')


if __name__ == "__main__":
    if len(argv) > 3 or len(argv) == 1:
        print("Specify single option")
        print("Available options:")
        print(f"- {SOLVE}")
        print(f"- {CHECK}")
        print(f"- {UNZIP}")
        exit()

    run_type = argv[1]
    option = None

    if len(argv) == 3:
        check_option(run_type, argv[2])

    if run_type == SOLVE:
        from source.solve import main as run_solve

        run_solve()

    elif run_type == CHECK:
        from source.check import main as run_check

        run_check()

    elif run_type == UNZIP:
        from source.unzip import main as run_unzip

        run_unzip()

    else:
        raise ValueError("Incorrect run argument")
