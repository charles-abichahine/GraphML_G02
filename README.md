# GraphML_G02
**IAAC MaCad · AIA26 S.3 Graph ML · 2025–26**

Graph-based analysis and learning pipeline for architectural floor plans, using the [Modified Swiss Dwellings dataset](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings).

## Team
| Name | GitHub |
|------|--------|
| Charles Abi Chahine | [@charles-abichahine](https://github.com/charles-abichahine) |
| Emilie El Chidiac | [@hi-em](https://github.com/hi-em) |
| Lakzhmy Zaro | [@lakzhmy](https://github.com/lakzhmy) |
| Maria Sánchez i Domínguez | [@modnas-m](https://github.com/modnas-m) |

## Structure
```
01_dataset/              MSD dataset research + recreated floor plan (Rhino/GH)
02_graph_construction/   TopologicPy graph from recreated floor plan
03_graph_analysis/       centrality metrics and spatial analysis
04_node_classification/  node classification using pretrained model (S06)
05_results/              final figures and discussion
notebooks/               reference notebooks
```

## Setup
```bash
conda env create -f environment.yml
conda activate graphml-g02
jupyter lab
```
