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
01_dataset/                      MSD dataset + our own floor plan (floor_plan/)
02_graph_construction_analysis/  TopologicPy graph construction + centrality analysis
03_node_classification/          node classification using pretrained model (S06)
04_results/                      final figures and discussion
notebooks/               reference notebooks
references/              research papers and links
```

## Dataset
Download the [Modified Swiss Dwellings dataset](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings) from Kaggle and place the files in `01_dataset/data/`. These files are gitignored and not committed to the repo.

## Setup
```bash
conda env create -f environment.yml
conda activate graphml-g02
jupyter lab
```
