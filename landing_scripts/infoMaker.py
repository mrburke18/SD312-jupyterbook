import json
from datetime import date

x = dict()
x['year']=2026
x['start']=(1,6)
x['end']=(5,28)
x['lectures']='MWR'
#x['labs']='R'
x['holidays']=(
    (1,19,'MLK Jr. Day'),
    (2,16,'Washington\'s Birthday'),
    (3,9,'Spring Break'),
    (3,10,'Spring Break'),
    (3,11,'Spring Break'),
    (3,12,'Spring Break'),
    (3,13,'Spring Break'),
    (4,1,'Comp Day'),
    )
x['weird']=(
    (1,6,'M'),
    )
x['other']=(
    (4,14,'Guest Speaker, T-Period, Mahan Auditorium'),
    (4,17,'Guest Speaker, T-Period, Hopper 513'),
    (5,8,'Last Day of Finals'),
    )
x['time']=(
    (7,30)
    )

with open('courseInfo.json','w') as f:
  json.dump(x,f,indent=2)
