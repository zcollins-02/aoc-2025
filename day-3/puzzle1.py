total_joltage = 0

with open("input.txt", "r") as f:
    for line in f:
        for i in reversed(range(11, 100)):
            string_num = str(i)
            first_num = string_num[0]
            second_num = string_num[1]

            found_first_num = False
            found_second_num = False

            print("try to find num: " + string_num)

            for current_num in line:
                #print("current_num: " + current_num)
                if not found_first_num and first_num == current_num:
                    print("Found first num: " + current_num)
                    found_first_num = True
                elif found_first_num and second_num == current_num:
                    print("Found second num: " + current_num)
                    found_second_num = True
                    break

            if found_second_num:
                total_joltage += i
                break


print("Your total joltage is: " + str(total_joltage))
