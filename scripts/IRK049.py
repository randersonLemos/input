completion = []
completion.append(('35', '40', '01', '1.0', '*OPEN'))
completion.append(('35', '40', '02', '1.0', '*OPEN'))
completion.append(('35', '40', '03', '1.0', '*OPEN'))
completion.append(('35', '40', '04', '1.0', '*OPEN'))
completion.append(('35', '40', '05', '1.0', '*OPEN'))
completion.append(('35', '40', '06', '1.0', '*OPEN'))
completion.append(('35', '40', '07', '1.0', '*OPEN'))
completion.append(('35', '40', '08', '1.0', '*OPEN'))
completion.append(('35', '40', '09', '1.0', '*OPEN'))
completion.append(('35', '40', '10', '1.0', '*OPEN'))
completion.append(('35', '40', '11', '1.0', '*OPEN'))
completion.append(('35', '40', '12', '1.0', '*OPEN'))
completion.append(('35', '40', '13', '1.0', '*OPEN'))
completion.append(('35', '40', '14', '1.0', '*CLOSED'))
completion.append(('35', '40', '15', '1.0', '*CLOSED'))
completion.append(('35', '40', '16', '1.0', '*OPEN'))
completion.append(('35', '40', '17', '1.0', '*OPEN'))
completion.append(('35', '40', '18', '1.0', '*OPEN'))
completion.append(('35', '40', '19', '1.0', '*OPEN'))
completion.append(('35', '40', '20', '1.0', '*OPEN'))
completion.append(('35', '40', '21', '1.0', '*OPEN'))
completion.append(('35', '40', '22', '1.0', '*OPEN'))
completion.append(('35', '40', '23', '1.0', '*OPEN'))
completion.append(('35', '40', '24', '1.0', '*OPEN'))
completion.append(('35', '40', '25', '1.0', '*OPEN'))
completion.append(('35', '40', '26', '1.0', '*OPEN'))
completion.append(('35', '40', '27', '1.0', '*OPEN'))
completion.append(('35', '40', '28', '1.0', '*OPEN'))
completion.append(('35', '40', '29', '1.0', '*OPEN'))
completion.append(('35', '40', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('35 40 01:13')
layerclump.append('35 40 16:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('G', 1522.0)

wag_cycle = ('W', 1918.0, 183.0, 100)

on_time = 0.98

icv_nr = None

icv_start = None

icv_control = None
