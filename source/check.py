from os.path import join
from source.utility import get_filenames, tred, tgreen, bgred, tyellow
from source import config


def main() -> None:
    ans_files = get_filenames(config.ANSWERS_FOLDER)
    res_files = get_filenames(config.RESULTS_FOLDER)

    print(f"Answers: {len(ans_files)}")
    print(f"Results: {len(res_files)}")

    for res_filename in res_files:
        ans_filename = answer_name(res_filename)

        if ans_filename not in ans_files:
            print(f'Answer for file "{res_filename}" not found')
            continue

        compare(res_filename, ans_filename)


def compare(res_filename: str, ans_filename: str) -> None:
    def err() -> None:
        ans.close()
        res.close()
        exit()

    res_path = join(config.RESULTS_FOLDER, res_filename)
    ans_path = join(config.ANSWERS_FOLDER, ans_filename)

    res = open(res_path)
    ans = open(ans_path)

    ans_lines = ans.readlines()

    for li in range(len(ans_lines)):
        ans_line = ans_lines[li]
        res_line = res.readline()

        if config.STRIP_FLAG:
            ans_line = ans_line.strip()
            res_line = res_line.strip()

        if len(res_line) != len(ans_line):
            print(tred(f"\nfile {res_filename}, line {li+1}"))
            print(f"len(result) = {len(res_line):d}")
            print(r'"', bgred(res_line), r'"', sep="")
            print(f"len(answer) = {len(ans_line):d}")
            print(r'"', bgred(ans_line), r'"', sep="")

            print(
                tyellow(
                    f'\nAnswer and result lines can be trimmed using "strip()" method. To enable, use "check {config.STRIP_ARG_VALUE}"'
                )
            )

            err()

        for i in range(len(ans_line)):
            if res_line[i] != ans_line[i]:
                s = max(i - 5, 0)
                ea = min(i + 6, len(ans_line))
                er = min(i + 6, len(res_line))

                print(tred(f"\nfile {res_filename}, line {li+1}, symbol {i+1}"))
                print(ans_line[s:ea])
                print(res_line[s:er])
                print(" " * (i - s), tred("↑"), sep="")

                err()

    res.close()
    ans.close()

    print(f"{tgreen('OK')} {res_filename:>4}")


def answer_name(filename: str) -> str:
    return f"{filename}.a"
