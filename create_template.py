import gdal

template_file = r'E:\data\basin\3secSRTM_DEM\DEM_ESRI_GRID_16bit_Integer\dem3s_int\hdr.adf'

template = gdal.Open(template_file)
template_transform = template.GetGeoTransform()
template_w = template.RasterXSize
template_h = template.RasterYSize

target = gdal.GetDriverByName('GTiff').Create(
    'template.tif',
    template_w,
    template_h,
    1,
    gdal.GDT_Byte,
    ["COMPRESS=LZW", "SPARSE_OK=TRUE"]
)

target.SetGeoTransform(template_transform)
target.SetProjection(template.GetProjection())
