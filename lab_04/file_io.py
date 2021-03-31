# Problem Lab04-2

import sys
def process_file(fileName):
    input_file = open(fileName, "r")

    for line in input_file:
        line = line.rstrip('\n')
        print(line)

    input_file.close()

if __name__ == "__main__":
    # process_file(sys.argv[1])
    process_file('list.txt')