# Assuming you have your F1 scores and NMI scores stored in vectors
f1_scores <- c(0.7500000, 0.06576402, 0.08633094, 0.2117647, 0.2352941, 0.1666667)
nmi_scores <- c(0.8701762 , 0.5729572, 0.7043853, 0.9004981, 0.8564483, 0.8374994)
algorithms <- c("infomap", "labelpropagation", "leadingeigenevector", "lovian", "spinglass", "walktrap")

# Create a dataframe
data <- data.frame(Algorithms = algorithms, F1_Scores = f1_scores, NMI_Scores = nmi_scores)

# Load igraph library
library(igraph)

# Plotting F1 scores
barplot(data$F1_Scores, names.arg = data$Algorithms, main = "F1 Scores for Community Detection Algorithms",
        xlab = "Algorithms", ylab = "F1 Scores", col = "blue")

# Adding F1 scores as annotations
text(x = 1:length(data$F1_Scores), y = data$F1_Scores, labels = round(data$F1_Scores, digits = 2), pos = 3)

# Plotting NMI scores
barplot(data$NMI_Scores, names.arg = data$Algorithms, main = "NMI Scores for Community Detection Algorithms",
        xlab = "Algorithms", ylab = "NMI Scores", col = "red")

# Adding NMI scores as annotations
text(x = 1:length(data$NMI_Scores), y = data$NMI_Scores, labels = round(data$NMI_Scores, digits = 2), pos = 3)
