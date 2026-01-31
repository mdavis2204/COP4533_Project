# Read single number from file
def read_num(file):
    out_str = ''
    while True:
        temp = file.read(1)
        # print(f"Temp: {temp}")
        if temp == '' or temp == ' ' or temp == '\n':
            break
        else:
            out_str += temp
    return int(out_str) - 1 # subtract 1 to convert to 0-indexed array

if __name__ == "__main__":
    # STEP 1: Read input file and build rank arrays
    with open('inputs/example_input1.txt') as file:
        length = int(file.readline())
        # print(f"Length: {length}")

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
        
        if(assignment_of_s[top_student] == -1): # if student is free
            assignment_of_s[top_student] = hospital
            assignment_of_h[hospital] = top_student
        elif(student_ranks[top_student][hospital] < student_ranks[top_student][assignment_of_s[top_student]]): # if student is not free but prefers new hospital over their current
            assignment_of_s[top_student] = hospital
            assignment_of_h[hospital] = top_student
            free_hospitals.append(assignment_of_s[top_student])
        else: # if student prefers their current hospital over new hospital
            free_hospitals.append(hospital)
            pass     

        all_assigned = True

    def convert_to_1_index(array):
        return [x + 1 for x in array]

    # print(f"Assignments of H: {convert_to_1_index(assignment_of_h)}")
    # print(f"Assignments of S: {convert_to_1_index(assignment_of_s)}")

    # Fixed print function
    for hospital in range(length):
        print(f"{hospital + 1} {assignment_of_h[hospital] + 1}")


    # Verifier
    hospital_verify = [[0] * length for _ in range(length)]
    student_verify = [[0] * length for _ in range(length)]

    # Create ranking lists for hospitals and students, named ??_verify b/c ??_ranks is already used
    for hospital in range(length):
        for rank, student in enumerate(hospital_ranks[hospital]):
            hospital_verify[hospital][student] = rank

    for student in range(length):
        for rank, hospital in enumerate(student_ranks[student]):
            student_verify[student][hospital] = rank

    # print(hospital_verify)
    # print(student_verify)

    stable = True; # Assumed stable at beginning
    for hospital in range(length):
        for student in range(length):
            if student == assignment_of_h[hospital]:
                continue

            if hospital_verify[hospital][student] < hospital_verify[hospital][assignment_of_h[hospital]]:
                if student_verify[student][hospital] < student_verify[student][assignment_of_s[hospital]]:
                    # If a hospital prefers a student over its current assignment and the student does too,
                        # Print blocking pair, make stable false, and break to save time
                    print(f"UNSTABLE: blocking pair (hospital {hospital + 1}, student {student + 1}")
                    stable = False
                    break
        if not stable:
            break
    if stable: # If no blocking pairs found, print "VALID STABLE"
        print("VALID STABLE")
