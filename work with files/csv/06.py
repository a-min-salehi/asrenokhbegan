import csv

# Open the CSV file in read mode
with open('books.csv', 'r') as file:
    # Create a CSV reader object with dictionary fieldnames
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        title = row['Title']
        author = row['Author']
        genre = row['Genre']
        quantity = int(row['Quantity'])

        # Check if book quantity is low
        if quantity < 5:
            print(f"Warning: The book '{title}' by {author} in the genre '{genre}' has a low quantity of {quantity}.")

