# Open the text file in read mode
with open('community_dict_eigen.txt', 'r') as file:
    lines = file.readlines()

# Initialize an empty dictionary to store the community memberships
community_dict = {}

# Iterate over each line in the file
for line in lines:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Check if the line contains a community name and members
    if '(' in line and ')' in line:
        # Extract the community name and members
        community_name, members = line.split('(')
        members = members.strip(')').split(', ')
        
        # Remove double quotes from members
        members = [int(member.strip('"')) for member in members]
        
        # Add the community name and members to the dictionary
        community_dict[community_name.strip()] = members

# Open the text file in write mode
with open('community_dict_eigen.txt', 'w') as file:
    # Write the dictionary to the text file
    for community_name, members in community_dict.items():
        file.write(f'{community_name}: {members}\n')