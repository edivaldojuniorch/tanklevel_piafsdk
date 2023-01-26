import sys
import clr

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')  
clr.AddReference('OSIsoft.AFSDK')

from OSIsoft.AF import *
from OSIsoft.AF.PI import *
from OSIsoft.AF.Search import * 
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *  
from OSIsoft.AF.UnitsOfMeasure import *


class PIIntegration(object):
    def connect_to_piserver(self, serverName):

        piServers = PIServers()
        global piServer

        piServer = piServers[serverName]
        piServer.Connect(False)        

        print("Connected to server: " + serverName)

    def find_tags(self, mask):
        tags = PIPoint.FindPIPoints(piServer, mask, None, None)
        tags = list(tags)
        return [print(i.get_Name()) for i in tags]

    def write_tag_value (self, tagName,timestamp, value):
        writeTag = PIPoint.FindPIPoint(piServer, tagName)
        valueObj = AFValue(value, AFTime(timestamp))
        writeTag.UpdateValue(valueObj, AFUpdateOption.Replace, AFBufferOption.BufferIfPossible)
        print('Tag"' + tagName + '" updated')


    def get_tag_value_snapshot(self, tagName):
        tag = PIPoint.FindPIPoint(piServer, tagName)
        snapValue = tag.Snapshot()
        
        return snapValue.Value, snapValue.Timestamp.LocalTime

    def get_tag_value_sample(self, tagName, initDate, enddate, span):
        tag = PIPoint.FindPIPoint(piServer, tagName)
        timerange = AFTimeRange(initDate, enddate)
        sampleValue =tag.InterpolatedValues(timerange, AFTimeSpan.Parse(span), '', False)  

        for event in sampleValue:
            print('timestamp:{0} value:{1}'.format(event.Timestamp.LocalTime, event.Value))

        return sampleValue
    
    def get_tag_value_recorded(self, tagName, initDate, enddate):
        tag = PIPoint.FindPIPoint(piServer, tagName)
        timerange = AFTimeRange(initDate, enddate)
        recordedValue = tag.RecordedValues(timerange, AFBoundaryType.Inside, '', False)

        for event in recordedValue:
            print('timestamp:{0} value:{1}'.format(event.Timestamp.LocalTime, event.Value))

        return recordedValue

    
