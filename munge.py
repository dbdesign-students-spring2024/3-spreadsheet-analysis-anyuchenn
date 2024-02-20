with open('data/original_data.csv', 'r') as file:
    lines = file.readlines()

updated_lines = []
updated_lines.append(lines[0].strip() + ',Percentage Change in Consumption\n')

for i in range(1, len(lines)):
    current_year_data = lines[i].strip().split(',')
    if i == 1:
        updated_lines.append(','.join(current_year_data) + ',\n')
    else:
        previous_year_data = lines[i-1].strip().split(',')
        consumption_change = (float(current_year_data[2]) - float(previous_year_data[2])) / float(previous_year_data[2]) * 100
        updated_lines.append(','.join(current_year_data) + ',' + str(round(consumption_change, 2)) + '\n')

with open('data/clean_data.csv', 'w') as file:
    file.writelines(updated_lines)