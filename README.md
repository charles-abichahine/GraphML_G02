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
notebooks/               all pipeline notebooks (01.x dataset · 02.x graph analysis · 03.x node classification)
01_dataset/              MSD dataset (data/) + our own floor plan (floor_plan/) + references/
02_graph_analysis/       assets (OBJ, Rhino) · output (BREP) · results (analysis images)
03_node_classification/  assets (model weights) · results (graph CSVs + predictions)
04_presentation/         slides and figures (img/)
```

## Dataset
Download the [Modified Swiss Dwellings dataset](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings) from Kaggle and place the files in `01_dataset/data/`. These files are gitignored and not committed to the repo.

## Setup
```bash
conda env create -f environment.yml
conda activate graphml-g02
jupyter lab
```
