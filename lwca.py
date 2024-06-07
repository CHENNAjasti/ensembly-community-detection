import numpy as np
import os

def read_community_assignments(filename):
  community_dict = {}
  with open(filename, 'r') as f:
    for line in f:
      cluster, nodes_text = line.split("\"", 1)
      nodes = nodes_text.strip("()").split("\",\"")
      community_dict[cluster] = nodes
  return community_dict

def get_conductance_score(filename, community_label):
  with open(filename, 'r') as f:
    next(f)  # Skip the header row
    for line in f:
      cluster, score = line.strip().split(',')
      if cluster.strip() == community_label:
        return float(score)
  raise ValueError(f"Community {community_label} not found in conductance scores file {filename}")

def construct_adjacency_matrix(num_nodes):
  # Dictionary to store all community assignments
  community_dict = {}
  for filename in os.listdir():
    if filename.startswith("community_dict_"):
      algorithm_name = filename.split("_")[2]
      community_dict[f"algorithm_{algorithm_name}"] = read_community_assignments(filename)

  # Dictionary to store conductance scores for each algorithm
  conductance_scores = {}
  for filename in os.listdir():
    if filename.startswith("conductance_scores_"):
      algorithm_name = filename.split("_")[2]
      conductance_scores[algorithm_name] = {}
      with open(filename, 'r') as f:
        next(f)  # Skip the header row
        for line in f:
          cluster, score = line.strip().split(',')
          conductance_scores[algorithm_name][cluster.strip()] = float(score)

  A_tilde = np.zeros((num_nodes, num_nodes))
  for i in range(num_nodes):
    print(f"Processing node {i+1}...")  # Track node processing for debugging
    for m in range(1, 7):  # Assuming 6 algorithms (1 to 6)
      algorithm_name = f"algorithm_{m}"
      if algorithm_name not in community_dict:
        continue  # Skip algorithm if no community assignments found
      community_i = community_dict[algorithm_name][f"c{i+1}"]
      try:
        conductance_m = get_conductance_score(f"conductance_scores_{m}.csv", community_i)
      except ValueError as e:
        print(f"Error getting conductance score: {e}")
        continue  # Skip community if conductance score not found
      for j in range(i + 1, num_nodes):
        community_j = community_dict[algorithm_name][f"c{j+1}"]
        if community_i == community_j:
          A_tilde[i, j] += conductance_m
          print(f"Adding connection ({i+1},{j+1}) with conductance {conductance_m} (algorithm {m})")  # Track connection creation (debug)
  # Fill the lower triangular portion by symmetry
  A_tilde += A_tilde.T - np.diag(A_tilde.diagonal())
  return A_tilde

# Assuming 500 nodes (replace with actual number of nodes)
A_tilde = construct_adjacency_matrix(500)

print(A_tilde)  # Print the constructed adjacency matrix
