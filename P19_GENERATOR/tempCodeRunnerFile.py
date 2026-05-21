def read(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("File not found")

for i in read("python.txt"):
    print(i)