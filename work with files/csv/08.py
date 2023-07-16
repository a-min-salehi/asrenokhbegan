import csv

# Open the CSV file in read mode
with open('feedback.csv', 'r') as file:
    # Create a CSV reader object with dictionary fieldnames
    csv_reader = csv.DictReader(file)

    keywords = ['service', 'food']
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        customer_name = row['Customer Name']
        date = row['Date']
        comment = row['Comment']

        # Check if comment contains any of the keywords
        if any(keyword in comment.lower() for keyword in keywords):
            print(f"Customer: {customer_name}")
            print(f"Date: {date}")
            print(f"Comment: {comment}")
            print()

