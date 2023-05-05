from sys import argv
from re import findall
import time
import resource


def read_corpus(path):
    with open(path) as f:
        words = set()
        #lstwords = tuple()
        for line in f.read().splitlines():
            words.update(findall(r"[\w']+", line))
            #words+=tuple(findall(r"[\w']+", line))
    return words # words


def check_coverage(corpus_path):

    words = read_corpus(corpus_path)
    path = "../output/output.csv"
    with open(path) as f:
        forms = tuple(row.split(',')[0] for row in f)
    #print(forms[-1])
    yes = 0
    #print(words)
    for word in words:
        if word in forms:
            yes += 1
    return yes, len(words)


def main():
    time_start = time.perf_counter()

    yes, length = check_coverage(argv[1])

    time_elapsed = (time.perf_counter() - time_start)
    memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

    print(f"coverage:{yes}/{length}")
    print ("%5.1f secs %5.1f MByte" % (time_elapsed,memMb))



main()
