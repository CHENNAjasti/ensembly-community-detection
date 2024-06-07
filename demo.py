import pandas as pd
from sklearn.metrics import f1_score, normalized_mutual_info_score

# Load the ground truth community memberships from the CSV files
ground_truth1 = pd.read_csv('ground_truth_community_membership.csv')
ground_truth2 = pd.read_csv('predicted_clusters.csv')

# Ensure that the node orders are the same in both files
ground_truth1 = ground_truth1.sort_values('node')
ground_truth2 = ground_truth2.sort_values('node')

# Check if the node orders are indeed the same
if not all(ground_truth1['node'] == ground_truth2['node']):
    print("Error: The node orders in the two ground truth files do not match.")
else:
    # Compute F1 score
    f1 = f1_score(ground_truth1['cluster_id'], ground_truth2['cluster_id'], average='macro')

    # Compute NMI
    nmi = normalized_mutual_info_score(ground_truth1['cluster_id'], ground_truth2['cluster_id'])

    print('F1 Score:', f1)
    print('NMI:', nmi)
