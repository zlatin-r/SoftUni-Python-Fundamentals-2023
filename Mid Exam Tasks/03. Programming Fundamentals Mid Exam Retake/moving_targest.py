targets = [int(x) for x in input().split(" ")]
result_targets = []

while True:
    command = input().split(" ")
    action = command[0]

    if action == "End":
        break

    elif action == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index <= len(targets) - 1:
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if index - radius >= 0 and index + radius <= len(targets) - 1:
            for i in range(len(targets)):
                if index - radius <= i <= index + radius:
                    pass
                else:
                    result_targets.append(targets[i])
            targets = result_targets
        else:
            print("Strike missed!")
            continue

print("|".join(str(x) for x in targets))