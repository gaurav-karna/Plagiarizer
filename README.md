# Plagiarizer Coding Challenge
Submitted to TripAdvisor Software Engineering Challenge on Sept 7, 2019

## Assumptions
- [x] Percentage of similar tuples takes into account if the files are different lengths. For example, if no more tuples of length N can be constructed from file two, then file one tuples still get constructed, and ```TOTAL_TUPLE_COUNT``` is still incremented, even though there is no checking for plagiarism done.
- [x] Files will be in the same directory as the script
- [x] Optimizing for speed rather than memory - explains the global variables, choice of dictionary (rather than consistent list iteration), etc.

## Run
You can run the script as: ```python3 main.py -s syns.txt --fileone fileA.txt --filetwo fileB.txt```, and add an extra ```-t``` flag to indicate a different tuple length.
