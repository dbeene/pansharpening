# Set environments
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\darbeene\Desktop\PS\Scenes\Landsat"

# Define algorithm objects
algorithms = [('IHS', ''), ('BROVEY', ''), ('Esri', ''), ('SIMPLE_MEAN', ''), ('Gram-Schmidt', 'Landsat 8')]

# Define scenes
scenes = [
('sfo', 'ms_sfo.img','pan_sfo.img',0.4023,0.5163,0.08139,0),
('rio', 'ms_rio.img','pan_rio.img',0.6317,0,0.3408,0.02753),
('stk', 'ms_stk.img','pan_stk.img',0.493,0.3296,0.1687,0.008707),
('tri', 'ms_tri.img','pan_tri.img',0.3894,0.5661,0.04447),
('was', 'ms_was.img','pan_was.img',0.572,0,0.4162,0.01179)
]

for s in scenes:
    arcpy.ComputePansharpenWeights_management('{}'.format(s[1]),'{}'.format(s[2]),"4 3 2 5")

for s in scenes:
    for a in algorithms:
        arcpy.CreatePansharpenedRasterDataset_management(
        '{}'.format(s[1]),
        4,3,2,5,
        arcpy.env.workspace + '\Processed\\'+'{}'.format(a[0])+'_'+'{}'.format(s[0])+'.tif',
        '{}'.format(s[2]),
        '{}'.format(a[0]),
        '{}'.format(s[3]),
        '{}'.format(s[4]),
        '{}'.format(s[5]),
        '{}'.format(s[6]),
        '{}'.format(a[1]))

