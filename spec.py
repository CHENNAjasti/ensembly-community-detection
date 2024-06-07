import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
import networkx as nx
from sklearn.metrics import f1_score, normalized_mutual_info_score

# Load the matrix from the CSV file
matrix = pd.read_csv('a_ij.csv', header=None).values

# Apply spectral clustering
sc = SpectralClustering(affinity='precomputed', n_clusters=29, assign_labels='discretize')
labels = sc.fit_predict(matrix)

# Save the clusters into a CSV file
pd.DataFrame(labels).to_csv("C:/Users/Chenn/OneDrive/Documents/capstone_R/predicted_clusters.csv", index=False)

# Create a graph from the matrix
graph = nx.from_numpy_array(matrix)

# Get unique labels
unique_labels = np.unique(labels)

# Create a figure
fig, ax = plt.subplots(figsize=(10, 10))

# Draw each community with a different color
for i, label in enumerate(unique_labels):   
    # Get nodes in this community
    nodes = [node for node, community in enumerate(labels) if community == label]
    
    # Create a subgraph for this community
    subgraph = graph.subgraph(nodes)
    
    # Draw the subgraph
    nx.draw(subgraph, ax=ax, node_color=plt.cm.jet(i / len(unique_labels)), with_labels=True)

plt.title('Communities')
plt.show()

# Load the ground truth community membership from the CSV file
ground_truth = pd.read_csv('ground_truth_community_membership.csv')

# Prepare spectral clustering results in the same format as ground truth
spectral_clustering_results = pd.DataFrame({
    'node': ground_truth['node'],
    'cluster_id': labels
})

# Compute F1 score
f1 = f1_score(ground_truth['cluster_id'], spectral_clustering_results['cluster_id'], average='macro')

# Compute NMI
nmi = normalized_mutual_info_score(ground_truth['cluster_id'], spectral_clustering_results['cluster_id'])

print('F1 Score:', f1)
print('NMI:', nmi)