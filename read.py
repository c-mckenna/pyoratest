import gdal
import numpy as np

ds = gdal.Open('test.tif')

x = ds.GetRasterBand(1).ReadAsArray()
print(np.max(x))
