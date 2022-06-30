import json

class powerstrip(object):
    def get_system_info(self):
        return json.loads('{"system":{"get_sysinfo":{"mac":1}}}')
ps = powerstrip()
mac = ps.get_system_info()['system']['get_sysinfo']
print(mac)