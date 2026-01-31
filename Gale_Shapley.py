import sys

# Read single number from file
def read_num(file):
    out_str = ''
    while True:
        temp = file.read(1)
        if temp == '' or temp == ' ' or temp == '\n':
            break
        else:
            out_str += temp
    return int(out_str) - 1 # subtract 1 to convert to 0-indexed array

# Returns string of whether it's stable or why not
def verification(length, hospital_rank, student_rank, assignment_of_h, assignment_of_s):
    if -1 in assignment_of_h:
        print("INVALID: unmatched hospital")
        return("INVALID: unmatched hospital")

    if -1 in assignment_of_s:
        print("INVALID: unmatched student")
        return("INVALID: unmatched student")

    for hospital in range(length):
        if assignment_of_s[assignment_of_h[hospital]] != hospital:
            print("INVALID: inconsistent matching")
            return("INVALID: inconsistent matching")

    hospital_verify = [[0] * length for _ in range(length)]
    student_verify = [[0] * length for _ in range(length)]

    # Create ranking lists for hospitals and students, named ??_verify b/c ??_ranks is already used
    for hospital in range(length):
        for rank, student in enumerate(hospital_rank[hospital]):
            hospital_verify[hospital][student] = rank

    for student in range(length):
        for rank, hospital in enumerate(student_rank[student]):
            student_verify[student][hospital] = rank

    stable = True; # Assumed stable at beginning
    for hospital in range(length):
        for student in range(length):
            if student == assignment_of_h[hospital]:
                continue

            if hospital_verify[hospital][student] < hospital_verify[hospital][assignment_of_h[hospital]]:
                if student_verify[student][hospital] < student_verify[student][assignment_of_s[student]]:
                    # If a hospital prefers a student over its current assignment and the student does too,
                        # Print blocking pair, make stable false, and break to save time
                    print(f"UNSTABLE: blocking pair (hospital {hospital + 1}, student {student + 1})")
                    stable = False
                    return f"UNSTABLE: blocking pair (hospital {hospital + 1}, student {student + 1}"
        if not stable:
            break
    if stable: # If no blocking pairs found, print "VALID STABLE"
        print("VALID STABLE")

def gale_shapley(hospital_ranks, student_ranks, length, print_assignments = True):
    # assignment_of_h[i] contains the student number assigned to hospital number i
    assignment_of_h = [-1] * length
    # assignment_of_s[i] contains the student number assigned to hospital number i
    assignment_of_s = [-1] * length

    # build list of free hospitals (all hospitals i start free)
    free_hospitals = []
    for i in range(length):
        free_hospitals.append(i)

    # STEP 2: Run Gale-Shapley algorithm
    while free_hospitals:
        hospital = free_hospitals.pop(0)
        top_student = hospital_ranks[hospital][0]
        hospital_ranks[hospital].pop(0) # prevent re-assignment to same student
        
        if assignment_of_s[top_student] == -1: # if student is free
            assignment_of_s[top_student] = hospital
            assignment_of_h[hospital] = top_student
        elif student_ranks[top_student].index(hospital) < student_ranks[top_student].index(assignment_of_s[top_student]): # if student prefers new hospital over their current
            old_hospital = assignment_of_s[top_student]
            assignment_of_s[top_student] = hospital
            assignment_of_h[hospital] = top_student
            assignment_of_h[old_hospital] = -1
            free_hospitals.append(old_hospital)
        else: # if student prefers their current hospital over new hospital
            free_hospitals.append(hospital)
            pass     

    # Fixed print function
    if print_assignments:
        for hospital in range(length):
            print(f"{hospital + 1} {assignment_of_h[hospital] + 1}")

    return assignment_of_h, assignment_of_s

if __name__ == "__main__":
    # STEP 1: Read input file and build rank arrays
    with open('inputs/example_input1.txt') as file:
        first_line = file.readline().strip()

        # Handle empty file
        if not first_line:
            print("INVALID: empty file")
            sys.exit(1)

        try:
            length = int(first_line)
        except ValueError:
            print("ERROR: first line must be an integer")
            sys.exit(1)

        hospital_ranks = [] # 2D array [x, y] where x is hospital number starting at 0
        for _ in range(length):
            temp_hospital = []
            for _ in range(length):
                temp_hospital.append(read_num(file))
            hospital_ranks.append(temp_hospital)

        student_ranks = []
        for _ in range(length):
            temp_student = []
            for _ in range(length):
                temp_student.append(read_num(file))
            student_ranks.append(temp_student)

        if student_ranks.__len__() != length:
            print("INVALID: inconsistent length of student ranks")
            exit(-1)

        if hospital_ranks.__len__() != length:
            print("INVALID: inconsistent length of hospital ranks")
            exit(-1)

        import copy
        hospital_copy = copy.deepcopy(hospital_ranks)
        student_copy = copy.deepcopy(student_ranks)

    assignment_of_h, assignment_of_s = gale_shapley(hospital_ranks, student_ranks, length)

    if len(sys.argv) > 1:
        cli_input = sys.argv[1]
        if(cli_input == "-v" or cli_input == "-verify"):
            verification(length, hospital_copy, student_copy, assignment_of_h, assignment_of_s)
