import json
import csv
import itertools

def load_data(json_file, csv_file):
    with open(json_file, 'r') as f:
        community_dict = json.load(f)

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        conductance_scores = {row[0]: float(row[1]) for row in reader}
    
    return community_dict, conductance_scores

def compute_conductance_scores(i, j, community_dict, conductance_scores):
    if i != j:
        for key, values in community_dict.items():
            if str(i) in values and str(j) in values:
                community_name = key
                conductance = 1-conductance_scores.get(community_name, None)
                if conductance is not None:
                    if (i, j) in w_ij:
                        w_ij[(i, j)] += conductance
                    else:
                        w_ij[(i, j)] = conductance

# Load data and compute conductance scores for each algorithm
community_dict_eigen, conductance_scores_eigen = load_data('community_dict_eigen.json', 'conductance_scores_eigen.csv')
community_dict_label, conductance_scores_label = load_data('community_dict_label.json', 'conductance_scores_label.csv')
community_dict_lovian, conductance_scores_lovian = load_data('community_dict_lovian.json', 'conductance_scores_lovian.csv')
community_dict_infomap, conductance_scores_infomap = load_data('community_dict_infomap.json', 'conductance_scores_infomap.csv')
community_dict_walktrap, conductance_scores_walktrap = load_data('community_dict_walktrap.json', 'conductance_scores_walktrap.csv')
community_dict_spinglass, conductance_scores_spinglass = load_data('community_dict_spinglass.json', 'conductance_scores_spinglass.csv')

# Dictionary to store conductance scores
w_ij = {}

# Compute and accumulate conductance scores for each algorithm
for i, j in itertools.product(range(1, 501), repeat=2):
    compute_conductance_scores(i, j, community_dict_eigen, conductance_scores_eigen)
    compute_conductance_scores(i, j, community_dict_label, conductance_scores_label)
    compute_conductance_scores(i, j, community_dict_lovian, conductance_scores_lovian)
    compute_conductance_scores(i, j, community_dict_infomap, conductance_scores_infomap)
    compute_conductance_scores(i, j, community_dict_walktrap, conductance_scores_walktrap)
    compute_conductance_scores(i, j, community_dict_spinglass, conductance_scores_spinglass)
#############
import numpy as np
import pandas as pd

# Create an empty n*n matrix
n = 501  # Adjust this value based on your data
a_ij = np.zeros((n, n))

# Compute a_ij for all pairs of nodes
for i, j in itertools.product(range(1, n), repeat=2):
    if (i, j) in w_ij:
        a_ij[i-1][j-1] = 1/6 * w_ij[(i, j)]

# Convert the numpy array to a pandas DataFrame
df = pd.DataFrame(a_ij)

# Write the DataFrame to a CSV file
df.to_csv('a_ij.csv', index=False, header=False)
