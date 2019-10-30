completion = []
completion.append(('16','36', '01', '1.0', '*OPEN'))
completion.append(('16','36', '02', '1.0', '*OPEN'))
completion.append(('16','36', '03', '1.0', '*OPEN'))
completion.append(('16','36', '04', '1.0', '*OPEN'))
completion.append(('16','36', '05', '1.0', '*OPEN'))
completion.append(('16','36', '06', '1.0', '*OPEN'))
completion.append(('16','36', '07', '1.0', '*OPEN'))
completion.append(('16','36', '08', '1.0', '*OPEN'))
completion.append(('16','36', '09', '1.0', '*OPEN'))
completion.append(('16','36', '10', '1.0', '*OPEN'))
completion.append(('16','36', '11', '1.0', '*OPEN'))
completion.append(('16','36', '12', '1.0', '*OPEN'))
completion.append(('16','36', '13', '1.0', '*OPEN'))
completion.append(('16','36', '14', '1.0', '*OPEN'))
completion.append(('16','36', '15', '1.0', '*OPEN'))
completion.append(('16','36', '16', '1.0', '*OPEN'))
completion.append(('16','36', '17', '1.0', '*OPEN'))
completion.append(('16','36', '18', '1.0', '*OPEN'))
completion.append(('16','36', '19', '1.0', '*OPEN'))
completion.append(('16','36', '20', '1.0', '*OPEN'))
completion.append(('16','36', '21', '1.0', '*OPEN'))
completion.append(('16','36', '22', '1.0', '*OPEN'))
completion.append(('16','36', '23', '1.0', '*OPEN'))
completion.append(('16','36', '24', '1.0', '*OPEN'))
completion.append(('16','36', '25', '1.0', '*OPEN'))
completion.append(('16','36', '26', '1.0', '*OPEN'))
completion.append(('16','36', '27', '1.0', '*OPEN'))
completion.append(('16','36', '28', '1.0', '*OPEN'))
completion.append(('16','36', '29', '1.0', '*OPEN'))
completion.append(('16','36', '30', '1.0', '*OPEN'))

layerclump = []

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1553

on_time = 1.0

icv_nr = 0

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
