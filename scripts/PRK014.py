completion = []
completion.append(('25', '10', '01', '1.0', '*OPEN'))
completion.append(('25', '10', '02', '1.0', '*OPEN'))
completion.append(('25', '10', '03', '1.0', '*OPEN'))
completion.append(('25', '10', '04', '1.0', '*OPEN'))
completion.append(('25', '10', '05', '1.0', '*OPEN'))
completion.append(('25', '10', '06', '1.0', '*OPEN'))
completion.append(('25', '10', '07', '1.0', '*OPEN'))
completion.append(('25', '10', '08', '1.0', '*OPEN'))
completion.append(('25', '10', '09', '1.0', '*OPEN'))
completion.append(('25', '10', '10', '1.0', '*OPEN'))
completion.append(('25', '10', '11', '1.0', '*OPEN'))
completion.append(('25', '10', '12', '1.0', '*CLOSED'))
completion.append(('25', '10', '13', '1.0', '*CLOSED'))
completion.append(('25', '10', '14', '1.0', '*OPEN'))
completion.append(('25', '10', '15', '1.0', '*OPEN'))
completion.append(('25', '10', '16', '1.0', '*OPEN'))
completion.append(('25', '10', '17', '1.0', '*OPEN'))
completion.append(('25', '10', '18', '1.0', '*OPEN'))
completion.append(('25', '10', '19', '1.0', '*OPEN'))
completion.append(('25', '10', '20', '1.0', '*CLOSED'))
completion.append(('25', '10', '21', '1.0', '*CLOSED'))
completion.append(('25', '10', '22', '1.0', '*OPEN'))
completion.append(('25', '10', '23', '1.0', '*OPEN'))
completion.append(('25', '10', '24', '1.0', '*OPEN'))
completion.append(('25', '10', '25', '1.0', '*OPEN'))
completion.append(('25', '10', '26', '1.0', '*OPEN'))
completion.append(('25', '10', '27', '1.0', '*OPEN'))
completion.append(('25', '10', '28', '1.0', '*OPEN'))
completion.append(('25', '10', '29', '1.0', '*OPEN'))
completion.append(('25', '10', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('25 10 01:11')
layerclump.append('25 10 14:19')
layerclump.append('25 10 22:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1704

on_time = 1.0

icv_nr = 3

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
