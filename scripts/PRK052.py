completion = []
completion.append(('13','40', '01', '1.0', '*OPEN'))
completion.append(('13','40', '02', '1.0', '*OPEN'))
completion.append(('13','40', '03', '1.0', '*OPEN'))
completion.append(('13','40', '04', '1.0', '*OPEN'))
completion.append(('13','40', '05', '1.0', '*OPEN'))
completion.append(('13','40', '06', '1.0', '*OPEN'))
completion.append(('13','40', '07', '1.0', '*OPEN'))
completion.append(('13','40', '08', '1.0', '*OPEN'))
completion.append(('13','40', '09', '1.0', '*OPEN'))
completion.append(('13','40', '10', '1.0', '*OPEN'))
completion.append(('13','40', '11', '1.0', '*OPEN'))
completion.append(('13','40', '12', '1.0', '*OPEN'))
completion.append(('13','40', '13', '1.0', '*OPEN'))
completion.append(('13','40', '14', '1.0', '*OPEN'))
completion.append(('13','40', '15', '1.0', '*OPEN'))
completion.append(('13','40', '16', '1.0', '*CLOSED'))
completion.append(('13','40', '17', '1.0', '*CLOSED'))
completion.append(('13','40', '18', '1.0', '*OPEN'))
completion.append(('13','40', '19', '1.0', '*OPEN'))
completion.append(('13','40', '20', '1.0', '*OPEN'))
completion.append(('13','40', '21', '1.0', '*OPEN'))
completion.append(('13','40', '22', '1.0', '*OPEN'))
completion.append(('13','40', '23', '1.0', '*OPEN'))
completion.append(('13','40', '24', '1.0', '*OPEN'))
completion.append(('13','40', '25', '1.0', '*OPEN'))
completion.append(('13','40', '26', '1.0', '*OPEN'))
completion.append(('13','40', '27', '1.0', '*OPEN'))
completion.append(('13','40', '28', '1.0', '*OPEN'))
completion.append(('13','40', '29', '1.0', '*OPEN'))
completion.append(('13','40', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('13 40 01:15')
layerclump.append('13 40 18:30')

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

icv_nr = 2

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
