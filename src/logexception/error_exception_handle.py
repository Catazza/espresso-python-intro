# Error & Exception handling

if __name__ == "__main__":
    f = open('example1.log')
    s = f.readline()
    i = int(s.strip())
    f.close()
