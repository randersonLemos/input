completion = []
completion.append(('23','55', '01', '1.0', '*OPEN'))
completion.append(('23','55', '02', '1.0', '*OPEN'))
completion.append(('23','55', '03', '1.0', '*OPEN'))
completion.append(('23','55', '04', '1.0', '*OPEN'))
completion.append(('23','55', '05', '1.0', '*OPEN'))
completion.append(('23','55', '06', '1.0', '*OPEN'))
completion.append(('23','55', '07', '1.0', '*OPEN'))
completion.append(('23','55', '08', '1.0', '*OPEN'))
completion.append(('23','55', '09', '1.0', '*OPEN'))
completion.append(('23','55', '10', '1.0', '*OPEN'))
completion.append(('23','55', '11', '1.0', '*OPEN'))
completion.append(('23','55', '12', '1.0', '*CLOSED'))
completion.append(('23','55', '13', '1.0', '*CLOSED'))
completion.append(('23','55', '14', '1.0', '*OPEN'))
completion.append(('23','55', '15', '1.0', '*OPEN'))
completion.append(('23','55', '16', '1.0', '*OPEN'))
completion.append(('23','55', '17', '1.0', '*OPEN'))
completion.append(('23','55', '18', '1.0', '*OPEN'))
completion.append(('23','55', '19', '1.0', '*OPEN'))
completion.append(('23','55', '20', '1.0', '*OPEN'))
completion.append(('23','55', '21', '1.0', '*OPEN'))
completion.append(('23','55', '22', '1.0', '*OPEN'))
completion.append(('23','55', '23', '1.0', '*OPEN'))
completion.append(('23','55', '24', '1.0', '*OPEN'))
completion.append(('23','55', '25', '1.0', '*OPEN'))
completion.append(('23','55', '26', '1.0', '*OPEN'))
completion.append(('23','55', '27', '1.0', '*OPEN'))
completion.append(('23','55', '28', '1.0', '*OPEN'))
completion.append(('23','55', '29', '1.0', '*OPEN'))
completion.append(('23','55', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('23 55 01:11')
layerclump.append('23 55 14:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1308

on_time = 1.0

icv_nr = 2

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
