name = input("Enter your name: ")
money = 1500 # in EUR
german_level = ["A1", "A2", "B1", "B2", "C1", "C2"]
status = "language learner"

print(f"My name is {name} and my job is {status}.")

player = {
    "name": name,
    "german_level": german_level.index("A1"),
    "money": money
}