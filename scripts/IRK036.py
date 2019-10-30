completion = []
completion.append(('07', '39', '01', '1.0', '*OPEN'))
completion.append(('07', '39', '02', '1.0', '*OPEN'))
completion.append(('07', '39', '03', '1.0', '*OPEN'))
completion.append(('07', '39', '04', '1.0', '*OPEN'))
completion.append(('07', '39', '05', '1.0', '*OPEN'))
completion.append(('07', '39', '06', '1.0', '*OPEN'))
completion.append(('07', '39', '07', '1.0', '*OPEN'))
completion.append(('07', '39', '08', '1.0', '*OPEN'))
completion.append(('07', '39', '09', '1.0', '*OPEN'))
completion.append(('07', '39', '10', '1.0', '*OPEN'))
completion.append(('07', '39', '11', '1.0', '*OPEN'))
completion.append(('07', '39', '12', '1.0', '*OPEN'))
completion.append(('07', '39', '13', '1.0', '*OPEN'))
completion.append(('07', '39', '14', '1.0', '*OPEN'))
completion.append(('07', '39', '15', '1.0', '*CLOSED'))
completion.append(('07', '39', '16', '1.0', '*CLOSED'))
completion.append(('07', '39', '17', '1.0', '*OPEN'))
completion.append(('07', '39', '18', '1.0', '*OPEN'))
completion.append(('07', '39', '19', '1.0', '*OPEN'))
completion.append(('07', '39', '20', '1.0', '*OPEN'))
completion.append(('07', '39', '21', '1.0', '*OPEN'))
completion.append(('07', '39', '22', '1.0', '*OPEN'))
completion.append(('07', '39', '23', '1.0', '*OPEN'))
completion.append(('07', '39', '24', '1.0', '*OPEN'))
completion.append(('07', '39', '25', '1.0', '*OPEN'))
completion.append(('07', '39', '26', '1.0', '*OPEN'))
completion.append(('07', '39', '27', '1.0', '*OPEN'))
completion.append(('07', '39', '28', '1.0', '*OPEN'))
completion.append(('07', '39', '29', '1.0', '*OPEN'))
completion.append(('07', '39', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('07 39 01:14')
layerclump.append('07 39 17:30')

operate = []
operate.append(('G', '*MAX', '*STG', 3000000.0, '*CONT *REPEAT'))
operate.append(('G', '*MAX', '*BHP',     540.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*STW',    5000.0, '*CONT *REPEAT'))
operate.append(('W', '*MAX', '*BHP',     470.0, '*CONT *REPEAT'))

monitor = []

group = 'INJECTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = ('G', 1584.0)

on_time = 0.98

wag_cycle = ('W', 1918.0, 183.0, 100)

icv_nr = None

icv_start = None

icv_control = None
