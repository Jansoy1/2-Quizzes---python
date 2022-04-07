import time
#2 quiz game
time.sleep(1)
print("hello, welcome to a 2 quiz game. You'll have the choice to choose from one or the other quiz to take, or you can take both quizes\n")
time.sleep(1)
name = input("Before we start, please enter your name: ")
time.sleep(1)
print("")
print("Welcome " +name)
print("")
time.sleep(1)
choose_quiz = input("which quiz would you like to start with? 1/2: ")

def one_or_two():
	while choose_quiz == "1":
		print("")
		print("Quiz one will start now\n")
		time.sleep(1)
		return start_quiz_one()
	while choose_quiz == "2":
		print("")
		print("Quiz two will start now\n")
		time.sleep(1)
		return start_quiz_two()


#quiz one
def start_quiz_one():
	point_q1 = 0
	incorrect_q1 = 0
	total_questions_q1 = 3
	print("Quiz one")
	for key in questions_quiz_one:
		print("----------")
		answer_q1 = input(key)
		if answer_q1 == questions_quiz_one.get(key):
			print("------")
			print("Correct")
			point_q1 = point_q1 + 1
			print("-------")
			
		else:
			print("-------")
			print("Incorrect, the correct answer is...... " +questions_quiz_one.get(key))
			print("-------")
			incorrect_q1 = incorrect_q1 + 1
			
	display_socres_q1(point_q1, incorrect_q1, total_questions_q1)		
		
		
	
	

#quiz 2

def start_quiz_two():
	point_q2 = 0
	incorrect_q2 = 0
	total_questions_q2 = 3
	print("Quiz two")
	for key2 in questions_quiz_two:
		print("----------")
		answer_q2 = input(key2)
		if answer_q2 == questions_quiz_two.get(key2):
			print("------")
			print("Correct")
			point_q2 = point_q2 + 1
			print("------")
		else:
			print("------")
			print("Incorrect, the correct answer is...... " +questions_quiz_two.get(key2))
			incorrect_q2 = incorrect_q2 + 1
			print("------")


	display_socres_q2(point_q2, incorrect_q2, total_questions_q2)






def display_socres_q1(point_q1, incorrect_q1, total_questions_q1):
	time.sleep(1)
	print("Calculating your results for quiz 1 .......")
	time.sleep(1)
	print("...........")
	time.sleep(1)
	total_results_q1 = int((point_q1/total_questions_q1)*100)
	print("Total correctly answered = " +str(point_q1))
	print("Toatl incorrectly answered = " +str(incorrect_q1))
	print("you scored = " +str(total_results_q1)+"%")
	if total_results_q1 >= 70:
		print("You have passed!!!")
	else:
		print("You have failed! The pass rate is 70%")
	time.sleep(1)
	play_again_q1 = input("Would you like to play again or move to quiz 2? : Again/Move/Quit: ").lower()
	while play_again_q1 == "again":
		return start_quiz_one()
	while play_again_q1 == "move":
		return start_quiz_two()
	while play_again_q1 == "quit":
		return end_game()
	
def display_socres_q2(point_q2, incorrect_q2, total_questions_q2):
	time.sleep(1)
	print("Calculating your results for quiz 2 .......")
	time.sleep(1)
	print("...........")
	time.sleep(1)
	total_results_q2 = int((point_q2/total_questions_q2)*100)
	print("Total correctly answered = " +str(point_q2))
	print("Toatl incorrectly answered = " +str(incorrect_q2))
	print("you scored = " +str(total_results_q2)+"%")
	if total_results_q2 >= 70:
		print("You have passed!!!")
	else:
		print("You have failed! The pass rate is 70%")
	time.sleep(1)
	play_again_q2 = input("Would you like to play again or move to quiz 1? : Again/Move/Quit: ").lower()
	while play_again_q2 == "again":
		return start_quiz_two()
	while play_again_q2 == "move":
		return start_quiz_one()
	while play_again_q2 == "quit":
		return end_game()

def end_game():
	time.sleep(1)
	print("Byee!")
	time.sleep(1)
	quit()

#would you like to play again?
#which quiz would you like to start






questions_quiz_one = {"1. In which part of your body would you find the cruciate ligament? ":"knee",
		      "2. What is the name of the main antagonist in the Shakespeare play Othello? ": "lago",
		      "3. What element is denoted by the chemical symbol Sn in the periodic table? ":"tin"}
questions_quiz_two = {"1. What is four-fifths as a decimal? ":"0.8",
		      "2. What is the next number in the series: 2, 9, 30, 93, …? ": "282",
		      "3. A dress has a thirty percent discount applied and is on sale for £63. What was the original price of the dress before the reduction? #No need to use £ just number# ":"90"}


one_or_two()
start_quiz_two()
start_quiz_one()
display_socres_q1()
	##
