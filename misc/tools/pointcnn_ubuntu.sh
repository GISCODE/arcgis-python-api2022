# Setup of 1.8 PointCNN on Ubuntu

conda create --name pytorcharcgis
conda activate pytorcharcgis

#default miniconda's Python 8.3.2 does not work with the pytorch we need
conda install python=3.7.3

conda install -c conda-forge requests-toolbelt requests_ntlm
conda install -c esri -c fastai -c pytorch arcgis fastai=1.0.54 pytorch=1.1.0 cudatoolkit=10 scikit-image pillow=6.2.1 fastprogress=0.1.21 --no-pin

#conda install -c esri -c plotly -c owlas laspy=1.6.0 plotly=4.5.0 plotly-orca psutil h5py=2.10.0 transforms3d
conda install -c esri -c plotly -c owlas plotly=4.5.0 plotly-orca psutil h5py=2.10.0 transforms3d

#installed laspy==1.6.0. via pip as conda says esri channel doesn't have it
pip install laspy==1.6.0

pip install --no-binary torch-cluster==1.4.5 torch-cluster==1.4.5 --no-cache-dir
pip install --no-binary torch-sparse==0.4.3 torch-sparse==0.4.3 --no-cache-dir
pip install --no-binary torch-scatter==1.4.0 torch-scatter==1.4.0 --no-cache-dir
pip install --no-binary torch-geometric==1.3.2 torch-geometric==1.3.2 --no-cache-dir

#installing ipykernel into jupyter-lab
conda install ipykernel
python -m ipykernel install --user --name pytorcharcgis --display-name="pytorcharcgis env"

# plotly display fix
#if no nodejs installed:
conda install -c conda-forge nodejs 
#if nodejs is older than 8.3.0:
conda update -c conda-forge nodejs 

#from https://plot.ly/python/getting-started/#jupyterlab-support-python-35
conda install jupyterlab=1.2
conda install "ipywidgets=7.5"
# Avoid "JavaScript heap out of memory" errors during extension installation
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build

# jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@1.5.1 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@1.5.1 --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build

# Unset NODE_OPTIONS environment variable
# (OS X/Linux)
unset NODE_OPTIONS
