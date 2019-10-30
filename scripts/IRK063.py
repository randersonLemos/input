completion = []
completion.append(('37', '56', '01', '1.0', '*OPEN'))
completion.append(('37', '56', '02', '1.0', '*OPEN'))
completion.append(('37', '56', '03', '1.0', '*OPEN'))
completion.append(('37', '56', '04', '1.0', '*OPEN'))
completion.append(('37', '56', '05', '1.0', '*OPEN'))
completion.append(('37', '56', '06', '1.0', '*OPEN'))
completion.append(('37', '56', '07', '1.0', '*OPEN'))
completion.append(('37', '56', '08', '1.0', '*OPEN'))
completion.append(('37', '56', '09', '1.0', '*OPEN'))
completion.append(('37', '56', '10', '1.0', '*OPEN'))
completion.append(('37', '56', '11', '1.0', '*OPEN'))
completion.append(('37', '56', '12', '1.0', '*OPEN'))
completion.append(('37', '56', '13', '1.0', '*OPEN'))
completion.append(('37', '56', '14', '1.0', '*OPEN'))
completion.append(('37', '56', '15', '1.0', '*CLOSED'))
completion.append(('37', '56', '16', '1.0', '*CLOSED'))
completion.append(('37', '56', '17', '1.0', '*OPEN'))
completion.append(('37', '56', '18', '1.0', '*OPEN'))
completion.append(('37', '56', '19', '1.0', '*OPEN'))
completion.append(('37', '56', '20', '1.0', '*OPEN'))
completion.append(('37', '56', '21', '1.0', '*OPEN'))
completion.append(('37', '56', '22', '1.0', '*OPEN'))
completion.append(('37', '56', '23', '1.0', '*OPEN'))
completion.append(('37', '56', '24', '1.0', '*OPEN'))
completion.append(('37', '56', '25', '1.0', '*OPEN'))
completion.append(('37', '56', '26', '1.0', '*OPEN'))
completion.append(('37', '56', '27', '1.0', '*OPEN'))
completion.append(('37', '56', '28', '1.0', '*OPEN'))
completion.append(('37', '56', '29', '1.0', '*OPEN'))
completion.append(('37', '56', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('37 56 01:14')
layerclump.append('37 56 17:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('G', 1278.0)

on_time = 0.98

wag_cycle = ('W', 1918.0, 183.0, 100)

icv_nr = None

icv_start = None

icv_control = None