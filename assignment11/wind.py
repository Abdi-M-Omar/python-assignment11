# Task 3: Interactive Visualizations with Plotly

from pathlib import Path

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
# Convert wind-strength ranges to numeric float values.
# Examples:
# "0-1" -> 0.5
# "1-2" -> 1.5
# "2-3" -> 2.5
# "6+"  -> 6.0

def convert_strength(value):
    value = value.strip()

    if "-" in value:
        low, high = value.split("-")
        return (float(low) + float(high)) / 2

    if value.endswith("+"):
        return float(value.replace("+", ""))

    return float(value)


df["strength"] = df["strength"].apply(convert_strength)

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
        "direction": "Direction",
    },
)


# Task 3.4: Save the interactive plot as wind.html
output_file = Path(__file__).parent / "wind.html"

fig.write_html(
    output_file,
    include_plotlyjs="cdn"
)

print(f"\nSaved Plotly visualization to: {output_file}")


# Explicitly load/read the saved HTML file to verify it works
html_content = output_file.read_text(encoding="utf-8")

if "<html" in html_content.lower() and "plotly" in html_content.lower():
    print("Verification successful: wind.html was saved and loaded correctly.")
else:
    raise ValueError("wind.html could not be verified correctly.")


# Display the interactive visualization
fig.show()