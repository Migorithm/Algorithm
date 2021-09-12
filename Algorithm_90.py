import os

def addNumbers(a, b):
    return int((a+b)//1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = float(input().strip())

    b = float(input().strip())

    result = addNumbers(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
