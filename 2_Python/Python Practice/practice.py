string = ["hello", "world", "good", "day"]
float = [6.2, 1, 4, 5.2]
int = [3, 4, 5, 6]

# new = zip(string, float, int)
# print (list(new))

for string, float, int in zip(string, float, int):
    print(string, float, int)

# name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
# roll_no = [ 4, 1, 3, 2 ]
# marks = [ 40, 50, 60, 70 ]
