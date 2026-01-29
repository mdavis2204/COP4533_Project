# Reading file
    # TODO: allow for >2 digit numbers

def read_num(file):
    out_str = ''
    while True:
        temp = file.read(1)
        print(temp)
        if temp == ' ':
            exit
        else:
            out_str += temp
    return int(out_str)

with open('example_input1.txt') as file:
    length = int(file.readline())


    hospital_ranks = [] # 2D array [x, y] where x is hospital number starting at 0
    for _ in range(length):
        temp_hospital = []
        for _ in range(length):
            # temp_hospital.append(read_num(file, length))
            temp_hospital.append(int(file.read(1))) # TODO: allow for more than 1 digit numbers
            file.read(1)
        hospital_ranks.append(temp_hospital)

    student_ranks = []
    for _ in range(length):
        temp_student = []
        for _ in range(length):
            # temp_student.append(read_num(file, length))
            temp_student.append(int(file.read(1)))
            file.read(1)
        student_ranks.append(temp_student)

assignments = [0] * length

all_assigned = False

while not all_assigned:
    all_assigned = True
    for i in range(assignments.__len__()):
        if(assignments[i] == 0):
            all_assigned = False

            # Part 1, initial if
            allocated = False
            for assign in assignments:
                if(hospital_ranks[i][0] == assign):
                    allocated = True

            if(not allocated):
                assignments[i] = hospital_ranks[i][0]
                continue

            # Part 2, else if


    all_assigned = True


# TODO: Output
    # Note, array index starts at 0, hospital/student numbers begin at 1. Just add 1.

print(assignments)