# Spreadsheets

Spreadsheets are used to **organize, analyze, and visualize data** for tasks such as:

* Tracking information
* Performing calculations
* Sorting data
* Generating charts

---

## Formulas vs. Functions

Spreadsheets use both **formulas** and **functions** to perform calculations.

---

### Formulas

A **formula**:

* Starts with an equal sign `=`
* Specifies cell references and mathematical operations:

  * Add `+`
  * Subtract `-`
  * Multiply `*`
  * Divide `/`

**Examples:**

```excel
=A1 + B1 + C1 + D1
=(B2 + B3 + B4) / 3
```

---

### Functions

A **function** automates a calculation.

* Has a function name like `SUM` or `AVERAGE`
* Often includes a **range** of numbers
* The `MAX` function returns the largest value

**Examples:**

```excel
=MAX(20, 50, 40)
```

---

## Ranges

A **range** defines a set of cells.

* `A1:D1` includes cells A1, B1, C1, and D1
* `B2:B4` includes cells B2, B3, and B4

**Examples:**

```excel
=SUM(A1:D1)
=AVERAGE(B2:B4)
```

---

## Common Errors

A common mistake is using the `SUM` function incorrectly around a formula:

```excel
=SUM(A1+A2+A3)     Not OK – improper use of function
=A1+A2+A3          OK – formula adding three cells
=SUM(A1:A3)        OK – function adding a range
```

---

## Key Spreadsheet Concept

1. Enter your data first.
2. Use formulas or functions to automate calculations.

If you find yourself:

* Using a calculator
* Adding numbers by hand

You are **not using the spreadsheet correctly**.

**Let the spreadsheet do the work!**

When data changes, the spreadsheet should **automatically update** the calculations.

---

# Charts

Charts provide a **visual representation of data**, making it easier to identify:

* Trends
* Comparisons
* Insights

To create a chart:

1. Select the data (use `Ctrl` or `Shift`)
2. Choose **Insert → Chart**

---

## Types of Charts

### 1. Pie Chart

Displays parts of a whole (total = 100%).

**Example:**
Showing sales contributions of individuals as a percentage of total sales.

![Pie Chart](images/pie_chart.png)
---

### 2. Column Chart

Compares different items or groups.

**Example:**
Comparing sales numbers for eight different individuals.

![Column Chart](images/column_chart.png)

---

### 3. Stacked Column Chart

Shows how different components contribute to a total across categories.

**Example:**
Comparing total sales where each segment of the column shows contributions from each week.

![Stacked Column Chart](images/stacked_column_chart.png)

---

### 4. Line Chart

Tracks changes over time.

**Example:**
Displaying sales over five weeks to identify trends.

![Line Chart](images/line_chart.png)

---

-- end --


