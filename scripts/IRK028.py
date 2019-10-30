completion = []
completion.append(('41', '30', '01', '1.0', '*OPEN'))
completion.append(('41', '30', '02', '1.0', '*OPEN'))
completion.append(('41', '30', '03', '1.0', '*OPEN'))
completion.append(('41', '30', '04', '1.0', '*OPEN'))
completion.append(('41', '30', '05', '1.0', '*OPEN'))
completion.append(('41', '30', '06', '1.0', '*OPEN'))
completion.append(('41', '30', '07', '1.0', '*OPEN'))
completion.append(('41', '30', '08', '1.0', '*OPEN'))
completion.append(('41', '30', '09', '1.0', '*OPEN'))
completion.append(('41', '30', '10', '1.0', '*OPEN'))
completion.append(('41', '30', '11', '1.0', '*OPEN'))
completion.append(('41', '30', '12', '1.0', '*OPEN'))
completion.append(('41', '30', '13', '1.0', '*OPEN'))
completion.append(('41', '30', '14', '1.0', '*OPEN'))
completion.append(('41', '30', '15', '1.0', '*CLOSED'))
completion.append(('41', '30', '16', '1.0', '*CLOSED'))
completion.append(('41', '30', '17', '1.0', '*OPEN'))
completion.append(('41', '30', '18', '1.0', '*OPEN'))
completion.append(('41', '30', '19', '1.0', '*OPEN'))
completion.append(('41', '30', '20', '1.0', '*OPEN'))
completion.append(('41', '30', '21', '1.0', '*OPEN'))
completion.append(('41', '30', '22', '1.0', '*OPEN'))
completion.append(('41', '30', '23', '1.0', '*OPEN'))
completion.append(('41', '30', '24', '1.0', '*OPEN'))
completion.append(('41', '30', '25', '1.0', '*OPEN'))
completion.append(('41', '30', '26', '1.0', '*OPEN'))
completion.append(('41', '30', '27', '1.0', '*OPEN'))
completion.append(('41', '30', '28', '1.0', '*OPEN'))
completion.append(('41', '30', '29', '1.0', '*OPEN'))
completion.append(('41', '30', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('41 30 01:14')
layerclump.append('41 30 17:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('W', 1643.0)

on_time = 0.98

wag_cycle = ('G', 1918.0, 183.0, 100)

icv_nr = None

icv_start = None

icv_control = None
