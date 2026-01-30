# Reading file

def read_num(file):
    out_str = ''
    while True:
        temp = file.read(1)
        print(f"Temp: {temp}")
        if temp == '' or temp == ' ' or temp == '\n':
            break
        else:
            out_str += temp
    return int(out_str)

if __name__ == "__main__":
    # STEP 1: Read input file and build rank arrays
    with open('inputs/example_input1.txt') as file:
        length = int(file.readline())
        print(f"Length: {length}")

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
    assignment_of_h = [0] * length
    # assignment_of_s[i] contains the student number assigned to hospital number i
    assignment_of_s = [0] * length

    # build list of free hospitals (all hospitals i start free)
    free_hospitals = []
    for i in range(length):
        free_hospitals.append(i)

    # Note to Matthew before going to sleep: I'm not sure current implementation will work, instead...
    # We should have a list of unassigned hospitals
    # Then while unassigned hospitals is not empty, we iterate
    # in one iteration we get the top student in the hospital h's rank list "to whom h has not been matched"
    # we check if student is free and if student prefers h over hospital they are assigned to, and reassign the student to h if so

    # STEP 2: Run Gale-Shapley algorithm
    while free_hospitals:
        hospital = free_hospitals.pop(0)
        top_student = hospital_ranks[hospital][0]
        hospital_ranks[hospital].pop(0) # prevent re-assignment to same student
        
        if(assignment_of_s[top_student] == 0): # if student is free
            assignment_of_s[top_student] = hospital
            assignment_of_h[hospital] = top_student
        elif(student_ranks[top_student][hospital] < student_ranks[top_student][assignment_of_s[top_student]]): # if student is not free but prefers new hospital over their current
            assignment_of_s[top_student] = hospital
            assignment_of_h[hospital] = top_student
            free_hospitals.append(assignment_of_s[top_student])
        else: # if student prefers their current hospital over new hospital
            pass

        # for i in range(length): # loop through all hospitals
        #     if(assignments[i] == 0): # if 0 then no student was assigned yet to hospital i
        #         all_assigned = False

        #         # Part 1, initial if
        #         allocated = False
        #         # loop through assigned students
        #         for student in assignments:
        #             if(hospital_ranks[i][0] == student): # if top student in hospital i's rank list is already assigned to a hospital
        #                 allocated = True

        #         if(not allocated):
        #             assignments[i] = hospital_ranks[i][0]
        #             continue

        #         # Part 2, else if


        all_assigned = True
    
    print(assignment_of_h)
    print(assignment_of_s)


# TODO: Output
    # Note, array index starts at 0, hospital/student numbers begin at 1. Just add 1.
