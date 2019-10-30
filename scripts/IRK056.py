completion = []
completion.append(('41', '51', '01', '1.0', '*OPEN'))
completion.append(('41', '51', '02', '1.0', '*OPEN'))
completion.append(('41', '51', '03', '1.0', '*OPEN'))
completion.append(('41', '51', '04', '1.0', '*OPEN'))
completion.append(('41', '51', '05', '1.0', '*OPEN'))
completion.append(('41', '51', '06', '1.0', '*OPEN'))
completion.append(('41', '51', '07', '1.0', '*OPEN'))
completion.append(('41', '51', '08', '1.0', '*OPEN'))
completion.append(('41', '51', '09', '1.0', '*OPEN'))
completion.append(('41', '51', '10', '1.0', '*OPEN'))
completion.append(('41', '51', '11', '1.0', '*OPEN'))
completion.append(('41', '51', '12', '1.0', '*OPEN'))
completion.append(('41', '51', '13', '1.0', '*OPEN'))
completion.append(('41', '51', '14', '1.0', '*CLOSED'))
completion.append(('41', '51', '15', '1.0', '*CLOSED'))
completion.append(('41', '51', '16', '1.0', '*OPEN'))
completion.append(('41', '51', '17', '1.0', '*OPEN'))
completion.append(('41', '51', '18', '1.0', '*OPEN'))
completion.append(('41', '51', '19', '1.0', '*OPEN'))
completion.append(('41', '51', '20', '1.0', '*OPEN'))
completion.append(('41', '51', '21', '1.0', '*OPEN'))
completion.append(('41', '51', '22', '1.0', '*OPEN'))
completion.append(('41', '51', '23', '1.0', '*OPEN'))
completion.append(('41', '51', '24', '1.0', '*OPEN'))
completion.append(('41', '51', '25', '1.0', '*OPEN'))
completion.append(('41', '51', '26', '1.0', '*OPEN'))
completion.append(('41', '51', '27', '1.0', '*OPEN'))
completion.append(('41', '51', '28', '1.0', '*OPEN'))
completion.append(('41', '51', '29', '1.0', '*OPEN'))
completion.append(('41', '51', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('41 51 01:13')
layerclump.append('41 51 16:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('G', 1461.0)

on_time = 0.98

wag_cycle = ('W', 1918.0, 183.0, 100)

icv_nr = None

icv_start = None

icv_control = None
