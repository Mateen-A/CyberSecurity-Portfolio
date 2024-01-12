with open('traffic_dump.log', 'r') as log_file:
    lines = log_file.readlines()

    search_phrase = 'specific phrase'

    for line in lines:
        if search_phrase in line:
            print(line.strip())