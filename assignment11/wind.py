# Task 3: Interactive Visualizations with Plotly

import plotly.express as px
import plotly.data as pldata


# Task 3.1: Load the Plotly wind dataset
df = pldata.wind(return_type="pandas")

# Print the first 10 rows
print("First 10 rows:")
print(df.head(10))

# Print the last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))


# Task 3.2: Clean the strength column
# The original values are strings such as:
# "0-1", "1-2", "2-3", and "6+"
# Remove everything after the first number so the
# strength column can be converted to float.
df["strength"] = (
    df["strength"]
    .str.replace(r"-.*", "", regex=True)
    .str.replace("+", "", regex=False)
    .astype(float)
)

# Display the cleaned data type
print("\nCleaned strength column:")
print(df[["strength"]].head(10))

print("\nStrength data type:")
print(df["strength"].dtype)


# Task 3.3: Create an interactive scatter plot
# X-axis: wind strength
# Y-axis: frequency
# Color: wind direction
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs. Frequency",
    labels={
        "strength": "Wind Strength",
        "frequency": "Frequency",
        "direction": "Direction"
    }
)


# Task 3.4: Save the interactive plot as wind.html
fig.write_html("wind.html")

# Show the interactive plot
fig.show()