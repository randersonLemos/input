completion = []
completion.append(('19','28', '01', '1.0', '*OPEN'))
completion.append(('19','28', '02', '1.0', '*OPEN'))
completion.append(('19','28', '03', '1.0', '*OPEN'))
completion.append(('19','28', '04', '1.0', '*OPEN'))
completion.append(('19','28', '05', '1.0', '*OPEN'))
completion.append(('19','28', '06', '1.0', '*OPEN'))
completion.append(('19','28', '07', '1.0', '*OPEN'))
completion.append(('19','28', '08', '1.0', '*OPEN'))
completion.append(('19','28', '09', '1.0', '*OPEN'))
completion.append(('19','28', '10', '1.0', '*OPEN'))
completion.append(('19','28', '11', '1.0', '*CLOSED'))
completion.append(('19','28', '12', '1.0', '*CLOSED'))
completion.append(('19','28', '13', '1.0', '*OPEN'))
completion.append(('19','28', '14', '1.0', '*OPEN'))
completion.append(('19','28', '15', '1.0', '*OPEN'))
completion.append(('19','28', '16', '1.0', '*OPEN'))
completion.append(('19','28', '17', '1.0', '*OPEN'))
completion.append(('19','28', '18', '1.0', '*CLOSED'))
completion.append(('19','28', '19', '1.0', '*CLOSED'))
completion.append(('19','28', '20', '1.0', '*OPEN'))
completion.append(('19','28', '21', '1.0', '*OPEN'))
completion.append(('19','28', '22', '1.0', '*OPEN'))
completion.append(('19','28', '23', '1.0', '*OPEN'))
completion.append(('19','28', '24', '1.0', '*OPEN'))
completion.append(('19','28', '25', '1.0', '*OPEN'))
completion.append(('19','28', '26', '1.0', '*OPEN'))
completion.append(('19','28', '27', '1.0', '*OPEN'))
completion.append(('19','28', '28', '1.0', '*OPEN'))
completion.append(('19','28', '29', '1.0', '*OPEN'))
completion.append(('19','28', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('19 28 01:10')
layerclump.append('19 28 13:17')
layerclump.append('19 28 20:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1369

on_time = 1.0

icv_nr = 3

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
