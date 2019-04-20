import pyperclip
import re

port_type = {'0000': 'SLT', '000C': 'TRK', '0004': 'DLT'}
status = {'00H': 'IDLE', '02H': 'DIAL_TN', '03H': 'CBK_TN', '04H': 'RGBK_TN',
          '0CH': 'HELD', '0DH': 'RINGING', '0EH': 'CALLBK', '0FH': 'DIALING',
          '10H': 'DIAL_TR', '11H': 'SPEAK', '24H': 'CALLING', '25H': 'GUARD',
          '26H': 'RELEASE', '61H': 'IHELD'}

log_paste = pyperclip.paste()
# we will analyze such lines >>>> PORT:000C0011H  STATUS 000DH => 0011H
rx = re.compile(r'>>>> PORT:(\d\d\d.)\d\d(\d\d)H  STATUS ....H => \d\d(\d\dH)')
rows_found = re.findall(rx, log_paste)
for item in rows_found:
    print('%s %02d - %s' % (port_type[item[0]], int(item[1], 16),
                            status.get(item[2], item[2])))
    # TRK 17 - SPEAK

input()
