import csv

filename = 'taxi_1000.csv'

total_fares = 0.0
trip_count = 0
max_trip_distance = 0.0

# Read the CSV file
with open(filename, mode='r') as csvfile:
    csvreader = csv.DictReader(csvfile)  # Use DictReader to access columns by name
    for row in csvreader:
        # Convert fare and trip miles to float for calculations
        fare = float(row['Fare'])  # Adjust the field name based on your CSV header
        trip_miles = float(row['Trip Miles'])  # Adjust the field name as needed
        
        # Only process records with fares greater than $10
        if fare > 10:
            # Calculate total fares
            total_fares += fare
            trip_count += 1
            
            # Determine the maximum trip distance
            if trip_miles > max_trip_distance:
                max_trip_distance = trip_miles

# Calculate the average fare if there are qualifying trips
average_fare = total_fares / trip_count if trip_count > 0 else 0

# Print the results
print(f'Total Fares (greater than $10): ${total_fares:.2f}')
print(f'Average Fare (greater than $10): ${average_fare:.2f}')
print(f'Maximum Trip Distance (for fares > $10): {max_trip_distance:.2f} miles')
