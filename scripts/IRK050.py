completion = []
completion.append(('10', '46', '01', '1.0', '*OPEN'))
completion.append(('10', '46', '02', '1.0', '*OPEN'))
completion.append(('10', '46', '03', '1.0', '*OPEN'))
completion.append(('10', '46', '04', '1.0', '*OPEN'))
completion.append(('10', '46', '05', '1.0', '*OPEN'))
completion.append(('10', '46', '06', '1.0', '*OPEN'))
completion.append(('10', '46', '07', '1.0', '*OPEN'))
completion.append(('10', '46', '08', '1.0', '*OPEN'))
completion.append(('10', '46', '09', '1.0', '*OPEN'))
completion.append(('10', '46', '10', '1.0', '*OPEN'))
completion.append(('10', '46', '11', '1.0', '*OPEN'))
completion.append(('10', '46', '12', '1.0', '*OPEN'))
completion.append(('10', '46', '13', '1.0', '*OPEN'))
completion.append(('10', '46', '14', '1.0', '*OPEN'))
completion.append(('10', '46', '15', '1.0', '*OPEN'))
completion.append(('10', '46', '16', '1.0', '*CLOSED'))
completion.append(('10', '46', '17', '1.0', '*CLOSED'))
completion.append(('10', '46', '18', '1.0', '*OPEN'))
completion.append(('10', '46', '19', '1.0', '*OPEN'))
completion.append(('10', '46', '20', '1.0', '*OPEN'))
completion.append(('10', '46', '21', '1.0', '*OPEN'))
completion.append(('10', '46', '22', '1.0', '*OPEN'))
completion.append(('10', '46', '23', '1.0', '*OPEN'))
completion.append(('10', '46', '24', '1.0', '*OPEN'))
completion.append(('10', '46', '25', '1.0', '*OPEN'))
completion.append(('10', '46', '26', '1.0', '*OPEN'))
completion.append(('10', '46', '27', '1.0', '*OPEN'))
completion.append(('10', '46', '28', '1.0', '*OPEN'))
completion.append(('10', '46', '29', '1.0', '*OPEN'))
completion.append(('10', '46', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('10 46 01:15')
layerclump.append('10 46 18:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('W', 1461.0)

wag_cycle = ('G', 1918.0, 183.0, 100)

on_time = 0.98

icv_nr = None

icv_start = None

icv_control = None
