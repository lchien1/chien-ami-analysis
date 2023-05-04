def read_forms():
    path = "output/output.txt"
    analyses = {}
    with open(path) as f:
        for line in f:
            form = line.split(':')
            analyses[form[1].strip()] = form[0]
    return analyses

def main():
    analyses = read_forms()
    while 1:
        word = input("Input Word: ")
        try:
            print(analyses[word])
        except:
            pass 

main()
