import csv

def filter_csv(input_file, output_file):
    filtered_rows = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            version = row['Version']
            laser_duration = row['LaserDuration']
            laser_protocol = row['LaserProtocol']
            if (version == '3.16.0.0' or version == '3.17.00') and laser_duration >= '15:00.0' and laser_protocol == "LaserFullFireRDP1":
                filtered_rows.append(row)

    fieldnames = reader.fieldnames
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)

# Example usage
input_file = 'LinePressureAnalyzerTable.csv'
output_file = 'output1.csv'
filter_csv(input_file, output_file)