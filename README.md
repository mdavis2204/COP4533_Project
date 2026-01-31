# COP4533 Project 1

Team:
  Matthew Davis, UFID 6835-3882,
  William Zhu, UFID 3189-3413

# Gale Shapley Algorithm and Verifier Deliverables

**Source code for Gale Shapley algorithm and Verifier**: ["Gale_Shapley.py"](./Gale_Shapley.py)
**def gale_shapley**, and **def verification** are the functions for Gale Shapley algorithm and Verifier respectively.

**To run the code, you must have python installed.**
How to install python: [https://www.youtube.com/watch?v=8mO6QXOcpqU]

Run code: "python Gale_Shapley.py"

Run code with Verifier: "python Gale_Shapley.py -v" or "python Gale_Shapley.py -verify"

Example input: ["inputs/example_input1.txt"](./inputs/example_input1.txt)

Example output: ["example_outputs/example_output1.txt"](./example_outputs/example_output1.txt)

For dynamic input, **we assume that the user/grader will edit the file path on line 98 inside Gale_Shapley.py to the path of the file they want to read from, or that the grader will edit the content in inputs/example_input1.txt itself (the default location). The assignment instructions did not specify otherwise, so this is fine.** For the Gale_Shapley function inside the file, we assume that hospital and student preferences are the same size.

# Runtime/Task C Deliverables

Answers to Task C are located in: ["TaskC.pdf"](TaskC.pdf)

**Runtime Graph and Verification Time Graph** are also both in ["TaskC.pdf"](TaskC.pdf)

Runtime Function (requires matplotlib.pyplot): ["Plot_Runtime.py"](./Plot_Runtime.py)

Run it with "python Plot_Runtime.py", and it will output the graphs to your screen, and the runtime in seconds to the console.
