# Set environments
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\darbeene\Desktop\PS\Scenes\Proprietary" # Define workspace

# Define algorithms Py objects
algorithms = [('IHS', ''), ('BROVEY', ''), ('Esri', ''), ('SIMPLE_MEAN', ''), ('Gram-Schmidt', '')]

# Define scenes

scenes = [
('sfo', 'ms_sfo.tif','pan_sfo.tif',3,2,1,4,0.03555,0.4652,0,0.4992),
('rio', 'ms_rio.tif','pan_rio.tif',5,3,2,7,0.4834,0.0496,0.2857,0.1813),
('stk', 'ms_stk.tif','pan_stk.tif',5,3,2,7,0.4041,0.1716,0.2195,0.2048),
('tri', 'ms_tri.tif','pan_tri.tif',5,3,2,7,0.3937,0.03117,0.4153,0.1598),
('was', 'ms_was.tif','pan_was.tif',3,2,1,4,0.3601,0.09414,0.3964,0.1494)
]

# Compute Weights (only required for Esri)

##for s in scenes:
##    arcpy.ComputePansharpenWeights_management('{}'.format(s[1]),'{}'.format(s[2]),str('{}'.format(s[3]) + " " + '{}'.format(s[4]) + " " + '{}'.format(s[5]) + " " + '{}'.format(s[6])))

# Create pansharpened rasters using nested for loop
for s in scenes:
    for a in algorithms:
        arcpy.CreatePansharpenedRasterDataset_management(
        '{}'.format(s[1]), # in_raster
        '{}'.format(s[3]), # red_channel
        '{}'.format(s[4]), # green_channel
        '{}'.format(s[5]), # blue_channel
        '{}'.format(s[6]), # infrared_channel
        arcpy.env.workspace + '\Processed\\'+'{}'.format(a[0])+'_'+'{}'.format(s[0])+'.tif', # out_raster_dataset
        '{}'.format(s[2]), # in_panchromatic_image
        '{}'.format(a[0]), # pansharpening_type
        '{}'.format(s[7]), # red_weight
        '{}'.format(s[8]), # green_weight
        '{}'.format(s[9]), # blue_weight
        '{}'.format(s[10]), # infrared_weight
        '{}'.format(a[1])) # sensor

    # Calculate NDVI, in separate script, <ndvi.py>
