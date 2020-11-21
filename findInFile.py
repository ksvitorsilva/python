def findInFile(username):
    with open('PERFIS.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if str(username + ':') in line:
            return line
    return None
