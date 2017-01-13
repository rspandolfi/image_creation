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
        '}\n' + \
        'network={\n' + \
            '\tpriority=2\n' + \
            '\tssid="Frog2"\n' + \
            '\tpsk=74a135a8394c439fcdf0f04f10381dd1bcc1becf07c84ab2836537cbf6bed582\n' + \
            '\tkey_mgmt=WPA-PSK\n' + \
        '}\n' + \
        'network={\n' + \
            '\tpriority=3\n' + \
            '\tssid="Toad"\n' + \
            '\tpsk=d138bdf4841084f97b15bcb80a417f76bf833077d9b6b9040cfc2bc69fcbb683\n' + \
            '\tkey_mgmt=WPA-PSK\n' + \
        '}\n' + \
        'network={\n' + \
            '\tpriority=2\n' + \
            '\tssid="Field_Frog2"\n' + \
            '\tpsk=1552043464bbf9a232ce7dcc18dc8b6f8ef5e890742ac550828589071c8fed68\n' + \
            '\tkey_mgmt=WPA-PSK\n' + \
        '}\n' + \
        'network={\n' + \
            '\tpriority=3\n' + \
            '\tssid="Field_Toad"\n' + \
            '\tpsk=0e8f0c524dc73882c39139e49296cd6c67f3693d1c31c11ec54803c225c98f03\n' + \
            '\tkey_mgmt=WPA-PSK\n' + \
        '}\n')


