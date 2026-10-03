# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#2. Running Total with Reset
#Track a running total of values. If a negative number is added, reset the total to 0.
#Input: [5, 7, -1, 3, 2]
#Output: [5, 12, 0, 3, 5]





if __name__ == "__main__":
    input_value = 0
    running_total = 0
    while input_value != "q":

        input_value = input("Please enter a positive number to be added to a total, a negative number to reset the total, or q to exit: ")

        if  input_value.lower() == "q":
            break

        else:
            try:
                input_value = float(input_value)#uses float just in case someone wants to input decimal values

            except (ValueError):
                print("Plese enter a valid number or q")
                continue


            if input_value >= 0:
                running_total = running_total + input_value

            else:
                running_total = 0

            print(f'Running total: {running_total}\n')

