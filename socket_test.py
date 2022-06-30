import socket
import json
import struct


class SmartPowerStrip(object):

    def __init__(self, ip, device_id=None, timeout=30.0, protocol='tcp'):
        self.ip = ip
        self.port = 9999
        self.protocol = protocol
        self.device_id = device_id
        self.sys_info = None
        self.timeout = timeout

        # if the device ID isn't supplied it needs to be queried from
        # the device before any commands can be sent
        if not self.device_id:
            sys_info = self.get_system_info()
            self.sys_info = sys_info['system']['get_sysinfo']
            self.device_id = self.sys_info['deviceId']

    def set_wifi_credentials(self, ssid, psk, key_type='3'):
        '''
        :param ssid: router ssid
        :param psk: router passkey
        :param key_type: 3 is WPA2, 2 might be WPA and 1 might be WEP?
        :return: command response
        '''

        wifi_command = '{"netif":{"set_stainfo":{"ssid":"' + ssid + '","password":"' + \
                       psk + '","key_type":' + key_type + '}}}'

        return self.send_command(wifi_command, self.protocol)

    def set_cloud_server_url(self, server_url=''):

        server_command = '{"cnCloud":{"set_server_url":{"server":"' + server_url + '"}}}'

        return self.send_command(server_command, self.protocol)

    def get_system_info(self):

        return self._udp_send_command('{"system":{"get_sysinfo":{}}}')

    # manually send a command
    def send_command(self, command, protocol='tcp'):

        if protocol == 'tcp':
            return self._tcp_send_command(command)
        elif protocol == 'udp':
            return self._udp_send_command(command)
        else:
            raise ValueError("Protocol must be 'tcp' or 'udp'")

    def _get_plug_state_int(self, state, reverse=False):

        if state.lower() == 'on':
            if reverse:
                state_int = 0
            else:
                state_int = 1
        elif state.lower() == 'off':
            if reverse:
                state_int = 1
            else:
                state_int = 0
        else:
            raise ValueError("Invalid state, must be 'on' or 'off'")

        return state_int

    # create a string with a list of plug_ids that can be inserted directly into a command
    def _get_plug_id_list_str(self, plug_num_list=None, plug_name_list=None):

        plug_id_list = []

        if plug_num_list:
            for plug_num in plug_num_list:

                # add as str to remove the leading u
                plug_id_list.append(str(self._get_plug_id(plug_num=plug_num)))

        elif plug_name_list:

            for plug_name in plug_name_list:
                # add as str to remove the leading u
                plug_id_list.append(str(self._get_plug_id(plug_name=plug_name)))

        # convert to double quotes and turn the whole list into a string
        plug_id_list_str = str(plug_id_list).replace("'", '"')

        return plug_id_list_str

    # get the plug child_id to be used with commands
    def _get_plug_id(self, plug_num=None, plug_name=None):

        if plug_num and self.device_id:
            plug_id = self.device_id + str(plug_num-1).zfill(2)

        elif plug_name and self.sys_info:
            target_plug = [plug for plug in self.sys_info['children'] if plug['alias'] == plug_name]
            if target_plug:
                plug_id = self.device_id + target_plug[0]['id']
            else:
                raise ValueError('Unable to find plug with name ' + plug_name)
        else:
            raise ValueError('Unable to find plug.  Provide a valid plug_num or plug_name')

        return plug_id

    def _tcp_send_command(self, command):

        sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_tcp.settimeout(self.timeout)
        sock_tcp.connect((self.ip, self.port))

        sock_tcp.send(self._encrypt_command(command))

        data = sock_tcp.recv(2048)
        sock_tcp.close()

        # the first 4 chars are the length of the command so can be excluded
        return json.loads(self._decrypt_command(data[4:]))

    def _udp_send_command(self, command):

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(self.timeout)

        addr = (self.ip, self.port)

        #client_socket.sendto(self._encrypt_command(command, prepend_length=False), addr)
        client_socket.sendto(self._encrypt_command(command, prepend_length=False), addr)

        data, server = client_socket.recvfrom(1024)

        return json.loads(self._decrypt_command(data))

    @staticmethod
    def _encrypt_command(string, prepend_length=True):

        """Encrypts the command to send to the device"""
        key = 171
        result = b''

        #
        # when sending get_sysinfo using udp the length of the command is not needed but
        # with all other commands using tcp it is
        #
        if (prepend_length):
            result = b'\0\0\0' + bytes([len(string)])

        for i in string.encode('utf-8'):
            item = key ^ i
            key = item
            result += bytes([item])

        return result

    @staticmethod
    def _decrypt_command(string):

        """Decrypts the response from the device"""
        key = 171
        result = b''
        for i in bytes(string):
            item = key ^ i
            key = i
            result += bytes([item])

        return result.decode('utf-8')

print('Make sure the HS300 is in set-up mode (blinking orange and green),\n\
and connect your computer to wifi SSID starting with \"TP-LINK_Power Strip\"\n')
#raw_input('Hit Enter to continue: ')

ip_address = "192.168.0.1"

power_strip = SmartPowerStrip(ip_address)

# Turn off cloud communication
power_strip.set_cloud_server_url(server_url='')

# Get MAC address
mac = power_strip.get_system_info()['system']['get_sysinfo']['mac']

print('The MAC address of your HS300 is: ' + mac)
print('Connecting the HS300 to RokuPlayer wifi...')
power_strip.set_wifi_credentials('RokuPlayer', 'ahovwxy@.0', key_type='3')

print('Device should be rebooting and will connect to RokuPlayer wifi shortly.')