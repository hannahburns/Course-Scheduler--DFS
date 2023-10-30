# Learning Data Structures and Algorithms with Course Scheduler

The primary objective of tis project is to familiarize myself wit and demonstate the Depth-First Search algorithm. 

The program employs the Depth-First Search (DFS) algorithm to determine the ideal order for taking classes within the context of a class scheduling project. DFS is a systematic exploration method. It begins by processing the user's input text file, parsing the data line by line, and organizing it into an array named 'lines.' Each line corresponds to a class, along with its associated prerequisites, separated by colons. 

DFS operates by iteratively examining each class in the 'classlist.' When a class has already been visited (indicated in the 'visited' array), it is bypassed. If a class hasn't been visited and has no prerequisites, it is directly added to the 'visited' array. Conversely, if the class has prerequisites, DFS employs recursion to delve deeper into the prerequisites, making sure each prerequisite is covered before moving on to the class itself.

After DFS has traversed the classes and prerequisites, the 'visited' array contains the recommended order in which to take the classes. This sequence is then written to the output text file. Essentially, DFS methodically explores the labyrinth of class prerequisites, ensuring that you follow a logical and optimized path when scheduling your classes.

## Prerequisites

Before you get started, make sure you have Python installed on your computer. You can download and install Python from the official [Python website](https://www.python.org/downloads/).

## Getting Started

1. Clone or download this project to your local machine.

2. Create an input file named `input.txt` with your class data. Each line should be in the following format:
   ```
   ClassName: Prerequisite1 Prerequisite2 Prerequisite3
   ```

   Example:
   ```
   Algebra: 
   Calculus: Algebra
   Geometry: Algebra
   Biology: Chemistry
   Chemistry: 
   ```

   This example represents a set of classes and their prerequisites.

3. Files `make.sh` and `run.sh` are provided to help complie and run the program with its simple calls in your bash.

4. The script will generate an output file named `output.txt` containing the recommended order in which to take the classes.

## Script Explanation

The Python script `course_scheduler.py` contains the following components:

- `dfs(prereq, visited, c)`: This is a recursive function that performs depth-first search to determine the order of classes to take based on prerequisites.

- Reading and writing input and output files:
  - `file = open('input.txt', 'r')`: Opens the input file for reading.
  - `output = open('output.txt', 'w')`: Creates an output file for writing the recommended class order.

- Data structures:
  - `prerequisites`: A dictionary that pairs classes (keys) with lists of requirements (values).
  - `classlist`: An array of all class names.
  - `visited`: A list of taken classes in the recommended order.
  - `prio_class` and `prio`: Variables to keep track of the class with the highest number of prerequisites.

- Data Preparation:
  - The script reads the input file line by line, splits each line to separate class names and prerequisites, and populates the `prerequisites` dictionary.

- DFS:
  - The script runs the `dfs` function for each class to determine the recommended order.

- Writing the Output:
  - The script writes the recommended class order to the output file.

## Viewing Data (Optional)

If you want to view how the data looks after preparing, you can uncomment the following lines in the script:
```python
# print(prerequisites)
# print(classlist)
```

## Acknowledgements

This project is designed for educational purposes to help learn data structures and algorithms. It demonstrates the use of depth-first search to solve a class scheduling problem. You can modify the input data in `input.txt` to experiment with different class prerequisites and see how the script generates a recommended order.

## License

Copyright © Hannah Burns 2023

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

This means that you are free to:

- Share — You can copy and redistribute the material in any medium or format.

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- NonCommercial — You may not use the material for commercial purposes.

- NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified material.

You are free to use this work for personal and educational purposes, but you may not use it for commercial gain, and you cannot create derivative works based on it without permission.


