import argparse
from threading import Thread

from merge_sort import merge_sort
from thread import *


def get_array_from_file(file_name: str):
    with open(file_name, "r") as f:
        arr = [int(line.strip()) for line in f.readlines()]
        f.close()
        return arr


def run_merge_sort(arr, thread_manager):
    sort_thread = ThreadWithReturnValue(
        target=merge_sort,
        name=thread_manager.get_new_thread_name(),
        args=(
            arr,
            thread_manager,
        ),
    )
    sort_thread.start()
    sort_thread.join()


if __name__ == "__main__":

    # Setup
    FILE_NAME = "input.txt"
    THREAD_MANAGER = ThreadManager()  # Master thread manager

    # Instantiate the parser
    parser = argparse.ArgumentParser(description="Merge-Sort using multithreading")

    # Optional argument
    parser.add_argument("--input", type=str, help="input file name")

    args = parser.parse_args()

    if args.input:
        FILE_NAME = args.input

    # Run sort on separate thread
    app = Thread(
        target=run_merge_sort,
        name="main_sort_thread",
        args=(
            get_array_from_file(FILE_NAME),
            THREAD_MANAGER,
        ),
    )
    app.start()
    app.join()
