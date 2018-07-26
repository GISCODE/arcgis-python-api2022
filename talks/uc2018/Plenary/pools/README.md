# Swimming pool detection and classification using deep learning
This project was presented at UC Plenary this year. This repository contains code for creating an swimming pool detector. However, with minor modifications it can be trained on new data. If know want to our journey of development of this project the following  blogs might be helpful to you.

* [Medium in-depth blog](https://medium.com/geoai/swimming-pool-detection-and-classification-using-deep-learning-aaf4a3a5e652)

* [Esri overview blog](https://www.esri.com/arcgis-blog/products/api-python/analytics/how-we-did-it-integrating-arcgis-and-machine-learning-at-uc-2018/?adumkts=product&adupro=ArcGIS_Enterprise&aduc=social&adum=external&aduSF=twitter&utm_Source=social&aduca=ArcGIS_Enterprise_Releases&adut=deeplearningUC_blog&sf_id=701f2000000rpeWAAQ&adbsc=social2466101&adbid=1021789845209804800&adbpl=tw&adbpr=80676821)


## Object detection and GIS
The field od Deep Learning has recently witnessed groundbreaking research with state of the art results, but taking this research to the field and solving real-world problems is still a challenge. Integration of the latest research in AI with ArcGIS, the industry leading GIS, opens up a world of opportunities ranging from feature identification and land cover classification to creating maps straight out of imagery. With the great results of deep learning this project also showcases the flexibility of ArcGIS api for python to integrate with deep learning libraries like PyTorch and Fast.ai

![Detected Pools](https://cdn-images-1.medium.com/max/896/1*17wkvk94x7EKx8u33FQdwA.png)

<sub> Detected Pools (700m X 700m)</sub>  

## The Challenge

#### Update assessor data

Tax assessors at local government agencies must often rely on expensive and infrequent surveys, leading to assessment inaccuracies. Swimming pools are an important part of assessment records because they impact the value of the property. Finding pools that are not on the assessment roll (such as those recently constructed) will be valuable to the assessor, and will ultimately mean additional revenue for the community. Doing this through GIS and AI would certainly reduce the expensive human labor involved in updating the records through field visits of each property.

![Assessor's data](https://www.esri.com/arcgis-blog/wp-content/uploads/2018/07/pools1.png "Visualizing residential parcels in ArcGIS Pro")

<sub> Visualizing residential parcels in ArcGIS Pro </sub>  

#### Identify neglected pools

If a swimming pool is neglected, as when the property is foreclosed, it often turns a green color and becomes inviting to mosquitoes – standing water with no inputs or outputs. The sheer volume of properties affected in warmer climates, even as the market rebounded, has made the detection of these risky pools challenging for many organizations.

Public health and mosquito control agencies are tasked with protecting the public from vector-borne diseases, including viruses carried by mosquitoes like West Nile and Chikungunya. These agencies need a simple solution that helps them locate neglected pools from imagery and then use this intelligence to drive [field activity and mitigation efforts](http://solutions.arcgis.com/local-government/public-works/mosquito-control/).

![Clean and Green Pools](https://www.esri.com/arcgis-blog/wp-content/uploads/2018/07/pools2.png)

<sub>  Green or Clean Pools </sub>  

## Enviroment Setup
The project used Amazon p2.xlarge for training and inference.Fast.ai V2 community AMI(ami-c6ac1cbc) was used, as it comes set up with all the required enviroments and libraries. To setup your own AWS instance follow [this guide](https://github.com/reshamas/fastai_deeplearn_part1/blob/master/tools/aws_ami_gpu_setup.md)

After setting the AMI up you need to run the following commands.
```shell
sudo apt update
sudo apt upgrade
cd fastai
conda env update
conda update --all 
```

If you want to set it up locally then you need to have a CUDA supported NVIDIA GPU.

Following are the libraries and tools you will need to install.
```
Anaconda
PyTorch v0.3+
Fastai (https://github.com/fastai/fastai)
CUDA V9.0
CuDNN
```

After setting up the AMI/Local machine, we need the following two more libraries. To install them just type in the following command in the terminal.

```bash
conda install -c esri arcgis
conda install -c conda-forge shapely
```

In your project home make a symlink using the following command
```shell
ln -s PATH_TO_CLONED_FASTAI_GITHUB_REPO/fastai fastai
```

## Workflow

The `data` directory contains a shapefile of swimming pools.The shapefile format is a popular geospatial vector data format for geographic information system (GIS). If you want to train your own object detector on satellite imagery, you will need this shapefile which can be easily created using ArcGIS pro software for Windows.

### Create shapefile and Image Extraction

You can manually label datset using ArcGIS pro software and then create a shapefile so that our notebook can be used to extract images. After you have created the shapefile you need to run the `Export Training Samples.ipynb` after setting up the path of the shapefile in the `PATH` variable. The images will be extracted from the specific locations in the shapefile and will be stored in the images folder in the directory of the shapefile.

One more method that to use ArcGIS pro software to extract the images also. If you use this method then the labels of the images will be created in PascalVOC format. We also provide a notebook `Convert Pascal VOC to Tilemapping.ipynb` to convert that file into tilemapping file, which is further used in training notebook

![Screenshot of PascalVOC format downloading](https://user-images.githubusercontent.com/16683472/43246778-5d7ab360-90d0-11e8-930a-d664322992e1.png)

### Train a swimming pool detector

Once the images are downloaded it can be used for training the deep learning network. Once the tilemapping object is created which contains a mapping from filepath to bounding boxes. Here also the `PATH` variable has to be set. 

```python
PATH = Path('path/to/folder/which/contains/tilemapping')
```
Make sure the images are also stored in this directory inside a folder named `images`.

In training you may need to train for longer depending on your data. The visualization of results are at the end of the notebook. This project is for only one class object detector. With minor changes it can be made to work on multi-classe 

Look at the few of our results.
![Our results](https://cdn-images-1.medium.com/max/716/1*rCYlCzQu4EODnOb986m07Q.png)

### Clean Vs Green Pools
This step is specific to our case in which we classify the detected pools as clean or green. The detected pools are downloaded and then mannually classified and stored in directory format. It assumes that the root directory for classification to have `train` and `valid` directories. It also assumes that each directory will have subdirectories for each class. (in this case, `green` and `clean`).

Then the notebook `Clean or Green Pools Training.ipynb` will create a deep learning model which will be able to classify clean and green pools.

![green pool detection](https://cdn-images-1.medium.com/max/896/1*RLD_PDZHBUl1oAYcv7aQOA.png)

### Deploy model's predictions as a Feature Layer.
The deployment code for the project is in `Deploy model to find swimming pools.ipynb`. This notebook is used to run the object detector on a large area whose predictions can be accumulated and then be converted into a feature layer. The webmap can be created using this feature layer. 

Later the the predictions from object detector can used to further classify the pools are clean or green, which also can be converted to a feature layer for visualization on a webmap.

![final results](https://cdn-images-1.medium.com/max/896/1*6-y2UbWpuHvZyEhn3vbPuA.png)
