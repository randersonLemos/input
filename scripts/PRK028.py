completion = []
completion.append(('23', '17', '01', '1.0', '*OPEN'))
completion.append(('23', '17', '02', '1.0', '*OPEN'))
completion.append(('23', '17', '03', '1.0', '*OPEN'))
completion.append(('23', '17', '04', '1.0', '*OPEN'))
completion.append(('23', '17', '05', '1.0', '*OPEN'))
completion.append(('23', '17', '06', '1.0', '*OPEN'))
completion.append(('23', '17', '07', '1.0', '*OPEN'))
completion.append(('23', '17', '08', '1.0', '*OPEN'))
completion.append(('23', '17', '09', '1.0', '*OPEN'))
completion.append(('23', '17', '10', '1.0', '*OPEN'))
completion.append(('23', '17', '11', '1.0', '*OPEN'))
completion.append(('23', '17', '12', '1.0', '*OPEN'))
completion.append(('23', '17', '13', '1.0', '*OPEN'))
completion.append(('23', '17', '14', '1.0', '*OPEN'))
completion.append(('23', '17', '15', '1.0', '*OPEN'))
completion.append(('23', '17', '16', '1.0', '*OPEN'))
completion.append(('23', '17', '17', '1.0', '*OPEN'))
completion.append(('23', '17', '18', '1.0', '*OPEN'))
completion.append(('23', '17', '19', '1.0', '*CLOSED'))
completion.append(('23', '17', '20', '1.0', '*CLOSED'))
completion.append(('23', '17', '21', '1.0', '*OPEN'))
completion.append(('23', '17', '22', '1.0', '*OPEN'))
completion.append(('23', '17', '23', '1.0', '*OPEN'))
completion.append(('23', '17', '24', '1.0', '*OPEN'))
completion.append(('23', '17', '25', '1.0', '*OPEN'))
completion.append(('23', '17', '26', '1.0', '*OPEN'))
completion.append(('23', '17', '27', '1.0', '*OPEN'))
completion.append(('23', '17', '28', '1.0', '*OPEN'))
completion.append(('23', '17', '29', '1.0', '*OPEN'))
completion.append(('23', '17', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('23 17 01:18')
layerclump.append('23 17 21:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

on_time = 1.0

openn = 1612

icv_nr = 2

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
