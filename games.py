def main():

# Question 1

    score_count = 0
    question = ("What color is red?").upper()
    answer_1 = "1. red"
    answer_2 = "2. green"
    answer_3 = "3. yellow"
    answer_4 = "4. pink"
    print(question, answer_1, answer_2, answer_3, answer_4, sep='\n')
    user_answer = input("Choose 1-4: ")
    if user_answer == '1':
        score_count += 1 
        print("Correct!")
    else:
        print("Incorrect")    

# Question 2

    question = ("What color is pink?").upper()
    answer_1 = "1. red"
    answer_2 = "2. green"
    answer_3 = "3. yellow"
    answer_4 = "4. pink"
    print(question, answer_1, answer_2, answer_3, answer_4, sep='\n')
    user_answer = input("Choose 1-4: ")
    if user_answer == '4':
        score_count += 1
        print("Correct!")
    else:
        print("Incorrect")

# Question 3

    question = ("What color is green?").upper()
    answer_1 = "1. red"
    answer_2 = "2. green"
    answer_3 = "3. yellow"
    answer_4 = "4. pink"
    print(question, answer_1, answer_2, answer_3, answer_4, sep='\n')
    user_answer = input("Choose 1-4: ")
    if user_answer == '2':
        score_count += 1
        print("Correct!")
    else:
        print("Incorrect")
   
# Question 4

    question = ("What color is yellow?").upper()
    answer_1 = "1. red"
    answer_2 = "2. green"
    answer_3 = "3. yellow"
    answer_4 = "4. pink"
    print(question, answer_1, answer_2, answer_3, answer_4, sep='\n')
    user_answer = input("Choose 1-4: ")
    if user_answer == '3':
        score_count += 1
        print("Correct!")
    else:
        print("Incorrect")

    percent_correct = (score_count / 4) * 100
    print(f"You got {score_count} correct!  Your grade is {percent_correct}% ")

             
if __name__ == "__main__":

    main()