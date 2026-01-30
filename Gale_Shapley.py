# Reading file
# TODO: allow for >2 digit numbers

def read_num(file):
    out_str = ''
    while True:
        temp = file.read(1)
        print(temp)
        if temp == ' ':
            break
        else:
            out_str += temp
    return int(out_str)

if __name__ == "__main__":
    # STEP 1: Read input file and build rank arrays
    with open('inputs/example_input1.txt') as file:
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

    # assignments[i] contains the student number assigned to hospital number i
    assignments = [0] * length

    all_assigned = False


    # Note to Matthew before going to sleep: I'm not sure current implementation will work, instead...
    # We should have a list of unassigned hospitals
    # Then while unassigned hospitals is not empty, we iterate
    # in one iteration we get the top student in the hospital h's rank list "to whom h has not been matched"
    # we check if student is free and if student prefers h over hospital they are assigned to, and reassign the student to h if so

    # STEP 2: Run Gale-Shapley algorithm
    while not all_assigned:
        all_assigned = True
        for i in range(len(assignments)): # loop through all hospitals
            if(assignments[i] == 0): # if 0 then no student was assigned yet to hospital i
                all_assigned = False

                # Part 1, initial if
                allocated = False
                # loop through assigned students
                for student in assignments:
                    if(hospital_ranks[i][0] == student): # if top student in hospital i's rank list is already assigned to a hospital
                        allocated = True

                if(not allocated):
                    assignments[i] = hospital_ranks[i][0]
                    continue

                # Part 2, else if


        all_assigned = True
    
    print(assignments)


# TODO: Output
    # Note, array index starts at 0, hospital/student numbers begin at 1. Just add 1.
