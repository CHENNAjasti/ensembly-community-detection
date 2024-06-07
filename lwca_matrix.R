# Load required libraries
library(kernlab)
library(igraph)
library(caret)
library(readr)

# Load the LWCA matrix from CSV (assuming header row is absent)
data <- read_csv("modified_output.csv", col_names = FALSE)
LWCA_matrix <- as.matrix(data)

# Remove constant/zero columns
LWCA_matrix <- LWCA_matrix[, apply(LWCA_matrix, 2, var) != 0]

# Define the number of clusters (communities)
n_clusters <- 20  # Adjust as needed based on your data

# Perform spectral clustering
sc <- specc(LWCA_matrix, centers = n_clusters)

# Get cluster assignments
cluster_assignments <- sc@.Data

# Print cluster assignments
print(cluster_assignments)

# If you want to visualize the clusters, you can use a PCA plot
pca <- prcomp(LWCA_matrix)
reduced_data <- data.frame(pca$x[, 1:2])
names(reduced_data) <- c("PC1", "PC2")
reduced_data$cluster <- as.factor(cluster_assignments)

ggplot(reduced_data, aes(x = PC1, y = PC2, color = cluster)) +
  geom_point() +
  labs(color = "Cluster", x = "Component 1", y = "Component 2", title = "Cluster Plot (Spectral Clustering)")
#################################
# Load required libraries
library(mclust)
library(MLmetrics)

# Load ground truth data (assuming CSV format with header "node", "cluster_id")
ground_truth <- read_csv("ground_truth_community_membership.csv")
ground_truth_labels <- ground_truth$cluster_id  # Assuming cluster IDs are in the second column

# Calculate F1-score (treating clustering as a classification task)
# Note: F1 Score in R is typically used for binary classification. For multi-class classification, we calculate the average F1 Score.
f1 <- MLmetrics::F1_Score(y_pred = factor(cluster_assignments), y_true = factor(ground_truth_labels), positive = NULL)
print(paste("F1-score:", f1))

# Calculate NMI (using adjusted_rand_score as an alternative)
nmi <- mclust::adjustedRandIndex(cluster_assignments, ground_truth_labels)
print(paste("Normalized Mutual Information (NMI):", nmi))
