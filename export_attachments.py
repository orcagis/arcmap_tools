#-------------------------------------------------------------------------------
# Name:        Export Attachments
# Purpose:     Exports attachments (stored as a blob field) to a specified folder location.  
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     06/13/2022
#
# Interpreter: C:\Python27\ArcGIS10.8\python.exe
#-------------------------------------------------------------------------------

import arcpy
from arcpy import da
import os

def main():
    
    inTable = arcpy.GetParameterAsText(0)
    fileLocation = arcpy.GetParameterAsText(1)

    with da.SearchCursor(inTable, ['DATA', 'ATT_NAME', 'ATTACHMENTID']) as cursor:
        for item in cursor:
            attachment = item[0]
            #filenum = "ATT" + str(item[2]) + "_"
            #filename = filenum + str(item[1])
            filename = str(item[1])
            open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
            del item
            #del filenum
            del filename
            del attachment

if __name__ == "__main__":
    main()
