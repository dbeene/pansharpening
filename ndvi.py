import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

arcpy.env.overwriteOutput = True

path = r'D:\PS\Scenes\Proprietary\Processed'
outpath = r'D:\PS\Scenes\Proprietary\NDVI'

rioraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\BROVEY_rio.tif')

redtmp = arcpy.MakeRasterLayer_management(rioraster,'redtmp','','','7')
nirtmp = arcpy.MakeRasterLayer_management(rioraster,'nirtmp','','','5')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIbroveyRio")

sforaster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\BROVEY_sfo.tif')

redtmp = arcpy.MakeRasterLayer_management(sforaster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(sforaster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIbroveySfo")

stkraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\BROVEY_stk.tif')

redtmp = arcpy.MakeRasterLayer_management(stkraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(stkraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIbroveyStk")

triraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\BROVEY_tri.tif')

redtmp = arcpy.MakeRasterLayer_management(triraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(triraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIbroveyTri")

wasraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\BROVEY_was.tif')

redtmp = arcpy.MakeRasterLayer_management(wasraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(wasraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIbroveyWas")

rioraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Esri_rio.tif')

redtmp = arcpy.MakeRasterLayer_management(rioraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(rioraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIesriRio")

sforaster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Esri_sfo.tif')

redtmp = arcpy.MakeRasterLayer_management(sforaster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(sforaster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIesriSfo")

stkraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Esri_stk.tif')

redtmp = arcpy.MakeRasterLayer_management(stkraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(stkraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIesriStk")

triraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Esri_tri.tif')

redtmp = arcpy.MakeRasterLayer_management(triraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(triraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIesriTri")

wasraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Esri_was.tif')

redtmp = arcpy.MakeRasterLayer_management(wasraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(wasraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIesriWas")

rioraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\IHS_rio.tif')

redtmp = arcpy.MakeRasterLayer_management(rioraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(rioraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIihsRio")

sforaster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\IHS_sfo.tif')

redtmp = arcpy.MakeRasterLayer_management(sforaster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(sforaster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIihsSfo")

stkraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\IHS_stk.tif')

redtmp = arcpy.MakeRasterLayer_management(stkraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(stkraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIihsStk")

triraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\IHS_tri.tif')

redtmp = arcpy.MakeRasterLayer_management(triraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(triraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIihsTri")

wasraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\IHS_was.tif')

redtmp = arcpy.MakeRasterLayer_management(wasraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(wasraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIihsWas")

rioraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\SIMPLE_MEAN_rio.tif')

redtmp = arcpy.MakeRasterLayer_management(rioraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(rioraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIsmRio")

sforaster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\SIMPLE_MEAN_sfo.tif')

redtmp = arcpy.MakeRasterLayer_management(sforaster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(sforaster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIsmSfo")

stkraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\SIMPLE_MEAN_stk.tif')

redtmp = arcpy.MakeRasterLayer_management(stkraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(stkraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIsmStk")

triraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\SIMPLE_MEAN_tri.tif')

redtmp = arcpy.MakeRasterLayer_management(triraster,'redtmp','','','5')
nirtmp = arcpy.MakeRasterLayer_management(triraster,'nirtmp','','','7')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIsmTri")

wasraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\SIMPLE_MEAN_was.tif')

redtmp = arcpy.MakeRasterLayer_management(wasraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(wasraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIsmWas")

rioraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Gram-Schmidt_rio.tif')

redtmp = arcpy.MakeRasterLayer_management(rioraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(rioraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIgsRio")

sforaster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Gram-Schmidt_sfo.tif')

redtmp = arcpy.MakeRasterLayer_management(sforaster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(sforaster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIgsSfo")

stkraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Gram-Schmidt_stk.tif')

redtmp = arcpy.MakeRasterLayer_management(stkraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(stkraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIgsStk")

triraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Gram-Schmidt_tri.tif')

redtmp = arcpy.MakeRasterLayer_management(triraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(triraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIgsTri")

wasraster = arcpy.Raster(r'D:\PS\Scenes\Proprietary\Processed\Gram-Schmidt_was.tif')

redtmp = arcpy.MakeRasterLayer_management(wasraster,'redtmp','','','3')
nirtmp = arcpy.MakeRasterLayer_management(wasraster,'nirtmp','','','4')

red = arcpy.gp.Float_sa("redtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/red")
nir = arcpy.gp.Float_sa("nirtmp", "C:/Users/darbeene/Documents/ArcGIS/Default.gdb/nir")

arcpy.gp.RasterCalculator_sa('("nir"-"red")/("nir"+"red")', "D:/PS/Scenes/Proprietary/NDVI/NDVIgsWas")

arcpy.CheckInExtension("Spatial")

print("Finished.")