# In-Class Assignment – Currency Converter  

![Currency Image](./currency.png)

**Instructions:** Work in groups of two, using one computer  
---

## Scenario

You’re in Canada and want an app that tells you the equivalent U.S. dollar cost when you see prices in Canadian dollars and enter the current exchange rate (e.g., .72222254).

**Example:**  
If an item is **$45.67 CAD** and the exchange rate is **0.72222254 US dollars per Canadian Dollar**, the app should display the price in U.S. dollars ie. **$32.98**.

---

## Step 1: Create an IPO Chart

1. Identify inputs (what data you’ll get from the user)  
2. Describe the processing (what calculation is needed)  
3. Define the output (what result you’ll display)  
4. Decide on clear variable names for each part  

| Input | Processing | Output |
|------|-----------|--------|
|      |           |        |

---

## Step 2: Develop Test Data

1. Create four sets of test data with expected results  
2. Verify your expected results using an online converter or calculator  

| Sample Input | Expected Output | Work? |
|-------------|----------------|-------|
| 1.          |                |       |
| 2.          |                |       |
| 3.          |                |       |
| 4.          |                |       |

---

## Step 3: Write the Python Code

*(Use IPO and sample test data as a guide)*

1. Add comments at the top with:
   - Program name  
   - Your name(s)  
   - Date  
   - Brief app description  

2. Label each code section as:
   - Input  
   - Processing  
   - Output  

---

## Step 4: Test Your Program

1. Run your program with your test data and confirm it matches the expected results  
2. Test with additional data from another group to ensure accuracy  

---

## Step 5: Demonstration

If completing in-class, demonstrate your completed program to **Professor Lehman**.

---

# Sample Solution

### Sample Calculations (assume .72 rate)

| Sample Input | Expected Output | Work? |
|-------------|----------------|-------|
| 1. $ 10, .72         |      $ 7.20          |   yes    |
| 2. $ 45.67, .72         |   $ 32.88          |  yes     |
| 3. $ 123.18, .72         |   $ 88.69             |  yes     |
| 4.  $1000, .72         |   $ 720.00             |   yes    |

---

## Sample IPO (Input Processing Output) chart 
| Input | Processing | Output |
|------|-----------|--------|
|   cad_price   |   usd_price = cad_price * exchange_rate        |        |
|   exchange_rate   |           | usd_price       |

---

```python
#     Program: CAD_to_USD_Converter.py
#      Author: Prof. Lehman
#        Date: 2025-11-05
# Description: Converts Canadian dollars to U.S. dollars using an exchange rate
#              entered as USD per 1 CAD (example rate: 0.71)

# ------------------------------
# Input
# ------------------------------
cad_price = float( input("Enter price in Canadian dollars: ") )
exchange_rate = float( input("Enter exchange rate (USD per 1 CAD, e.g., 0.71): ") )

# ------------------------------
# Processing
# ------------------------------
usd_price = cad_price * exchange_rate

# ------------------------------
# Output
# ------------------------------
print()
print(f"${cad_price:.2f} CAD = ${usd_price:.2f} USD")
```
-- end --
