source("C:/Users/Chenn/OneDrive/Documents/capstone_R/old/lovian.R")
source("C:/Users/Chenn/OneDrive/Documents/capstone_R/old/spinglass.R")
source("C:/Users/Chenn/OneDrive/Documents/capstone_R/old/walktrap.R")
source("C:/Users/Chenn/OneDrive/Documents/capstone_R/old/leading eigenevector.R")
source("C:/Users/Chenn/OneDrive/Documents/capstone_R/old/labelpropagation.R")
source("C:/Users/Chenn/OneDrive/Documents/capstone_R/old/infomap.R")
# Load the required libraries
library(igraph)

# Create an empty graph with some initial vertices
g <- graph(edges = numeric(0))

# List of community dictionaries from different algorithms
community_dicts <- list(
  community_dict_walktrap = community_dict_walktrap,
  community_dict_lovian = community_dict_lovian,
  community_dict_spinglass = community_dict_spinglass,
  community_dict_leading = community_dict_eigen,
  community_dict_label=community_dict_label,
  community_dict_infomap=community_dict_infomap
)

# Add nodes and edges for each community
for (algorithm in names(community_dicts)) {
  community_dict <- community_dicts[[algorithm]]
  
  for (community_name in names(community_dict)) {
    community_nodes <- community_dict[[community_name]]
    
    # Add nodes to the graph
    g <- add_vertices(g, n = length(community_nodes), name = community_nodes)
    
    # Add edges within the community
    for (i in 1:(length(community_nodes) - 1)) {
      for (j in (i + 1):length(community_nodes)) {
        g <- add_edges(g, c(community_nodes[i], community_nodes[j]))
      }
    }
  }
}
# Plot the n-partition graph
plot(g)

#get.edge.attribute(g, "weight", index = which(ends(E(g))[, 1] == "1" & ends(E(g))[, 2] == "4"))
# Get the edge list of the graph
edge_list <- get.edgelist(g, names=TRUE)

# Create a data frame from the edge list
edge_df <- data.frame(source_node = edge_list[, 1], destination_node = edge_list[, 2])

# Get the weights of the edges
weights <- get.edge.attribute(g, "weight")

# Add the weights to the data frame
edge_df$weight <- weights

# Write the data frame to a CSV file
write.csv(edge_df, file = "edge_weights.csv", row.names = FALSE)

