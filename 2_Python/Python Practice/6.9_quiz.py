# name = input("Enter names separated by commas: ")
# assignments = int(input("Enter assignments separated by commas: "))
# grade = float(input("Enter grades separated by commas: "))



name = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignments separated by commas: ").split(",")
grade = input("Enter grades separated by commas: ").split(",")


message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignments, grade in zip(name, assignments, grade):
    print(message.format(name, assignments, int(grade), int(grade) + int(assignments) * 2))
