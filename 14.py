# 1.) FizzBuzz Challenge. Write a program that prints 
# numbers from 1 to 50

import string
class Solution:
    def __init__(self):
        self.challenge_one = []
        self.challenge_two = 0
        self.challenge_three = []
        self.challenge_four = 0
        self.challenge_five = {} # grade and score
        self.challenge_six = 0 #consonants count
        self.challenge_seven = False # is_palindrome
        self.challenge_eight = {} # word frequency counter
    
    def fizz_buzz(self, num):
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.challenge_one.append("FizzBuzz")
            elif i % 3 == 0:
                self.challenge_one.append("Fizz")
            elif i % 5 == 0:
                self.challenge_one.append("Buzz")
            else:
                self.challenge_one.append(i)
    
    def sum_even_numbers(self, num):
        total = 0
        for i in range(2, num + 1, 2):
            total += i
        self.challenge_two = total
    
    def reverse_a_word(self, word):
        self.challenge_three = list(word[::-1])
    
    def count_vowels_in_word(self, word):
        vowels =  ["a", "e", "i", "o", "u"]
        count = 0
        for i in word.lower():
            if i in vowels:
                count += 1
        self.challenge_four = count
     
    def check_grade(self, score):
        if score >= 90:
            self.challenge_five["grade"] = "A"
            self.challenge_five["score"] = score
        elif score >= 80 and score <= 89:
            self.challenge_five["grade"] = "B"
            self.challenge_five["score"] = score
        elif score >= 70 and score <= 79:
            self.challenge_five["grade"] = "C"
            self.challenge_five["score"] = score
        elif score >= 60 and score <= 69:
            self.challenge_five["grade"] = "D"
            self.challenge_five["score"] = score
        else:
            self.challenge_five["grade"] = "F"
            self.challenge_five["score"] = score
    
    def count_consonants_in_word(self, word):
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
        for i in word.lower():
            if i.isalpha() and i not in vowels:
                count += 1
        self.challenge_six = count
    
    def is_palindrome(self, word):
        self.challenge_seven = list(word) == list(word[::-1])
    
    def word_frequency_counter(self, sentence):
        my_list = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for i in my_list:
            if i in self.challenge_eight:
                self.challenge_eight[i] += 1
            else:
                self.challenge_eight[i] = 1
        
    def display_all(self):
        print("\n Challenge One: FizzBuzz")
        print(self.challenge_one)

        print("\n Challenge Two: Sum of Even Numbers")
        print(self.challenge_two)

        print("\n Challenge Three: Reverse a word")
        print(",".join(self.challenge_three))

        print("\n Challenge Four: Count vowels in word")
        print(self.challenge_four)

        print("\n Challenge Five: Check grade")
        print(f'{self.challenge_five["score"]} is {self.challenge_five["grade"]}')

        print("\n Challenge Six: Count consonants in word")
        print(self.challenge_six)

        print("\n Challenge Seven: Palindrome checker ")
        if solution.challenge_seven:
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")
        
        print("\n Challenge Eight: Word frequency counter")
        print(solution.challenge_eight)


if __name__ == "__main__":
    solution = Solution()
    num_1 = int(input("What is your input range for challenge one? "))
    solution.fizz_buzz(num_1)

    num_2 = int(input("What is your input range for challenge two? "))
    solution.sum_even_numbers(num_2)

    word = input("Enter the word you want reversed: ")
    solution.reverse_a_word(word)

    solution.count_vowels_in_word(word)

    score = int(input("What was your score? "))
    solution.check_grade(score)

    solution.count_consonants_in_word(word)

    solution.is_palindrome(word)

    sentence = input("Enter a sentence here: ")
    solution.word_frequency_counter(sentence)
    
    solution.display_all()