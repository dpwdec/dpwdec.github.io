file_path = "./update.txt"

number = int(open(file_path).read()) + 1

with open(file_path, "w") as target:
    target.write(str(number))