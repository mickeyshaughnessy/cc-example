# This problem is difficult to parallelize, since the running
# median at any step is depedent on the running median of the 
# previous step. The solution implemented here is a serial
# algorithm that is reasonably efficient and uses a dictionary
# of counts to compute the running median

import sys

# Parameter specifying the maximum line length (# of characters) in the input
# files. Lines longer than this will be counted as having length = MAX_LIN_LEN
# This parameter defines the memory footprint. Alternately, we could use a 
# defaultdict, but this could grow arbitrarily large, depending on the line
# lengths.
MAX_LINE_LEN = 10000

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    if len(lst) %2 == 0:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

def make_median_counter():
    counts = {}
    for x in range(0,MAX_LINE_LEN*10):
        counts[x/10.0] = 0
    return counts

def compute_running_median(counts, infile):
    for line in open(infile, 'r'):
        counts[len(line.split())] += 1
        maximum = max(counts.values())
        median_cands = [l for l, count in counts.items() if count == maximum]
        cur_median = int((median(median_cands) * 10)) / 10.0 
        # The line above produces a single digit after the decimal: 8.666 -> 8.6 
        
        outfile.write('%s\n' % (cur_median))
        
if __name__ == '__main__':
    outfile = open('wc_output/'+sys.argv[1], 'w')
    sorted_files = sorted([s.replace('wc_input/', '') for s in sys.argv[2:]])
    counts = make_median_counter()
    for infile in sorted_files:
        print infile
        compute_running_median(counts, 'wc_input/'+infile)

