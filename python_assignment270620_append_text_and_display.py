def file_read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write('file1\n')
    txt = open(fname)
    print(txt.read())
file_read('file1.txt')
    