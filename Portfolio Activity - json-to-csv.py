def json_to_csv(input_json_filepath, output_csv_filepath, fieldnames):
    # Create a dictionary to store the parsed JSON data
    parsed_data = []

    # Open the input JSON file and parse its content
    with open(input_json_filepath, 'r') as input_json_file:
        parsed_json = json.load(input_json_file)

    # Extract the field values from the parsed JSON data and append them to the parsed_data list
    for row in parsed_json:
        parsed_data.append({field: row[field] for field in fieldnames})

    # Open the output CSV file and write the parsed data to it
    with open(output_csv_filepath, 'w', newline='') as output_csv_file:
        writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parsed_data)