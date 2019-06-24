from owslib.wfs import WebFeatureService

wfs = WebFeatureService(url='http://stratunits.gs.cloud.ga.gov.au/ows', version='1.1.0')

#print([operation.name for operation in wfs.operations])
#print(list(wfs.contents))

print(wfs.getfeature(typename='gsmlb:GeologicUnit', maxfeatures=1))

# http://stratunits.gs.cloud.ga.gov.au/ows?service=wfs&version=2.0.0&request=GetFeature&count=1&typeNames=gsmlb:GeologicUnit