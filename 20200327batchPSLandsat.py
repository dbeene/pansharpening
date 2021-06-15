# Set environments
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\darbeene\Desktop\PS\Scenes\Landsat"

# Define algorithms as Py objects
algorithms = [('IHS', ''), ('BROVEY', ''), ('Esri', ''), ('SIMPLE_MEAN', ''), ('Gram-Schmidt', 'Landsat 8')]

# Define scenes
scenes = [
('sfo', 'ms_sfo.img','pan_sfo.img',0.4023,0.5163,0.08139,0),
('rio', 'ms_rio.img','pan_rio.img',0.6317,0,0.3408,0.02753),
('stk', 'ms_stk.img','pan_stk.img',0.493,0.3296,0.1687,0.008707),
('tri', 'ms_tri.img','pan_tri.img',0.3894,0.5661,0.04447),
('was', 'ms_was.img','pan_was.img',0.572,0,0.4162,0.01179)
]

# Compute Weights (only required for Esri)

##for s in scenes:
##    arcpy.ComputePansharpenWeights_management('{}'.format(s[1]),'{}'.format(s[2]),"4 3 2 5")

# Create pansharpened rasters using nested for loop
for s in scenes:
    for a in algorithms:
        arcpy.CreatePansharpenedRasterDataset_management(
        '{}'.format(s[1]), # in_raster
        4,3,2,5, # r, g, b, nir channels
        arcpy.env.workspace + '\Processed\\'+'{}'.format(a[0])+'_'+'{}'.format(s[0])+'.tif' # out_raster_dataset
        , '{}'.format(s[2]) # in_panchromatic_image
        , '{}'.format(a[0]) # pansharpening_type
        , '{}'.format(s[3]) # red_weight
        , '{}'.format(s[4]) # green_weight
        , '{}'.format(s[5]) # blue_weight
        , '{}'.format(s[6]) # infrared_weight
        , '{}'.format(a[1])) # sensor
