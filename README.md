# **Word and Character Counter**

#### **Task 11 - Python Programming Internship:**



This project is a simple Python program that accepts a paragraph from the user and calculates the number of characters, words, sentences, and spaces in the given paragraph.



###### **Objective:**



The objective of this task is to practice:



1. String manipulation
2. `len()` function
3. `split()` function
4. `count()` function
5. User input
6. Basic text processing
7. Conditional statements



###### **Technologies Used**



Python



###### **Program**



t=input("Enter a paragraph: ")

if t=="":

&#x20;   print("No text entered.")

else:

&#x20;   c= len(t)

&#x20;   w= len(t.split())

&#x20;   sp=t.count(" ")

&#x20;   s=t.count(".")+t.count("!")+t.count("?")

&#x20;   print("\\nText Statistics")

&#x20;   print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

&#x20;   print("Characters:",c)

&#x20;   print("Words:",w)

&#x20;   print("Sentences:",s)

&#x20;   print("Spaces:",sp)



###### **How the Program Works**

**1. Get Paragraph from User**

The input() function is used to accept a paragraph from the user.

t=input("Enter a paragraph: ")

The paragraph is stored in the variable t.


**2. Check Empty Input**

if t=="":    print("No text entered.")

This checks whether the user entered an empty paragraph.



**3. Count Characters**

c=len(t)

The len() function counts the total number of characters in the paragraph, including spaces and punctuation marks.



**4. Count Words**

w=len(t.split())

The split() function separates the paragraph into words, and len() counts the number of words.

5\. Count Spaces

sp=t.count(" ")

The count() function counts the number of spaces in the paragraph.



**6. Count Sentences**

s=t.count(".")+t.count("!")+t.count("?")

The program counts ., !, and ? as sentence-ending punctuation marks.



**7. Display the Results**

The calculated values are displayed using the print() function.





###### 

**Sample Output:**
Enter a paragraph: I am Madeena Beebi. I am completed Task 11 in python internship.!

Text Statistics

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Characters: 65

Words: 12

Sentences: 3

Spaces: 11



###### **Concepts Used**

* input()
* if-else
* Strings
* len()
* split()
* count()
* String manipulation
* Basic text processing


###### **Conclusion**

The Word and Character Counter is a simple Python text-processing program. It accepts a paragraph from the user and calculates characters, words, sentences, and spaces. This task helped me understand basic string functions and text manipulation in Python.

