### Python Assignment 4 - Lists

![assignment graphic](./movie_list.png)

### Overview
The purpose of this assignment is to learn how to build lists dynamically and process data in lists.
Instead of starting with a full list, you will use a **sentinel loop** to allow the user to build their own collection of movie data. 
You will practice managing two lists `movies` and `scores` to keep titles and corresponding scores.

---

### Starter Code (`lists.py`)
```python
# lists.py
# your name
# date
# description

# 1. Initialize Empty Lists
# Create two empty lists: one named 'movies' and one named 'scores'
# add code here


# 2. Dynamic Data Entry (Sentinel Loop)
print("2. Build Your Movie Database")
print("Enter movie details below. Enter 'quit' as the movie title to stop.")
print()

# Use a sentinel loop to ask for movie titles.
# While the title is not 'quit':
#   1. Append the title to the movies list.
#   2. Ask for the Rotten Tomatoes score and append it to the scores list.
#   3. Ask for the next movie title (or 'quit').

# add code here


# 3. List Functions
print()
print("3. Collection Statistics")
# Use len() to display how many movies are in the list.
# Use sum() and len() to calculate and display the average score.
# add code here


# 4. Accessing Specific Data
print()
print("4. First and Last Entries")
# Display the first movie added and the last movie added 
# (Hint: use index 0 and index -1)
# add code here


# 5. Full Report (Iterating)
print()
print("5. Complete Movie Report")
# Use a **while** loop to print every movie
# and its score from your lists in a formatted report.
# add code here


# 6. Highs and Lows
print()
print("6. Top Rated")
# Use max() to find the highest score in the list.
# Display that high score.
# add code here
```

---

### Sample Run
```text
1. Build Your Movie Database
Enter movie details below. Enter 'quit' as the movie title to stop.

Enter movie title: Toy Story
Enter Rotten Tomatoes score: 100

Enter movie title: Cars
Enter Rotten Tomatoes score: 74

Enter movie title: Up
Enter Rotten Tomatoes score: 98

Enter movie title: quit

2. Collection Statistics
You have 3 movies in your collection.
The average score is 90.67%

3. First and Last Entries
First added: Toy Story
Last added: Up

4. Complete Movie Report
1. Toy Story - Score: 100%
2. Cars - Score: 74%
3. Up - Score: 98%

5. Top Rated
The highest score in your collection is 100%
```

---
## In-Class Examples

[Chapel List Example](./chapel_list.py)

---

### Challenges (optional)
* display a list of all movies that are 90% or higher
* add a search feature that asks for the user's movie title and displays the score if found
* add an update feature that allows the user to enter the title and update the score
* add a list called `genre` that stores the type of movie, i.e., drama, comedy, action, horror

---

### Submitting Assignment
Upload `lists.py` to the course website.

---

