# GraphML_G02
**IAAC MaCad · AIA26 S.3 Graph ML · 2025–26**

Graph learning pipeline for architectural data — dataset generation, graph construction, analysis, and node classification.

## Team
| Name | GitHub |
|------|--------|
| Charles Abichahine | [@charles-abichahine](https://github.com/charles-abichahine) |
| Emilie El Chidiac | [@hi-em](https://github.com/hi-em) |
| Lakzhmy Zaro | [@lakzhmy](https://github.com/lakzhmy) |
| Maria Sánchez i Domínguez | [@modnas-m](https://github.com/modnas-m) |

## Structure
```
01_dataset/          parametric dataset (Grasshopper + processed data)
02_graph_construction/   TopologicPy graph building
03_graph_analysis/   centrality metrics and spatial analysis
04_node_classification/  GNN node classification
05_results/          final figures and discussion
notebooks/           faculty reference notebooks (not graded)
```

## Setup
```bash
conda env create -f environment.yml
conda activate graphml-g02
jupyter lab
```
