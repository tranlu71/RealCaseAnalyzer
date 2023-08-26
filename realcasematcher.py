import csv
def append_column(input_file_a, input_file_b, output_file):
    data_a = []
    data_b = {}

    with open(input_file_a, 'r') as file_a:
        reader_a = csv.DictReader(file_a)
        fieldnames_a = reader_a.fieldnames
        for row in reader_a:
            data_a.append(row)

    with open(input_file_b, 'r') as file_b:
        reader_b = csv.DictReader(file_b)
        fieldnames_b = reader_b.fieldnames
        counter = 0
        for row in reader_b:
            case_id = row['CaseId']
            laser_power = row['LaserPowerIntoProbe']
            start = row['Start']
            if case_id in data_b:
                data_b[case_id][start] = laser_power
            else:
                data_b[case_id] = {start: laser_power}
            counter = counter + 1
    updated_rows = []
    for row in data_a:
        case_id = row['CaseId']
        laser_on_time = row['LaserOnTime']
        laser_power = data_b[case_id][laser_on_time]
        row['LaserPower'] = laser_power
        updated_rows.append(row)

    fieldnames_a.append('LaserPower')

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_a)
        writer.writeheader()
        writer.writerows(updated_rows)

# Example usage
input_file_a = 'output1.csv'
input_file_b = 'CaseSummaryAnalyzerByLaserFireTable.csv'
output_file = 'output2.csv'
append_column(input_file_a, input_file_b, output_file)
