import sqlite3

import pandas as pd
import matplotlib.pyplot as plt


# Connect to the lesson database
connection = sqlite3.connect("../db/lesson.db")


# Calculate the total price for each order
sql = """
SELECT
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l
    ON o.order_id = l.order_id
JOIN products p
    ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""


# Load the SQL results into a Pandas DataFrame
df = pd.read_sql_query(sql, connection)

# Close the database connection
connection.close()


# Calculate cumulative revenue
def cumulative(row):
    totals_above = df["total_price"][0:row.name + 1]
    return totals_above.sum()


df["cumulative"] = df.apply(cumulative, axis=1)


# Create a line plot using Pandas
df.plot(
    kind="line",
    x="order_id",
    y="cumulative"
)

# Add title and labels
plt.title("Cumulative Revenue by Order")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")

# Show the plot
plt.show()