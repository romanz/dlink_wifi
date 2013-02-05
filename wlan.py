#!/usr/bin/env python
import requests

def main(args):
    url = 'http://' + args.url
    
    if args.login:
        user, password = args.login.split(':')
        login = {'ACTION_POST': 'LOGIN', 'FILECODE': '', 'LOGIN_PASSWD': password, 'LOGIN_USER': user, 'VERIFICATION_CODE': '', 'VER_CODE': '', 'login': 'Log In '}
        r = requests.post(url + '/login.php', data=login)
        print 'Login:', r

    if args.on:
        r = requests.post(url + '/bsc_wlan.php', data=_ENABLE)
        print 'Enable:', r
        
    if args.off:
        r = requests.post(url + '/bsc_wlan.php', data=_DISABLE)
        print 'Disable:', r
    
    if args.on or args.off:
        r = requests.get(url + '/bsc_wlan.xgi?exeshell=submit%20COMMIT&exeshell=submit%20WLAN') # Wierd commit request (as shown by Wireshark)
        print 'Save:', r
    
_ENABLE = { 'ACTION_POST': 'final',
 'f_ap_hidden': '0',
 'f_authentication': '0',
 'f_auto_channel': '0',
 'f_channel': '9',
 'f_cipher': '0',
 'f_enable': '1',
 'f_radius_ip1': '',
 'f_radius_port1': '',
 'f_radius_secret1': '',
 'f_ssid': 'nexus',
 'f_txrate': '0',
 'f_wep': '',
 'f_wep_def_key': '',
 'f_wep_format': '',
 'f_wep_len': '',
 'f_wlan_sch': '0',
 'f_wmm_enable': '1',
 'f_wpa_psk': '',
 'f_wpa_psk_type': '',
 'f_wps_enable': '0',
 'f_xr': ''}
 
_DISABLE = {'ACTION_POST': 'final',
 'f_ap_hidden': '',
 'f_authentication': '',
 'f_auto_channel': '',
 'f_channel': '',
 'f_cipher': '',
 'f_enable': '0',
 'f_radius_ip1': '',
 'f_radius_port1': '',
 'f_radius_secret1': '',
 'f_ssid': '',
 'f_super_g': '',
 'f_txrate': '',
 'f_wep': '',
 'f_wep_def_key': '',
 'f_wep_format': '',
 'f_wep_len': '',
 'f_wlan_sch': '',
 'f_wmm_enable': '',
 'f_wpa_psk': '',
 'f_wpa_psk_type': '',
 'f_wps_enable': '',
 'f_xr': ''}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='D-Link DIR-300 WiFi switch')
    parser.add_argument('--url', default='192.168.0.1', help='Router URL')
    parser.add_argument('--login', type=str, help='Login information for the router (username:password)')
    parser.add_argument('--on', action='store_true', help='Enable WiFi')
    parser.add_argument('--off', action='store_true', help='Disable WiFi')
    args = parser.parse_args()
    main(args)
    
