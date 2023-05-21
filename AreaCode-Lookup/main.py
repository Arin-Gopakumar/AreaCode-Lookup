import pandas as pd

data = pd.read_csv('data.csv')

userInfo = int(input("Please enter an area code for which you want to find more information about: "))

# Group the data by area code and state
grouped_data = data.groupby(['Number', 'State'])

# Convert the group keys to a list
group_keys = list(grouped_data.indices.keys())

# Find the group that matches the user input area code
matching_group = None
for key in group_keys:
    if key[0] == userInfo:
        matching_group = key
        break

if matching_group:
    # Filter the grouped data for the matching group
    area_code_data = grouped_data.get_group(matching_group)

    if len(area_code_data) > 1:
        # If there are multiple cities with the same area code within the state
        for index, row in area_code_data.iterrows():
            specific = "City: " + row['City'] + ", State: " + row['State'] + ", Country: " + row['Country']
            print(specific)
    else:
        # If there is only one city with the area code within the state
        specific = "City: " + area_code_data['City'].iloc[0] + ", State: " + area_code_data['State'].iloc[0] + ", Country: " + area_code_data['Country'].iloc[0]
        print(specific)
else:
    print("No information available for the provided area code and state.")