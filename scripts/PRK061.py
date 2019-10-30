completion = []
completion.append(('26','34', '01', '1.0', '*OPEN'))
completion.append(('26','34', '02', '1.0', '*OPEN'))
completion.append(('26','34', '03', '1.0', '*OPEN'))
completion.append(('26','34', '04', '1.0', '*OPEN'))
completion.append(('26','34', '05', '1.0', '*OPEN'))
completion.append(('26','34', '06', '1.0', '*OPEN'))
completion.append(('26','34', '07', '1.0', '*OPEN'))
completion.append(('26','34', '08', '1.0', '*OPEN'))
completion.append(('26','34', '09', '1.0', '*OPEN'))
completion.append(('26','34', '10', '1.0', '*OPEN'))
completion.append(('26','34', '11', '1.0', '*OPEN'))
completion.append(('26','34', '12', '1.0', '*CLOSED'))
completion.append(('26','34', '13', '1.0', '*CLOSED'))
completion.append(('26','34', '14', '1.0', '*OPEN'))
completion.append(('26','34', '15', '1.0', '*OPEN'))
completion.append(('26','34', '16', '1.0', '*OPEN'))
completion.append(('26','34', '17', '1.0', '*OPEN'))
completion.append(('26','34', '18', '1.0', '*CLOSED'))
completion.append(('26','34', '19', '1.0', '*CLOSED'))
completion.append(('26','34', '20', '1.0', '*OPEN'))
completion.append(('26','34', '21', '1.0', '*OPEN'))
completion.append(('26','34', '22', '1.0', '*OPEN'))
completion.append(('26','34', '23', '1.0', '*OPEN'))
completion.append(('26','34', '24', '1.0', '*OPEN'))
completion.append(('26','34', '25', '1.0', '*OPEN'))
completion.append(('26','34', '26', '1.0', '*OPEN'))
completion.append(('26','34', '27', '1.0', '*OPEN'))
completion.append(('26','34', '28', '1.0', '*OPEN'))
completion.append(('26','34', '29', '1.0', '*OPEN'))
completion.append(('26','34', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('26 34 01:11')
layerclump.append('26 34 14:17')
layerclump.append('26 34 20:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1673

on_time = 1.0

icv_nr = 3

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
