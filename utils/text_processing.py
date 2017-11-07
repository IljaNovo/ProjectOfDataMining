def remove_comments(file):
    file2 = list()
    lst = to_array(file)
    for line in lst:
        if(line[0] != '#'):
            file2.append(line)
    return file2
def to_array(str):
    i = 0
    line = ""
    lst = list()
    for a in str :
        if(a != '\n') :
            line = line + a
        else:
            lst.append(line)
            line = ""
    lst.append(line)
    return lst