import cx_Oracle
from osgeo import ogr, gdal

dsnStr = cx_Oracle.makedsn("localhost", "32769", "ORCLCDB")
connection = cx_Oracle.connect('username', 'password', dsn=dsnStr)

cursor = connection.cursor()

sql = "SELECT name, sdo_util.TO_WKTGEOMETRY(geometry) FROM PROVINCEFULLEXTENT"

cursor.execute(sql)

template_file = r'3arcsecond_template.tif'
print(template_file)

template = gdal.Open(template_file)
template_transform = template.GetGeoTransform()
template_w = template.RasterXSize
template_h = template.RasterYSize

target = gdal.GetDriverByName('GTiff').Create(
    'test.tif',
    template_w,
    template_h,
    1,
    gdal.GDT_Byte,
    ["COMPRESS=LZW"]
)

target.SetGeoTransform(template_transform)
target.SetProjection(template.GetProjection())

ds = ogr.GetDriverByName('Memory').CreateDataSource('wrk')
layer = ds.CreateLayer('poly')

for name, geom in cursor:
    print(name)
    # print(geom)
    # print(dir(geom))

    feature = ogr.Feature(layer.GetLayerDefn())
    feature.SetGeometryDirectly(ogr.Geometry(wkt=str(geom)))

    layer.CreateFeature(feature)

gdal.RasterizeLayer(target, [1], layer, None, None, [1], ['ALL_TOUCHED=TRUE'])

#x = target.GetRasterBand(1).ReadAsArray()
#print(x)
