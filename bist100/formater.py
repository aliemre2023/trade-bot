f = open("bist100/bist100_wikipedia.txt","r")
data = f.read()

# Extract table rows
rows = data.split('|-\n')

# Define a function to clean up text
def clean_text(text):
    return text.replace('[', '').replace(']', '')

# Convert rows into the desired format
formatted_data = []
for row in rows[1:]:
    cells = row.split('\n|')
    row_data = []
    for cell in cells:
        cell = clean_text(cell)
        row_data.append(f"{cell}")
     
    row_data[0] = row_data[0][1:]
    row_data = row_data[:-2]
    formatted_data.append(row_data)

# Write the formatted data to a text file
f = open('bist100/bist100.txt', 'w')
f.write("code;company;sector;subsector;central;\n")
for row in formatted_data:
    for item in range(len(formatted_data[0])):
        f.write(row[item])
        f.write(";")
    f.write("\n")

print("Data has been converted and saved to bist100.txt file.")
