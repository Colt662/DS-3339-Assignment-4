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


#Reflection:
#I didn't choose the most stimulating option for this challenge, as it didn't require choosing a data structure, it just required 2 variables. If I had to make this problem use a data structure, I would have used lists, since the input and output would have to be ordered to make sense, and values would only ever be added to the back, and never removed. 
#(While typing this reflection I realized I might have misinterpreted what this problem was asking for, and it might have wanted me to keep a list of the inputs and outputs. If this was the case however, my code wouldn't be much different, as I would have simply added the input_value to a input_value_list if it was valid, and would have added the running_total to output_value_list instead of printing it.)
#The time limit didn't shape my choice of data structure much, as I knew it was a simple enough problem that I would be able to complete it in time. I wasn't pressured by time too much, and even tried to see if I could do 2 problems in the time limit, but I wasn't able to finish the 2nd problem (commented out below). I wasn't able to take the time to more thoroughly evaluate how efficient my solution was, but it would be bottlenecked by user input anyways. I didn't make any intentional compromises in my design.
#Since there isn't much to say about the problem I did complete, I'll say what I was going to do for the second problem. For the second problem I was going to use a list, since it would be required to be ordered, and values would never be removed. I was more pressured by time for this problem, since I only had ~10 minutes left when I started it. I was considering how I would achieve the shift, and considered making a list of 0s and shifting the index where I would start to add values. Even though I believe that solution would have worked, having to create an empty list before populating it felt like too much of a compromise for time. I then considered shifting where I started pulling values from the input list, but ran out of time before I could implement it.

#What got completed for the 2nd problem
"""
    #1. Rotate Right
    #Rotate the values in a collection to the right by k steps.
    #Input: [1, 2, 3, 4, 5], k = 2
    #Output: [4, 5, 1, 2, 3]

    input_list = [1, 2, 3, 4, 5]
    valid_k = False

    while valid_k != True:
        input_k = input("Please enter an integer value to rotate a list to the right: ")

        try:
            input_k = int(input_k)
            valid_k = True

        except (ValueError):
            print(ValueError)
            print("Plese enter a valid number")
            continue

    output_list = []
    
"""
#Roughly what I would have done
"""
    def index_overflow(index, length):
        return index % (length)

    index_shift = len(input_list)
    index_shift = index_shift - input_k
    for i in range(len(input_list)):
        output_list.append(input_list[index_overflow(index_shift + i, len(input_list))])

    print(f'Original List: {input_list}')
    print(f'Shifted List:  {output_list}')

"""
    
    