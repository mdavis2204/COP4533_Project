from Gale_Shapley import gale_shapley, verification
import time


def generate_normal_ranks(length):
    # Generates normal ranks for hospitals and students
    # Example:
    # 1 2 3
    # 1 2 3
    # 1 2 3
    # for length 3
    # or
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # for length 5
    # and so on
    preference_ranks = [] # preference_ranks can be used for either hospitals or students
    for i in range(length):
        # hospital ranks are just the numbers 1 to length in order to keep it simple
        preference_ranks.append(list(range(length)))
    return preference_ranks

if __name__ == "__main__":
    # Test with lengths n = n*2, starting at n = 2
    for length in [2**i for i in range(1, 10)]:
        hospital_ranks = generate_normal_ranks(length)
        student_ranks = generate_normal_ranks(length)

        # Get clock time before and after running Gale-Shapley algorithm
        start_time = time.perf_counter()
        assignment_of_h, assignment_of_s = gale_shapley(hospital_ranks, student_ranks, length, False)
        end_time = time.perf_counter()

        runtime = end_time - start_time
        print(f"Runtime for n = {length}: {runtime} seconds")

    print("Runtime Test Complete")