# Define the calculate_metrics function
calculate_metrics <- function(true_positive, false_positive, false_negative) {
  precision <- true_positive / (true_positive + false_positive)
  recall <- true_positive / (true_positive + false_negative)
  f1_score <- 2 * precision * recall / (precision + recall)
  
  return(list(precision = precision, recall = recall, f1_score = f1_score))
}

# Define the entropy function
entropy <- function(labels) {
  counts <- table(labels)
  probabilities <- prop.table(counts)
  entropy <- -sum(probabilities * log(probabilities))
  return(entropy)
}

# Load the required library
library(mclust)
library(igraph)
library(openxlsx)

# Define the calculate_nmi function
calculate_nmi <- function(true_labels, predicted_labels) {
  # Calculate entropy
  H_true <- entropy(true_labels)
  H_pred <- entropy(predicted_labels)
  
  # Calculate joint entropy
  H_joint <- entropy(cbind(true_labels, predicted_labels))
  
  # Calculate mutual information
  MI <- H_true + H_pred - H_joint
  
  # Calculate NMI
  NMI <- 2 * MI / (H_true + H_pred)
  
  return(NMI)
}

# Read the CSV file
df <- read.csv("C:/Users/Chenn/Documents/capstone_R/old/Network_File.csv")

# Create a graph from the edge list with weights
G <- graph.data.frame(df, directed = FALSE)
weight <- E(G)$weight

# Apply specified model for community detection
communities <- cluster_edge_betweenness(G, weight)

# Read ground truth community membership from CSV
ground_truth <- read.csv("C:/Users/Chenn/Documents/capstone_R/old/ground_truth_community_membership.csv")

# Extracting community memberships as a vector
ground_truth_vector <- ground_truth$cluster_id

# Create an empty dictionary to store community memberships
community_dict_edgebetweeness <- list()

# Iterate over each community
for (i in 1:length(communities)) {
  # Get nodes in the current community
  community_nodes <- which(membership(communities) == i)
  
  # Store the nodes in the dictionary
  community_dict_edgebetweeness[[paste0("Community_", i)]] <- V(G)$name[community_nodes]
}

# Compare ground truth with detected communities
true_positive <- sum(ground_truth_vector == membership(communities))
false_positive <- sum(ground_truth_vector != membership(communities) & membership(communities) == 1)
false_negative <- sum(ground_truth_vector != membership(communities) & membership(communities) == 0)

# Calculate precision, recall, and F1 score
metrics <- calculate_metrics(true_positive, false_positive, false_negative)

# Calculate NMI
nmi <- calculate_nmi(ground_truth_vector, membership(communities))

# Set up community colors
community_colors <- rainbow(length(communities))

# Set smaller margins
par(mar = c(2, 2, 1, 1))  # Adjust the margin values as needed

# Plot each community
par(mfrow = c(3, 2))  # Adjust the layout based on the number of communities
for (i in 1:length(communities)) {
  subgraph_nodes <- which(membership(communities) == i)
  subgraph <- induced.subgraph(G, subgraph_nodes)
  
  # Use layout.fruchterman.reingold for node layout
  plot(subgraph, layout = layout.fruchterman.reingold, 
       vertex.color = community_colors[i], main = paste("Community", i))
}

# Reset graphics parameters
par(mfrow = c(1, 1))  # Reset to default single plot layout
par(mar = c(5, 4, 4, 2) + 0.1)  # Reset default margins

# Print the metrics
cat("F1 Score:", metrics$f1_score, "\n")

# Print NMI
cat("NMI:", nmi, "\n")
print(community_dict_edgebetweeness)