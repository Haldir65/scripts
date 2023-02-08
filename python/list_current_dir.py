import os



def _read_all_content_of_a_file_line_by_line(path):
    # removing the new line characters
    with open(file=path) as f:
        lines = [line.rstrip() for line in f]
        return lines


def main():
    pwd = os.getcwd()
    files = os.listdir(pwd)
    filterd = [f for f in files if os.path.isfile(pwd+'/'+f) and not os.path.isdir(pwd+'/'+f)] #Filtering only the files.
    for f in filterd:
        wd = _read_all_content_of_a_file_line_by_line(f)
        for w in wd:
            print(w)
        # print(len(wd))
        # print(f)
        # print(*files, sep="\n")







if __name__ == '__main__':
    main()