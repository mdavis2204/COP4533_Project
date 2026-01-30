# Read single number from file
def read_num(file):
    out_str = ''
    while True:
        temp = file.read(1)
        print(f"Temp: {temp}")
        if temp == '' or temp == ' ' or temp == '\n':
            break
        else:
            out_str += temp
    return int(out_str) - 1 # subtract 1 to convert to 0-indexed array

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
    print(f"Assignments of H: {convert_to_1_index(assignment_of_h)}")
    print(f"Assignments of S: {convert_to_1_index(assignment_of_s)}")

# TODO: Output
    # Note, array index starts at 0, hospital/student numbers begin at 1. Just add 1.
