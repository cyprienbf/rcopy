#!/bin/python3
import os, argparse

VERSION = "0.1.0"

EXCLUDED_DIR = [".git", "__pycache__", ".venv"]
EXCLUDED_EXTENSIONS = [".cfg", ".gitignore", ".bin"]

class Config:
    def __init__(
        self,
        input_path: str,
        output_path: str,
        full_file_path: bool,
        verbose: bool
    ):
        self.input_path = os.path.abspath(input_path) if input_path else os.getcwd()
        self.output_path = os.path.abspath(output_path) if output_path else os.path.abspath("result.txt")
        self.full_file_path = full_file_path
        self.verbose = verbose

    def __str__(self):
        return f"Config:\n\tinput_path: {self.input_path}\n\toutput_path: {self.output_path}\n\tfull_file_path: {self.full_file_path}\n\tverbose: {self.verbose}"


def main():
    parser = argparse.ArgumentParser(
        "rcopy",
        f"{argparse._sys.argv[0]} [-i <input_path>] [-o <output_path>]",
        "Description",
        "Epilog",
    )
    parser.add_argument("-i", "--input", help="")
    parser.add_argument("-o", "--output", help="")
    parser.add_argument("-f", "--full", action="store_true", help="")
    parser.add_argument("-v", "--verbose", action="store_true", help="")

    args = parser.parse_args()

    conf = Config(args.input, args.output, args.full, args.verbose)

    if conf.verbose:
        print(conf)

    output = ""

    try:
        for root, folders, files in os.walk(conf.input_path):
            folders[:] = [f for f in folders if f not in EXCLUDED_DIR]
            for filename in files:
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as f:
                    content = f.read()
                output += f"{file_path if conf.full_file_path else filename}: '{content}'\n\n"

        with open(conf.output_path, 'w') as f:
            f.write(output)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
