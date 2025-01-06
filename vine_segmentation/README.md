# Vine-specific segmentation model with YOLOv9

### Table of contents

* [Summary](#summary)
* [Data](#data)
* [Model](#model)
* [Result](#result)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

### Summary

A vine segmentation model has been developed to identify and segment individual vines from vineyard drone imagery. Within this repository, you will find a vine segmentation model designed for vineyard severity monitoring. The model's output (the segmented vines) is subsequently used to compute NDVI values per vine which allow an assessment of vineyard health.


### Data
The training data repository is available in the [Zenodo data folder](https://zenodo.org/...), which you can download from there. The vine vegetation image dataset was prepared, split into training, validation, and testing datasets. The Labelme tool was used for image annotation. Each vine tree was annotated with precise polygon-based annotations and they were saved in JSON format. Afterwards, the JSON annotations were converted into [YOLO format](https://github.com/ICAERUS-EU/AI4Leafhopper/vine_segmentation/yolo_2_geojson.py) which is acceptable annotation format for the YOLOv9 model.


### Model

The [vine segmentation](https://github.com/ICAERUS-EU/AI4Leafhopper/vine_segmentation/model/best.pt) model is a computer vision model for segmenting the vegetation area of each vine that allows vine health assessments through vegetation indices. This uses a algorithm called YOLOv9 for semantic segmentation and achieved 0.825 mean average precision (mAP).


### Result

1. Segmented vines with their bounding boxes:  

<p align="center">
  <img src="https://github.com/ICAERUS-EU/AI4Leafhopper/vine_segmentation/images/crop_20240528_code_reyAB01_154.png" width="400" height="400">
</p>

2. A vector shape file obtained by merging the single json file and representing all the segmented vines in AB01 vineyard in Reynolds study area. Thus, the final result displays the AI-segmented vines on the left and the same vines with their corresponding NDVI index on the right:

<p align="center">
  <img src="https://github.com/ICAERUS-EU/AI4Leafhopper/vine_segmentation/images/17_results_NDVI_segmentation.jpg" width="400" height="400">
</p>


### Authors
* **Manisha Sirsat** - [Manisha Sirsat](https://github.com/manishasirsat)
* **iLaria Marengo**


### Acknowledgements
This project is funded by the European Union, grant ID 101060643.


<img src="https://rea.ec.europa.eu/sites/default/files/styles/oe_theme_medium_no_crop/public/2021-04/EN-Funded%20by%20the%20EU-POS.jpg" alt="https://cordis.europa.eu/project/id/101060643" width="200"/>
