#Load first data shp file.
dizin= 'D:\Program Files\QGIS 3.10\bin\gdalplugins\cbsproject\data'
dosya='ne_10m_land.shp'
iface.addVectorLayer(dizin + dosya, '(world)', 'ogr')

#Load second data shp file.
dizin2='D:\Program Files\QGIS 3.10\bin\gdalplugins\cbsproject\data'
dosya2='ASAM_events.shp'
iface.addVectorLayer(dizin + dosya, '(pirate)', 'ogr')

#Change the name of ASAM_events layer.
layer=iface.activeLayer()
layer.setName('pirate_events')

#Change the name of ne_10m_land layer.
layer=iface.activeLayer()
layer.setName('world')

#Adjusting the symbology of the layers.
layer=QgsProject.instance().mapLayersByName('pirate_events')[0]
symbol = QgsMarkerSymbol.createSimple({'name': 'square', 'color': 'blue'})
layer.renderer().setSymbol(symbol)

layer2=QgsProject.instance().mapLayersByName('world')[0]
symbol2 = QgsMarkerSymbol.createSimple({'name':'gradient fill', 'color': '#ff7b8a'})
layer2.renderer().setSymbol(symbol2)

#Save the project map layout as png file. 
Dizin='D:\Program Files\QGIS 3.10\bin\gdalplugins\cbsproject'
isim='Outputbypyqgis.png'
kanvas=iface.mapCanvas()
kanvas.saveAsImage(Dizin + isim)

#Save the project Layer by Layer as png file.
# create image
img = QImage(QSize(800, 800), QImage.Format_ARGB32_Premultiplied)
 
# set background color
color = QColor(255, 255, 255, 255)
img.fill(color.rgba())
 
# create painter
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)
 
# create map settings
ms = QgsMapSettings()
ms.setBackgroundColor(color)
 
# set layers to render
layer = QgsProject.instance().mapLayersByName('pirate', 'world')
ms.setLayers([layer[0]])
 
# set extent
rect = QgsRectangle(ms.fullExtent())
rect.scale(1.1)
ms.setExtent(rect)
 
# set ouptut size
ms.setOutputSize(img.size())
 
# setup qgis map renderer
render = QgsMapRendererCustomPainterJob(ms, p)
render.start()
render.waitForFinished()
p.end()
 
# save the image
img.save('D:\Program Files\QGIS 3.10\bin\gdalplugins\cbsproject\pyqgisoutput2')
