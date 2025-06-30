import sys
import csv

def main():
    input_file, output_file = get_file()
    lista = format_file(input_file)
    write(output_file, lista)

def get_file():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")
    
    first = sys.argv[1]
    second = sys.argv[2]
    return first, second

def format_file(file):
    lista = []
    try:
        with open(file, newline='') as inputfile:
            csv_file = csv.reader(inputfile)
            for line in csv_file:
                splitted = line[0].split(", ")
                splitted = splitted[::-1]
                fline = [line[1]]
                new_line = splitted + fline
                lista.append(new_line)
    except FileNotFoundError:
        sys.exit("File was not")
    return lista

def write(output, lista):
    with open(output, "w", newline='') as outputfile:
        writer = csv.writer(outputfile)
        for line in lista:
            if line[0] == "name":
                writer.writerow(["first", "last", "house"])
            else:
                writer.writerow(line)

if __name__ == "__main__":
    main()