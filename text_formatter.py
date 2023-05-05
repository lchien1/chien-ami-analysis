from re import findall
from os import listdir

# NOTE: ay, aw, en, an are suffixes and will be at the end of the list!!!

def letter_changer(parts, stripped):
    if stripped[0][0] == 'A':
        temp = stripped[0].replace('A','a',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('A','',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'N':
        temp = stripped[0].replace('N','n',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('N','',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'M':
        temp = stripped[0].replace('M','m',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('M','n',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'T':
        temp = stripped[0].replace('T','t',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('T','k',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('T','c',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'L':
        temp = stripped[0].replace('L','t',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('L','l',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'K':
        temp = stripped[0].replace('K','k',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('K','c',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'C':
        temp = stripped[0].replace('C','c',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('C','k',1)
        parts.append([temp] + stripped[1:])
    elif stripped[0][0] == 'G':
        temp = stripped[0].replace('G','ng',1)
        parts.append([temp] + stripped[1:])
        temp = stripped[0].replace('G','',1)
        parts.append([temp] + stripped[1:])


def letter_alternater(parts,stripped):
    if stripped[0][0] in ('o','u'):
        parts.append(['o'] + stripped[1:])
        parts.append(['u'] + stripped[1:])
    elif stripped[0][0] == 'f':
        parts.append(['f'] + stripped[1:])
        parts.append(['v'] + stripped[1:])
        parts.append(['b'] + stripped[1:])
    elif stripped[0][0] in ('r','l'):
        parts.append(['r'] + stripped[1:])
        parts.append(['l'] + stripped[1:])


def line_splitter(path):
    with open(path) as f:
        lines = [line for line in f]
    parts = []
    for line in lines:
        line = line.partition('#')[0]
        stripped = findall(r"[\w']+", line)
        if stripped[0] == stripped[1]:
            stripped.pop(0)
        if stripped[0][0] < 'a': # if capital letter
            letter_changer(parts,stripped)
        #elif stripped[0][0] in ['o','u','f','r','l']:
            #letter_alternater(parts,stripped)
        else:
            parts.append(stripped)
    return parts


def txt_write(lines, path):
    with open(path, "w+") as f:
        for line in lines:
            f.write(','.join(line)+'\n')

def main():
    dir_list = listdir("txts/lexd_style/")
    for fname in dir_list:
        data = line_splitter("txts/lexd_style/" + fname)
        txt_write(data, "txts/new_style/" + fname)

main()
