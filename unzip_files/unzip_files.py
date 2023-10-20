import os
import zipfile
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Extract a specified zip file.')
    parser.add_argument("-l", "--zippedfile", required=True, help="Path to the zipped file")
    return parser.parse_args()

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")
    if not file_path.endswith(".zip"):
        raise ValueError(f"Not a zip file: {file_path}")

def extract(zip_file):
    file_name, _ = os.path.splitext(zip_file)
    new_directory = os.path.join(os.getcwd(), file_name)
    with zipfile.ZipFile(zip_file, 'r') as zip_object:
        zip_object.extractall(new_directory)
    print(f"Extracted {zip_file} to {new_directory}")

def main():
    args = parse_arguments()
    zip_file = args.zippedfile
    try:
        validate_file(zip_file)
        extract(zip_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
