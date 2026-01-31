import matplotlib.pyplot as plt
from Runtime_Tester import test_runtime
if __name__ == "__main__":
    # Plot runtime of gale shapley algorithm
    lengths, runtimes, v_runtimes = test_runtime(10)
    plt.plot(lengths, runtimes)
    plt.xlabel('Length (n hospitals/students)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Gale-Shapley Runtimes')
    plt.show()

    plt.plot(lengths, v_runtimes)
    plt.xlabel('Length (n hospitals/students)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Verification Runtimes')
    plt.show()