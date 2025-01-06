##### Author: Manisha Sirsat
##### Department: Data Management and Risk Analysis
##### Organization: InnovPlantProtect, Elvas, Portugal

#importing the necessory libraries
import os
from osgeo import gdal, osr
import json

#extracting geographic bounds (both projected and geographic coordinates) from the TIF images 
def get_geographic_bounds(tif_image_path):
    dataset = gdal.Open(tif_image_path)
    if dataset is None:
        raise FileNotFoundError(f"TIF image is not found: {tif_image_path}")

    geo_transform = dataset.GetGeoTransform()
    proj_ref = dataset.GetProjection()
    #calculating the bounds
    min_lon = geo_transform[0]
    max_lon = min_lon + geo_transform[1] * dataset.RasterXSize
    max_lat = geo_transform[3]
    min_lat = max_lat + geo_transform[5] * dataset.RasterYSize
    #debugging using Log GeoTransform
    print("GeoTransform matrix:")
    print(f"Origin: ({geo_transform[0]}, {geo_transform[3]})")
    print(f"Pixel size: ({geo_transform[1]}, {geo_transform[5]})")
    dataset = None
    return min_lon, max_lon, min_lat, max_lat, proj_ref

#converting yolo normalized coordinates to geographic coordinates and saving them in GeoJSON format
def convert_yolo_to_geojson(yolo_file_path, min_lon, max_lon, min_lat, max_lat, output_geojson_path):
    features = []
    #reading yolo annotations
    with open(yolo_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 2:
                continue

            #extracting class ID and polygon points
            class_id = int(parts[0])
            points = list(map(float, parts[1:]))
            #rescaling normalized coordinates to geographic coordinates
            polygon = []
            for x, y in zip(points[::2], points[1::2]):
                #converting normalized x value to longitude
                lon = min_lon + x * (max_lon - min_lon)  
                #converting normalized y value to latitude
                lat = max_lat + y * (min_lat - max_lat)  
                polygon.append([lon, lat])

            #debugging using Log polygon
            print(f"Class ID {class_id} - Polygon (Sample): {polygon}")
            #creating GeoJSON feature structure
            feature = {
                "type": "Feature",
                "properties": {
                    "OBJECTID": class_id,
                    "class_id": class_id,
                    "description": "created GeoJSON from the yolo annotations"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [polygon]
                }
            }
            features.append(feature)

    #constructing GeoJSON with CRS=WGS84 
    geojson_data = {
        "type": "FeatureCollection",
        "name": "Boundaries_PSA",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:EPSG::32629"
            }
        },
        "features": features
    }
    #saving the data to GeoJSON file
    with open(output_geojson_path, 'w') as geojson_file:
        json.dump(geojson_data, geojson_file, indent=2)

#validating the CRS of the TIF image that matches the expected code
def validate_tif_crs(proj_ref, expected_epsg=4326):
    source_srs = osr.SpatialReference()
    source_srs.ImportFromWkt(proj_ref)
    if source_srs.IsGeographic() == 1 and source_srs.GetAuthorityCode(None) == str(expected_epsg):
        print(f"CRS Validation: TIF image is already in EPSG:{expected_epsg} (WGS84).")
        return True
    else:
        print(f"TIF image CRS is not EPSG:{expected_epsg}. Transformation may be needed.")
        return False

#processing all TIF and yolo files in the specified directories and saving them into GeoJSON format
def process_dir(tif_dir, yolo_dir, geojson_dir):
    #checking if the output directory exists
    os.makedirs(geojson_dir, exist_ok=True)
    #iterating over TIF images
    for image_name in os.listdir(tif_dir):
        if image_name.endswith(".tif"):
            tif_image_path = os.path.join(tif_dir, image_name)
            yolo_file_name = image_name.replace(".tif", ".txt")
            yolo_file_path = os.path.join(yolo_dir, yolo_file_name)
            if not os.path.exists(yolo_file_path):
                print(f"{image_name}: No yolo annotation file found in {yolo_dir}.")
                continue

            output_geojson_name = image_name.replace(".tif", ".geojson")
            output_geojson_path = os.path.join(geojson_dir, output_geojson_name)
            #extracting the geographic bounds
            min_lon, max_lon, min_lat, max_lat, proj_ref = get_geographic_bounds(tif_image_path)
            print(f"Processing {image_name}:")
            print(f"Geographic Bounds: min_lon={min_lon}, max_lon={max_lon}, min_lat={min_lat}, max_lat={max_lat}")
            print(f"Projection: {proj_ref}")
            #validating CRS
            validate_tif_crs(proj_ref, expected_epsg=4326)
            #converting yolo annotations to GeoJSON format
            convert_yolo_to_geojson(yolo_file_path, min_lon, max_lon, min_lat, max_lat, output_geojson_path)
            print(f"  GeoJSON file saved at: {output_geojson_path}")

def main():
    #setting the paths of the tif image, yolo annotation and geojson directories
    tif_dir = "../yolov9/YOLODataset/images/test/tif"  
    yolo_dir = "../yolov9/runs/predict-seg/exp/labels"  
    geojson_dir = "../yolov9/runs/predict-seg/exp/geo_json"  
    #calling the function to access/process the directories
    process_dir(tif_dir, yolo_dir, geojson_dir)

if __name__ == "__main__":
    main()
