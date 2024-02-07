from os import listdir, remove
from os.path import join


def get_filenames(folder: str) -> list[str]:
    def remove_gitignore(paths: list[str]) -> None:
        try:
            paths.remove(".gitignore")
        except:
            ...

    filenames = listdir(folder)
    remove_gitignore(filenames)

    return sorted(filenames, key=lambda f: int("".join(filter(str.isdigit, f))))


def clear_directory(path: str) -> None:
    filenames = get_filenames(path)

    if len(filenames) != 0:
        print(f'Clearing directory "{path}"')

    for filename in filenames:
        remove(join(path, filename))


class textcolor:
    green = "\033[32m"
    red = "\033[31m"
    yellow = "\033[33m"
    end = "\033[0m"


class bgcolor:
    red = "\033[41m"
    end = "\033[0m"


def tred(string: str) -> str:
    return f"{textcolor.red}{string}{textcolor.end}"


def tgreen(string: str) -> str:
    return f"{textcolor.green}{string}{textcolor.end}"


def tyellow(string: str) -> str:
    return f"{textcolor.yellow}{string}{textcolor.end}"


def bgred(string: str) -> str:
    return f"{bgcolor.red}{string}{bgcolor.end}"
