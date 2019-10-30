completion = []
completion.append(('31', '06', '01', '1.0', '*OPEN'))
completion.append(('31', '06', '02', '1.0', '*OPEN'))
completion.append(('31', '06', '03', '1.0', '*OPEN'))
completion.append(('31', '06', '04', '1.0', '*OPEN'))
completion.append(('31', '06', '05', '1.0', '*OPEN'))
completion.append(('31', '06', '06', '1.0', '*OPEN'))
completion.append(('31', '06', '07', '1.0', '*OPEN'))
completion.append(('31', '06', '08', '1.0', '*OPEN'))
completion.append(('31', '06', '09', '1.0', '*OPEN'))
completion.append(('31', '06', '10', '1.0', '*OPEN'))
completion.append(('31', '06', '11', '1.0', '*OPEN'))
completion.append(('31', '06', '12', '1.0', '*OPEN'))
completion.append(('31', '06', '13', '1.0', '*OPEN'))
completion.append(('31', '06', '14', '1.0', '*OPEN'))
completion.append(('31', '06', '15', '1.0', '*CLOSED'))
completion.append(('31', '06', '16', '1.0', '*CLOSED'))
completion.append(('31', '06', '17', '1.0', '*OPEN'))
completion.append(('31', '06', '18', '1.0', '*OPEN'))
completion.append(('31', '06', '19', '1.0', '*OPEN'))
completion.append(('31', '06', '20', '1.0', '*OPEN'))
completion.append(('31', '06', '21', '1.0', '*OPEN'))
completion.append(('31', '06', '22', '1.0', '*OPEN'))
completion.append(('31', '06', '23', '1.0', '*OPEN'))
completion.append(('31', '06', '24', '1.0', '*OPEN'))
completion.append(('31', '06', '25', '1.0', '*OPEN'))
completion.append(('31', '06', '26', '1.0', '*OPEN'))
completion.append(('31', '06', '27', '1.0', '*OPEN'))
completion.append(('31', '06', '28', '1.0', '*OPEN'))
completion.append(('31', '06', '29', '1.0', '*OPEN'))
completion.append(('31', '06', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('31 06 01:14')
layerclump.append('31 06 17:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('W', 1734.0)

on_time = 0.98

wag_cycle = ('G', 1918.0, 183.0, 100)

icv_nr = None

icv_start = None

icv_control = None
