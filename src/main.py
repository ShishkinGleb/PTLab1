import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    #path = "C:\VolgGTU\mag_1_1\tp\Lab_1_Shishkin\PTLab1\data\data.txt"
    #print(path)
    #reader = TextDataReader()
    reader = XMLDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)


if __name__ == "__main__":
    main()
