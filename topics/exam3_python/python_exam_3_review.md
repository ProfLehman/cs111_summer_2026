# Exam 3 covers Python programming and Ethics

* Students may use a 1-page (8.5” by 11” front/back) help guide on the exam
* Review class notes, examples on the course Moodle page, [Exam #3 (Python) - Reading and Resources](./exam3_python_resources.md), and Python assignments.

## Topics
* Current Ethical Issues (briefly describe several current examples)
* Ethical Analysis (facts, issues, people affected, consequences, faith/values) note: be able to list these questions that should be addressed  
* IPO (Input, Output, Processing) for planning
* single line comments # and multiple line comments """ """
* valid variable names (start with a letter, then letter, number, underscore)
* variable types number int (7, 2700, -8), float (3.14, -98.6), str ("abc", ‘abc’, "46750")
* use print to display text and variables on a single line, end=””
* use print formatting f”text {variable}” including formatting to one {v:.1f} or two{v:.1f} decimal places
* arithmetic operations (*, /, + -), order of precedence ie. parenthesis, exponents, mult/div, add/sub
* input values from keyboard using input statement and convert to int or float  
* if, else, relational operators (<, >, <=, >=, ==, !=), and, or)  
* generate random numbers 0 to N, 1 to N
* while loop, repeat code N times, sentinel loop  
* lists [], empty list, index list[n], append
* len, sum, min, max
* loop to print all items in a list

## Sample Questions


### 1. Current Ethical Issues
**Question:** Briefly describe several current ethical issues related to computing technology.

**Sample Answers:**
- The use of copyrighted content is an ethical issue because digital materials can be easily copied and shared without the creator’s permission. This can harm creators by reducing their ability to control and earn from their work. 
- AI bias in decision-making systems occurs when algorithms reflect or amplify biases present in their training data. This can lead to unfair or discriminatory outcomes, especially in areas like hiring, lending, or criminal justice. 
- Data privacy is a concern because companies often collect and track large amounts of personal information about users, sometimes without full transparency. This data can be used for targeted advertising or shared with others, raising concerns about consent and security.
- The use of AI in education raises concerns because students may use tools to complete assignments without actually learning the material. This can undermine academic integrity and make it difficult for instructors to accurately assess student understanding.

---

### 2. Ethical Analysis
**Question:** What questions should be addressed in an ethical analysis?

**Sample Answer:**
1. Identify the **facts** surrounding the issue 
2. Define the **issues** surrounding the issue 
3. Identify the **people/groups of people involved**
4. Describe **how each is affected** 
5. Identify the **options** for each group and the **consequences** of these options 
6. How do your **values and beliefs**, including your **religious faith**, affect your view of the issue? What **scripture or biblical principles apply** to this issue?
7. If confronted with this type of ethical situation/issue, **what would you do**?  

---

# Concepts

### 3. IPO Model
**Question:** What is an IPO chart? How is it used to assist the programming process?

**Sample Answer:**
An IPO chart describes:
- **Input** – data received  
- **Processing** – calculations/logic  
- **Output** – results displayed  

It helps plan programs before coding.

---

# Python Basics

### 4. Variable Names
**Question:** Which is NOT a valid variable name?

a. total1  
b. 1total  
c. total_score  
d. totalScore  

**Answer:** **b. 1total** (cannot start with a number)

---

### 5. Comments
**Question:** Which is a valid single-line comment?

a. //comment  
b. /* comment */  
c. #comment  
d. *** comment  

**Answer:** **c. #comment**

---

### 6. What will print to the screen when the following Python code is executed?
```python
a = 10
b = 20
print("a + b")
print(a + b)

amount = 7.4589
print(f"amount = ${amount:.2f}")
````

**Answer:**

```
a + b
30
amount = $7.46
```

---

### 7. Order of Operations

**Question: What value is assigned to x?**

```python
x = 40 - 20 / 4 * 5 + 3
print( x )
```

**Answer:**

* 20 / 4 = 5
* 5 * 5 = 25
* 40 - 25 + 3 = **18**

---

### 8. What will print to the screen when the following Python code is executed?

```python
temp = 2
temp = temp + 1

print(temp / 2) # _______

temp = temp + 3

print(temp) # ________
```

**Answer:**

```
1.5
6
```

---

### 9. Boolean Logic #1

**Question: What value will be displayed by the following code, given: a=10, b=20, c=30?**

```python
a = 10
b = 20
c = 30

if a > b or b < c:
     print("True")
else:
     print("False")
```

**Answer:** **True**

---

### 10. Boolean Logic #2

**Question: What value will be displayed by the following code, given: a=10, b=20, c=30?**

```python
a = 10
b = 20
c = 30

if c == 30 and b > c:
     print("True")
else:
     print("False")
```

**Answer:** **False**

---

### 11. Program Comments

**Question:** What comments should be included at the beginning of every program?**  

**Answer:**

* program name ie. exam3.py
* Author name ie. Norman Forester
* Date ie. April 30, 2026
* Purpose/Description of program ie. program calculates an average grade

---

# Coding Questions

### 12. Dessert Logic (individual ifs)

**Question: Implement the following logic using individual if statements. Remember that your code segment sets the
variable dessert to either “Cookie”, “Cake”, or “Pie” based on the value in variable choice. Your code segment
does not print anything. You are given the variable choice and variable dessert. You can assume the choice will either
be 1, 2, 3, 4, 5, 6, or 7.**  

| choice | dessert   |
|--------|----------|
| 1, 2, 3 | Cookie   |
| 4, 5      | Cake     |
| 6, 7      | Pie      |

### Complete code shown  
```python
choice = 4
dessert = "undefined"

# *** add if statements here 

print( "dessert is", dessert )
```


**Answer:**
```python
choice = 4
dessert = "undefined"

if choice == 1 or choice == 2 or choice == 3:
    dessert = "Cookie"

if choice == 4 or choice == 5:
    dessert = "Cake"

if choice == 6 or choice == 7:
    dessert = "Pie"

print( "dessert is", dessert )
```

---

### 13. Temperature Program

**Question: Show the code needed to input a temperature from the keyboard and print the message “above freezing” if
the temperature is greater than 32.0 and the message “freezing” if the temperature is equal to or below 32.0. 
Two sample runs are shown.**

Sample Run #1
```
Enter temperature: 17.5
17.5 is freezing
```

Sample Run #2
```
Enter temperature: 45.5
45.5 is above freezing **
```

**Answer:**

```python
temp = float(input("Enter temperature: "))

if temp > 32.0:
    print(f"{temp} is above freezing")
else:
    print(f"{temp} is freezing")
```

---

### 14. Random Number (0–3)

**Question: Complete the code segment such that a random integer number 0, 1, 2, or 3 will be stored in variable x**

```python
from random import randint

x = ____________________________________
```


**Answer:**
```python
from random import randint
x = randint(0, 3)
```

---

### 15. Random Number (17–19)

**Question: Complete the code segment such that a random integer number 17, 18, or 19 will be stored in variable x**

```python
from random import randint

x = ____________________________________
```

**Answer:**
```python
x = randint(17, 19)
```

---

### 16. Random Word

**Question: Show the code needed to set word randomly to “go”, “fight”, or “win” each time the code is executed.**

```python
from random import randint

# *** show code here ***



print(word)
```

**Answer:**
```python
from random import randint

r = randint(1, 3)

if r == 1:
    word = "go"
if r == 2:
    word = "fight"
if r == 3:
    word = "win"

print(word)
```

---

### 17. While Loop Output

**Question: What will be output by the following code snippet?**

```python
count = 0
while count < 4:
    print(count)
    count = count + 2
```

**Answer:**

```
0
2
```

---

### 18. Countdown

**Question: Show the python code needed to print the numbers 5,000 down to 1.**

**Answer:** 

```python
count = 5000
while count >= 1:
    print(count)
    count = count - 1
```

---

### 19. Repeat Name

**Question: Use a while loop to display your name ie. “Norman Forester” 3,000 times.**

**Answer:**
```python
count = 1
while count <= 3000:
    print("Norman Forester")
    count = count + 1
```

---

### 20. Sentinel Loop

**Question: Create a sentinel loop that will input numbers until -1 is entered and then display a total of all numbers
entered.**

**Answer:**
```python
total = 0

num = int(input("Enter number (-1 to stop): "))

while num != -1:
    total = total + num
    num = int(input("Enter number (-1 to stop): "))

print("Total =", total)
```

# Python Lists Review

## 21. Creating Lists

**Question: Create a list named `numbers` that contains the values 5, 10, and 15.**

**Answer:**
```python
numbers = [5, 10, 15]
````

---

**Question: Create an empty list called `data`.**

**Answer:**
```python
data = []
```

---

## 22. Indexing

**Question: Given the list below, what value is stored in `x`?**

```python
colors = ["red", "green", "blue"]
x = colors[1]
```

**Answer:**
```
green
```

---

### Question

**Question: What index would you use to access the first item in a list?**

**Answer:**

```
0
```

---

## 23. Append

### Question
Write code to add the value `25` to the list `numbers`.

**Answer:**

```python
numbers.append( 25 )
```

---

## 24. List Functions

### Question

Given the list below, what will each statement display?

```python
values = [4, 7, 2, 9]

print ( len(values) ) #____________  

print ( sum(values) ) #____________  

print ( min(values) ) #____________  

print ( max(values) ) #____________  

```

**Answer:**

```
len(values) => 4
sum(values) => 22
min(values) => 2
max(values) => 9
```

---

## 25. Loop Through a List

**Question: Write a loop to print all items in the list `fruits`, displaying the items on separate lines as shown.**

**Sample Output**
```
apple
banana
cherry
```

```python
fruits = ["apple", "banana", "cherry"]

# *** show code here
```

**Answer:**

```python
fruits = ["apple", "banana", "cherry"]

i = 0
while i < len(fruits):
    print( fruits[ i ] )
    i = i + 1
```


-- end --
