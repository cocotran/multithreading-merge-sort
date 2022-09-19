import argparse

from merge_sort import *
from thread import *


def get_array_from_file(file_name: str):
    with open(file_name, "r") as f:
        arr = [int(line.strip()) for line in f.readlines()]
        f.close()
        return arr


if __name__ == "__main__":

    # Setup
    FILE_NAME = "input.txt"

    # Instantiate the parser
    parser = argparse.ArgumentParser(description="Merge-Sort using multithreading")

    # Optional argument
    parser.add_argument("--input", type=str, help="input file name")

    args = parser.parse_args()

    if args.input:
        FILE_NAME = args.input

    # Run program
    thread_manager = ThreadManager()
    app = ThreadWithReturnValue(
        target=merge_sort,
        name=thread_manager.get_new_thread_name(),
        args=(
            get_array_from_file(FILE_NAME),
            thread_manager,
        ),
    )
    app.start()
    app.join()
