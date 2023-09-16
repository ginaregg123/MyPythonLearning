print('\nSoal 1')
#Complete the code to output the statement, “Diego’s favorite food is lasagna”.
#Remember that precise syntax must be used to receive credit.

name = "Diego"
fav_food = "lasagna"
print(name + "’s favorite food is " + fav_food)

print('\nSoal 2')

#Consider the following scenario about using if-elif-else statements:
#Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score".
#Fill in the blanks in this function so that it returns the appropriate "Pass", "Fail", or "Top Score" grade.

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65)) # Should print Pass
print(exam_grade(55)) # Should print Fail
print(exam_grade(60)) # Should print Pass
print(exam_grade(95)) # Should print Pass
print(exam_grade(100)) # Should print Top Score
print(exam_grade(0)) # Should print Fail

print('\nSoal 3')
#What's the value of the comparison in this if statement? Hint: The answer is not what the code will print.

n = 4
if n*6 > n**2 or n%2 == 0:
    print("Check")

#answer : True

print('\nSoal 4')

#Fill in the blanks to complete the function. The character translator function receives a single lowercase letter, then prints the numeric location of the letter in the English alphabet.
#For example, “a” would return 1 and “b” would return 2. Currently, this function only supports the letters “a”, “b”, “c”, and “d” It returns "unknown" for all other letters or if the letter is uppercase.

def letter_translator(letter):
    if letter == "a":
      letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown

print('\nSoal 5')
def sum(x, y):
    return (x + y)

print(sum(sum(1, 2), sum(3, 4)))

print('\nSoal 6')
#What's the value of this Python expression?
#((10 >= 5*2) and (10 <= 5*2)))

#answer : 10

print('\nSoal 7')
#Fill in the blanks to complete the “safe_division” function. The function accepts two numeric variables through the function parameters and divides the “numerator” by the “denominator”.
#The function’s main purpose is to prevent a ZeroDivisionError by checking if the “denominator” is 0. If it is 0, the function should return 0 instead of attempting the division.
# Otherwise all other numbers will be part of the division equation. Complete the body of the function so that the function completes its purpose.

def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator  == 0:
        return 0
    else:
        # Complete the division equation.
        result = numerator / denominator
    return result


print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0