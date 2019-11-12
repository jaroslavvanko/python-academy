time = input('Please enter your time: ')

hours, mins = time.split(':')

adjusted_h = hours if int(hours)==12 else str(int(hours) % 12)

daytime = ['AM','PM'][int(hours)>=12]

print('Converted to English: ' + adjusted_h + ':' + mins + ' ' + daytime)