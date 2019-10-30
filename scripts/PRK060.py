completion = []
completion.append(('25','45', '01', '1.0', '*OPEN'))
completion.append(('25','45', '02', '1.0', '*OPEN'))
completion.append(('25','45', '03', '1.0', '*OPEN'))
completion.append(('25','45', '04', '1.0', '*OPEN'))
completion.append(('25','45', '05', '1.0', '*OPEN'))
completion.append(('25','45', '06', '1.0', '*OPEN'))
completion.append(('25','45', '07', '1.0', '*OPEN'))
completion.append(('25','45', '08', '1.0', '*OPEN'))
completion.append(('25','45', '09', '1.0', '*OPEN'))
completion.append(('25','45', '10', '1.0', '*OPEN'))
completion.append(('25','45', '11', '1.0', '*OPEN'))
completion.append(('25','45', '12', '1.0', '*CLOSED'))
completion.append(('25','45', '13', '1.0', '*CLOSED'))
completion.append(('25','45', '14', '1.0', '*OPEN'))
completion.append(('25','45', '15', '1.0', '*OPEN'))
completion.append(('25','45', '16', '1.0', '*OPEN'))
completion.append(('25','45', '17', '1.0', '*OPEN'))
completion.append(('25','45', '18', '1.0', '*OPEN'))
completion.append(('25','45', '19', '1.0', '*OPEN'))
completion.append(('25','45', '20', '1.0', '*OPEN'))
completion.append(('25','45', '21', '1.0', '*OPEN'))
completion.append(('25','45', '22', '1.0', '*OPEN'))
completion.append(('25','45', '23', '1.0', '*OPEN'))
completion.append(('25','45', '24', '1.0', '*OPEN'))
completion.append(('25','45', '25', '1.0', '*OPEN'))
completion.append(('25','45', '26', '1.0', '*OPEN'))
completion.append(('25','45', '27', '1.0', '*OPEN'))
completion.append(('25','45', '28', '1.0', '*OPEN'))
completion.append(('25','45', '29', '1.0', '*OPEN'))
completion.append(('25','45', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('25 45 01:11')
layerclump.append('25 45 14:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1492

on_time = 1.0

icv_nr = 2

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr
