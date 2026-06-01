# Introduction to Python Lists: Managing Collections of Data

![list image](./python_lists.png)

Up to this point, we have been working with **simple variables**. A simple variable is like a single box that holds one piece of information—one name, one score, or one price. 

But what if you need to store 100 names? Or a thousand data points? Creating `name_variable1`, `name_variable2`, `name_variable3`... is inefficient and makes it impossible to perform calculations easily. That is where **Lists** come in.

---

## 1. What is a List?
A list is a **collection** of items stored in a single variable name. Think of it as a container with internal compartments. In Python, we define a list using square brackets `[]` and separate the items with commas.

Lists can hold any type of data. Here are a few examples:

```python
# A list of strings (text)
fruits = ["Apple", "Banana", "Cherry"]

# A list of integers (whole numbers)
jersey_numbers = [12, 24, 45, 99]

# A list of floats (decimal numbers)
prices = [19.99, 5.50, 10.00]

# An empty list (ready to be filled later)
shopping_cart = []
```

---

## 2. Accessing Items by Index
Items in a list are ordered, and every item has a specific address called an **index**. 



**The Golden Rule:** Python is **zero-indexed**. We start counting at **0**, not 1.

* `fruits[0]` is "Apple"
* `fruits[1]` is "Banana"
* `fruits[2]` is "Cherry"

**Pro Tip:** You can also count from the back using negative numbers. `fruits[-1]` is a shortcut for the **last** item in any list, regardless of its length.

---

## 3. Parallel Lists (Linking Data)
**Parallel Lists** is a technique where you maintain two or more separate lists that are logically "linked" by their index. This allows you to store different types of related information without complex structures.

For example, tracking store inventory:

| Index | `items` list | `costs` list |
| :--- | :--- | :--- |
| **0** | "Laptop" | 1200.00 |
| **1** | "Mouse" | 25.50 |
| **2** | "Keyboard" | 45.00 |

If you want to know the cost of the "Mouse," you look at index **1** in both lists.



---

## 4. Growing a List Dynamically
Most of the time, we don't know what data goes into a list when the program starts. We use the `.append()` method to add items to the **end** of an existing list.

```python
names = []              # Start empty
names.append("Alice")   # Now ["Alice"]
names.append("Bob")     # Now ["Alice", "Bob"]
```

In many programs, you will use a **sentinel loop** to allow a user to keep appending data until they decide to stop by entering a specific keyword (like "quit" or "-1").

---

## 5. List "Superpowers" (Built-in Functions)
Python provides built-in tools to analyze numeric lists instantly. These save you from having to write your own math logic:

* **`len(list)`**: Returns the total number of items in the list.
* **`sum(list)`**: Adds all the numbers in a list together.
* **`max(list)`**: Instantly finds the highest value in a list.
* **`min(list)`**: Instantly finds the lowest value in a list.

---

## 6. Processing Lists with While Loops
To "walk" through a list and process every item inside using a `while` loop, you must manually manage an index variable (usually `i`). This variable starts at 0 and increases until it reaches the end of the list.


```python
i = 0
while i < len(items):
    # Inside the loop, 'i' represents the current index
    # We use 'i' to pull from BOTH parallel lists at the same time
    print(f"Item: {items[i]} | Price: ${costs[i]}")
    
    # CRITICAL: Increment i so the loop moves to the next index
    i = i + 1
```

By using the length of the list (`len(items)`) as the limit, the loop automatically stops once it has touched every item in the collection.
