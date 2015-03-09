Word Count with Python + mrjob & Running Median Line Length 
===========================================================

This directory a pair of programs to analyze text files.

The first program uses the MapReduce paradigm, as implemented in
the mrjob Python library, to count the occurences of all words in a 
set of files. MapReduce allows files to be processed in parallel,
with no communication between nodes during processing. The mrjob library is
chosen because it is fairly commonly used for Python MapReduce jobs and
because it can run the actual job locally, on a Hadoop cluster, or an Amazon Elastic 
MapReduce. The current program is set to run on a single processor - see
![python mrjob user guide](https://pythonhosted.org/mrjob/guides/quickstart.html#running-your-job-different-ways)
for additional options for larger jobs. 

The second program computes a running median line length for the same 
files, when the files are proccessed in alphabetical order according to 
their names. In this case the task is difficult to parallelize because
the running median for line l+1 of a file is dependent on the lengths of
the l lines before it. These lines could be stored in memory, but if the
size of the input files is very large, this may not be feasible. Alternately,
a pair of minHeap and maxHeap structures or a counting sort could be used.
In this solution I build a histogram of lengths and extract its maximum using
the standard python max function, which is O(k), where k is the number of
elements in the list. In this case `k = MAX_LINE_LEN`. This solution is chosen
because it allows for a very simple program whose runtime can be linear in the 
size of the input files.

Running the scripts
-----------------------
The only dependency is the mrjob library, which is installed automatically
when the user runs the `run.sh` script. Alternately, the command
    pip install mrjob
can be used to install mrjob. 

Typing
    bash run.sh
into the command line will run the jobs and produce output. The root password may
be requested in order to ensure the mrjob library is installed. This section of the `run.sh`
script can be ommitted (and the script run without sudo privileges) if mrjob is already installed. 

Inputs are located in the `wc_input/` directory - all files in this directory are processed. Outputs are
in the `wc_output` directory, called `wc_result.txt` and `med_result.txt`.
