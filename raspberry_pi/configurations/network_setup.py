import sys
import fileinput

drone = sys.argv[1]
if not isinstance(drone, str):
    print "ERROR: Invalid drone name!"
    quit()

for line in fileinput.input('/etc/hostname', inplace=True):
    sys.stdout.write(drone)

for line in fileinput.input('/etc/hosts', inplace=True):
    if str.startswith(line.strip(), '127.0.1.1'):
        sys.stdout.write('127.0.1.1\t'+drone)
    else:
        sys.stdout.write(line)

with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as wpa:
    wpa.write(
        'network={\n' + \
            '\tpriority=1\n' + \
            '\tssid="Frog"\n' + \
            '\tpsk=ce351656a00bd9f9de28b309821f4190b2625f2b43f6eba1c7a5738e62ece227\n' + \
            '\tkey_mgmt=WPA-PSK\n' + \
        '}\n')


