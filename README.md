# Ensembly community detection
In this repository, you will find multiple files and may confuse you a little imma explain you in a clear manner.

## PreRequesits
You need R studio and all the libraries mentioned in the ".R" files along with a python interpreter

## datasets
You will find 2 datasets:
#### 1) Network_file.txt
#### 2) Ground_truth_file.txt

## Preprocessing 
We pre-processed the data by removeing the blank spaces as this dataset was created by [ LFR benchmark algorithm ](https://networkx.org/documentation/stable/reference/generated/networkx.generators.community.LFR_benchmark_graph.html) it doesn't require much pre-processing being a synthetic dataset
-> convert the txt file into .csv file for more convenient data frame creation and give the dataframe as a parameter to the functions.

## Base community detection
We pass this dataset into multiple base community detection algorithmsin an R file and save the communities in an output file.[ Igraph package ](https://cran.r-project.org/web/packages/igraph/index.html)
Later we caliculate the [ conductance score ](https://search.r-project.org/CRAN/refmans/clustAnalytics/html/conductance.html) of these communities useing a prebuilt function and save them in a output file.

## Co-Assosiation Matrix
After the outputs are taken to make a Weighted co-assosiation matrix on the conditions which can be checked in the [ report ](https://github.com/CHENNAjasti/ensembly-community-detection/blob/main/keshav.pdf).

## Spectral clustering
After the Weighted Co-Assosiation amtrix is formed a spectral clustering algorithms is used to get the required number of clusters.

## Checking output
F1-score and NMI is caliculaed by compareing the final resultant communitys with the groundtruth file.
