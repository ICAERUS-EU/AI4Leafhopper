# Leafhopper disease severity prediction

### Table of contents

* [Summary](#summary)
* [Data](#data)
* [Model](#model)
* [Result](#result)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

### Summary
This repository introduces the necessary steps to develop the model for the severity of leafhopper infestation symptoms.  


### Data
The dataset [leafhopper_2022_2024_adults_nymphs_per_plot_wk2.csv](https://github.com/ICAERUS-EU/AI4Leafhopper/tree/main/severity_prediction/data) was used to perform the experiments.


### Model
The model is an averaged linear mixed model for the variation, in two weeks, of the variable "% of leaves with more than 25% severity symptoms"
This model can be run using the R script: [scriptR_leafhopper_2022_2024_p_s_leaves_delta_wk2_alldata.Rfile](https://github.com/ICAERUS-EU/AI4Leafhopper/blob/main/severity_prediction/script/scriptR_leafhopper_2022_2024_p_s_leaves_delta_wk2_alldata.Rfile).


### Result
Two outputs are enabled: 
1) The [pdf](https://github.com/ICAERUS-EU/AI4Leafhopper/blob/main/severity_prediction/output/p_s_leaves_delta_wk2_alldata.pdf) includes all graphs derived from the linear mixed models run 
2) The [txt file](https://github.com/ICAERUS-EU/AI4Leafhopper/blob/main/severity_prediction/output/p_s_leaves_delta_wk2_alldata.txt) includes all the text output generated in R and  presents the model's output statistics. The R outputs (graphs and text) are sequential, and generated according to the order of the R script.

### Authors
Nuno Faria

### Acknowledgements
This project is funded by the European Union, grant ID 101060643.


<img src="https://rea.ec.europa.eu/sites/default/files/styles/oe_theme_medium_no_crop/public/2021-04/EN-Funded%20by%20the%20EU-POS.jpg" alt="https://cordis.europa.eu/project/id/101060643" width="200"/>
