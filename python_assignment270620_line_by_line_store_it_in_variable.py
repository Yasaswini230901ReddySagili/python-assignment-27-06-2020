def file_name(fname):
    with open(fname,"r") as myfile:
        data=myfile.readlines()
        print(data)
file_read('file.txt')