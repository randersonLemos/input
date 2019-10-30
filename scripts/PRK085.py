completion = []
completion.append(('24','60', '01', '1.0', '*OPEN'))
completion.append(('24','60', '02', '1.0', '*OPEN'))
completion.append(('24','60', '03', '1.0', '*OPEN'))
completion.append(('24','60', '04', '1.0', '*OPEN'))
completion.append(('24','60', '05', '1.0', '*OPEN'))
completion.append(('24','60', '06', '1.0', '*OPEN'))
completion.append(('24','60', '07', '1.0', '*OPEN'))
completion.append(('24','60', '08', '1.0', '*OPEN'))
completion.append(('24','60', '09', '1.0', '*OPEN'))
completion.append(('24','60', '10', '1.0', '*CLOSED'))
completion.append(('24','60', '11', '1.0', '*CLOSED'))
completion.append(('24','60', '12', '1.0', '*OPEN'))
completion.append(('24','60', '13', '1.0', '*OPEN'))
completion.append(('24','60', '14', '1.0', '*OPEN'))
completion.append(('24','60', '15', '1.0', '*OPEN'))
completion.append(('24','60', '16', '1.0', '*OPEN'))
completion.append(('24','60', '17', '1.0', '*CLOSED'))
completion.append(('24','60', '18', '1.0', '*CLOSED'))
completion.append(('24','60', '19', '1.0', '*OPEN'))
completion.append(('24','60', '20', '1.0', '*OPEN'))
completion.append(('24','60', '21', '1.0', '*OPEN'))
completion.append(('24','60', '22', '1.0', '*OPEN'))
completion.append(('24','60', '23', '1.0', '*OPEN'))
completion.append(('24','60', '24', '1.0', '*OPEN'))
completion.append(('24','60', '25', '1.0', '*OPEN'))
completion.append(('24','60', '26', '1.0', '*OPEN'))
completion.append(('24','60', '27', '1.0', '*OPEN'))
completion.append(('24','60', '28', '1.0', '*OPEN'))
completion.append(('24','60', '29', '1.0', '*OPEN'))
completion.append(('24','60', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('24 60 01:09')
layerclump.append('24 60 12:16')
layerclump.append('24 60 19:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1247

on_time = 1.0

icv_nr = 3

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
