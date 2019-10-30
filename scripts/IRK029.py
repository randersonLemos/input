completion = []
completion.append(('07', '34', '01', '1.0', '*OPEN'))
completion.append(('07', '34', '02', '1.0', '*OPEN'))
completion.append(('07', '34', '03', '1.0', '*OPEN'))
completion.append(('07', '34', '04', '1.0', '*OPEN'))
completion.append(('07', '34', '05', '1.0', '*OPEN'))
completion.append(('07', '34', '06', '1.0', '*OPEN'))
completion.append(('07', '34', '07', '1.0', '*OPEN'))
completion.append(('07', '34', '08', '1.0', '*OPEN'))
completion.append(('07', '34', '09', '1.0', '*OPEN'))
completion.append(('07', '34', '10', '1.0', '*OPEN'))
completion.append(('07', '34', '11', '1.0', '*OPEN'))
completion.append(('07', '34', '12', '1.0', '*OPEN'))
completion.append(('07', '34', '13', '1.0', '*OPEN'))
completion.append(('07', '34', '14', '1.0', '*OPEN'))
completion.append(('07', '34', '15', '1.0', '*OPEN'))
completion.append(('07', '34', '16', '1.0', '*CLOSED'))
completion.append(('07', '34', '17', '1.0', '*CLOSED'))
completion.append(('07', '34', '18', '1.0', '*OPEN'))
completion.append(('07', '34', '19', '1.0', '*OPEN'))
completion.append(('07', '34', '20', '1.0', '*OPEN'))
completion.append(('07', '34', '21', '1.0', '*OPEN'))
completion.append(('07', '34', '22', '1.0', '*OPEN'))
completion.append(('07', '34', '23', '1.0', '*OPEN'))
completion.append(('07', '34', '24', '1.0', '*OPEN'))
completion.append(('07', '34', '25', '1.0', '*OPEN'))
completion.append(('07', '34', '26', '1.0', '*OPEN'))
completion.append(('07', '34', '27', '1.0', '*OPEN'))
completion.append(('07', '34', '28', '1.0', '*OPEN'))
completion.append(('07', '34', '29', '1.0', '*OPEN'))
completion.append(('07', '34', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('07 34 01:15')
layerclump.append('07 34 18:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('W', 1400.0)

on_time = 0.98

wag_cycle = ('G', 1918.0, 183.0, 100)

icv_nr = None

icv_start = None

icv_control = None
