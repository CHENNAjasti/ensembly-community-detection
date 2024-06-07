import json
import numpy as np

# Load the JSON files
community_dict_eigen = json.load(open('community_dict_eigen.json'))
community_dict_label = json.load(open('community_dict_label.json'))
community_dict_walktrap = json.load(open('community_dict_walktrap.json'))
community_dict_spinglass = json.load(open('community_dict_spinglass.json'))
community_dict_lovian = json.load(open('community_dict_lovian.json'))
community_dict_infomap = json.load(open('community_dict_infomap.json'))

# Load the CSV files skipping the header row
conductance_scores_eigen = np.loadtxt('conductance_scores_eigen.csv', delimiter=',', skiprows=1)
conductance_scores_infomap = np.loadtxt('conductance_scores_infomap.csv', delimiter=',', skiprows=1)
conductance_scores_label = np.loadtxt('conductance_scores_label.csv', delimiter=',', skiprows=1)
conductance_scores_walktrap = np.loadtxt('conductance_scores_walktrap.csv', delimiter=',', skiprows=1)
conductance_scores_spinglass = np.loadtxt('conductance_scores_spinglass.csv', delimiter=',', skiprows=1)
conductance_scores_lovian = np.loadtxt('conductance_scores_lovian.csv', delimiter=',', skiprows=1)

# Initialize the matrix Ã
Ã = np.zeros((500, 500))

# Calculate the conductance scores
for i in range(500):
    for j in range(500):
        if i != j:
            # Initialize the total conductance score
            total_conductance_score = 0
            
            # Check if nodes i and j exist in the same community
            if i in community_dict_eigen.values() and j in community_dict_eigen.values():
                # Calculate the conductance score
                total_conductance_score += conductance_scores_eigen[np.where(community_dict_eigen.values() == i)[0][0], 1]
                total_conductance_score += conductance_scores_eigen[np.where(community_dict_eigen.values() == j)[0][0], 1]
            if i in community_dict_label.values() and j in community_dict_label.values():
                # Calculate the conductance score
                total_conductance_score += conductance_scores_label[np.where(community_dict_label.values() == i)[0][0], 1]
                total_conductance_score += conductance_scores_label[np.where(community_dict_label.values() == j)[0][0], 1]
            if i in community_dict_walktrap.values() and j in community_dict_walktrap.values():
                # Calculate the conductance score
                total_conductance_score += conductance_scores_walktrap[np.where(community_dict_walktrap.values() == i)[0][0], 1]
                total_conductance_score += conductance_scores_walktrap[np.where(community_dict_walktrap.values() == j)[0][0], 1]
            if i in community_dict_spinglass.values() and j in community_dict_spinglass.values():
                # Calculate the conductance score
                total_conductance_score += conductance_scores_spinglass[np.where(community_dict_spinglass.values() == i)[0][0], 1]
                total_conductance_score += conductance_scores_spinglass[np.where(community_dict_spinglass.values() == j)[0][0], 1]
            if i in community_dict_lovian.values() and j in community_dict_lovian.values():
                # Calculate the conductance score
                total_conductance_score += conductance_scores_lovian[np.where(community_dict_lovian.values() == i)[0][0], 1]
                total_conductance_score += conductance_scores_lovian[np.where(community_dict_lovian.values() == j)[0][0], 1]
            
            # Calculate the value for aij
            aij = 1/6 * total_conductance_score

            # Store the value in the matrix Ã
            Ã[i, j] = aij

# Export the matrix Ã to a CSV file
np.savetxt('Ã.csv', Ã, delimiter=',')
