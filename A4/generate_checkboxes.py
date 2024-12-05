# Number of rows and columns for the grid
rows = 18  # Adjust based on your schedule (e.g., weeks)
columns = 7  # Adjust based on days or slots in each week

# Base top and left positions
top_start = 7   # Starting top position
left_start = 29  # Starting left position
top_increment = 6  # Increment for each row
left_increment = 7  # Increment for each column

# Generate HTML
checkboxes = []
for row in range(rows):
    for col in range(columns):
        top = top_start + row * top_increment
        left = left_start + col * left_increment
        day_id = f"day-{row}-{col}"  # Unique ID for each checkbox

        # Create checkbox and fire emoji
        checkbox_html = f"""
        <input type="checkbox" id="{day_id}" class="day-checkbox" style="top: {top}%; left: {left}%; position: absolute;">
        <span class="fire-emoji" style="top: {top}%; left: {left}%; position: absolute;">🔥</span>
        """
        checkboxes.append(checkbox_html)

# Combine all generated checkboxes into a single string
output_html = "\n".join(checkboxes)

# Save to a file or print to copy-paste into your project
with open("checkboxes.html", "w") as file:
    file.write(output_html)

print("HTML generated!")
