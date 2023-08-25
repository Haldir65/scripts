import os


def write_list_to_file_override(file_path, lines):
    with open(file_path, 'w') as f:
        f.write(os.linesep.join(str(item) for item in lines))
        

        # for line in lines:
        #     f.write(f"{line}\n")


def write_list_to_file_append(file_path, lines):
    with open(file_path, 'a') as f:
        f.write(os.linesep)
        f.write(os.linesep.join(str(item) for item in lines))
        # for line in lines:
        #     f.write(f"{line}\n")            


def _read_all_content_of_a_file_line_by_line(path):
    # removing the new line characters
    with open(file=path) as f:
        lines = [line.rstrip() for line in f]
        return lines        