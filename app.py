from integration import PIIntegration
from random import random
myserverName = "HCGSERVER2016"
mytagName = "first tag.pv"

work = PIIntegration()
work.connect_to_piserver(myserverName)
work.find_tags("*")
# work.write_tag_value(mytagName, "2023-01-25 12:36:30.526524", 12.3)

# for i in range(1,5):
#     work.write_tag_value(mytagName, "2023-01-25 12:3{0}:30.526524".format(i), random())


snap = work.get_tag_value_snapshot(mytagName)
print(snap)

myiniDate = "*-24h"
myendData = "*"
myspan = "1h"

# sample = work.get_tag_value_sample(mytagName,myiniDate, myendData, myspan)
# sample = work.get_tag_value_sample(mytagName,myiniDate, myendData, myspan)
recorded = work.get_tag_value_recorded(mytagName,myiniDate, myendData)


# print(sample)
print(recorded)

