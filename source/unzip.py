from source import config
from source.utility import get_filenames, tgreen, clear_directory
import zipfile
from os.path import join
from os import rename


def main() -> None:
    filenames = get_filenames(config.RAW_FOLDER)

    if len(filenames) > 1 or len(filenames) == 0:
        raise Exception(
            f'Directory "{config.RAW_FOLDER}" must contain single .zip file'
        )

    clear_directory(config.INPUTS_FOLDER)
    clear_directory(config.ANSWERS_FOLDER)

    zip_name = filenames[0]
    zip_path = join(config.RAW_FOLDER, zip_name)

    zip_filenames: list[str] = None

    with zipfile.ZipFile(zip_path) as zip_file:
        zip_filenames = zip_file.namelist()
        zip_filenames.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

        zip_file.extractall(config.RAW_FOLDER)

        for filename in zip_filenames:
            fr = join(config.RAW_FOLDER, filename)
            to = (
                join(config.ANSWERS_FOLDER, filename)
                if filename.endswith("a")
                else join(config.INPUTS_FOLDER, filename)
            )
            print(f"{filename:5s} -> {to}")
            rename(fr, to)

    print(tgreen("All done"))
