import sys
import os 

INDEX_1 = 1
INDEX_2 = 2

FILE_1 = sys.argv[INDEX_1]
FILE_2 = sys.argv[INDEX_2]

PATH_1 = os.path.exists(FILE_1)
PATH_2 = os.path.exists(FILE_2)

if PATH_1 and PATH_2: 
    with open(FILE_1, 'r') as origin:
        with open(FILE_2, 'a') as destination:
            for line in origin:
                destination.write(line[0:len(line)-1] + " = "+ str(eval(line)) + "\n")
else:
    print("Retry with valid paths")


"""
inputs 2 file paths. 
the first one is a file in which there mathematical equations written in order to be solved.
the second one is a blank text file.
reads from first file, evaluates the solutions and writes to second file
"""
