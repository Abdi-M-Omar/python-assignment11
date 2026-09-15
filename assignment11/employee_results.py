import sqlite3

import pandas as pd
import matplotlib.pyplot as plt


# Connect to the lesson database
connection = sqlite3.connect("../db/lesson.db")


# SQL query to calculate revenue for each employee
sql = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""


# Load the SQL query results into a DataFrame
employee_results = pd.read_sql_query(sql, connection)

# Close the database connection
connection.close()


# Create a bar chart using Pandas
employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    color="steelblue"
)

# Add title and labels
plt.title("Employee Revenue")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")

# Show the plot
plt.show()