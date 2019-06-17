import os
import platform
import psutil
import subprocess


# 收集mac系统信息
def mac_collect():
    # 序列号——>sn
    Serial_Number = os.popen(
        'system_profiler SPHardwareDataType | fgrep "Serial" | awk "{print $NF}"').read().strip()
    Serial_Number = Serial_Number.split(":")[1]

    # 产品名称
    Product_Name = os.popen('system_profiler SPHardwareDataType | fgrep "Model Name"').read().strip()
    Product_Name = Product_Name.split(":")[1]

    # 生产商
    Manufacturer = "苹果公司"

    Wake_up_type = ""

    # UUID
    UUID = os.popen('system_profiler SPHardwareDataType | fgrep "Hardware UUID"').read().strip()
    UUID = UUID.split(":")[1]

    data = dict()
    data['asset_type'] = 'server'
    data['manufacturer'] = Manufacturer
    data['sn'] = Serial_Number
    data['model'] = Product_Name
    data['uuid'] = UUID
    data['wake_up_type'] = Wake_up_type

    data.update(get_os_info())
    data.update(get_cpu_info())
    data.update(get_disk_info())
    data.update(get_nic_info())
    data.update(get_ram_info())

    return data


# 获取系统信息
def get_os_info():
    distributor = platform.version()
    os_release = platform.release()
    os_type = platform.system()
    data_dic = {
        "os_distribution": distributor,
        "os_release": os_release,
        "os_type": os_type,
    }
    return data_dic


# 获取CPU
def get_cpu_info():
    cpu_count = psutil.cpu_count()
    cpu_core_count = os.popen('system_profiler SPHardwareDataType | fgrep "Total Number of Cores"').read().strip()
    cpu_core_count = cpu_core_count.split(":")[1]
    cpu_model = os.popen('system_profiler SPHardwareDataType | fgrep "Processor Name"').read().strip()
    cpu_model = cpu_model.split(":")[1]

    data = {
        "cpu_count": cpu_count,
        "cpu_core_count": cpu_core_count,
        "cpu_model": cpu_model,
    }

    return data


# 获取内存
def get_ram_info():
    total = float(psutil.virtual_memory().total) / pow(1024, 3)
    used = round(float(psutil.virtual_memory().used) / pow(1024, 3), 2)
    available = round(float(psutil.virtual_memory().available) / pow(1024, 3), 2)

    ram_data = {
        "total_ram": total,
        "used_ram": used,
        "available_ram": available
    }

    return ram_data


# 获取硬盘
def get_disk_info():
    total_disk = round(float(psutil.disk_usage('/').total) / pow(1024, 3), 3)
    used_disk = round(float(psutil.disk_usage('/').used) / pow(1024, 3), 3)
    free_disk = round(float(psutil.disk_usage('/').free) / pow(1024, 3), 3)
    used_percent = psutil.disk_usage('/').percent

    disk_data = {
        "total_disk": total_disk,
        'used_disk': used_disk,
        'free_disk': free_disk,
        'used_percent': used_percent

    }
    return disk_data


# 获取网卡
# 假数据
def get_nic_info():
    nic_data = {'nic': [{
        'network': '0.0.0.0',
        'net_mask': '255.255.0.0',
        'ip_address': '172.17.42.1',
        'bonding': 0,
        'mac': '56:84:7A:FE:97:99',
        'name': 'docker0',
        'model': 'unknown'
    }, {
        'network': None,
        'net_mask': None,
        'ip_address': None,
        'bonding': 0,
        'mac': '08:94:EF:1B:C9:8F',
        'name': 'eth0',
        'model': 'unknown'
    }, {
        'network': None,
        'net_mask': None,
        'ip_address': None,
        'bonding': 0,
        'mac': '0A:94:EF:1B:C9:96',
        'name': 'usb0',
        'model': 'unknown'
    }, {
        'network': None,
        'net_mask': None,
        'ip_address': None,
        'bonding': 0,
        'mac': '08:94:EF:1B:C9:92',
        'name': 'eth3',
        'model': 'unknown'
    }, {
        'network': None,
        'net_mask': None,
        'ip_address': None,
        'bonding': 0,
        'mac': '08:94:EF:1B:C9:91',
        'name': 'eth2',
        'model': 'unknown'
    }, {
        'network': '60.190.223.255',
        'net_mask': '255.255.255.0',
        'ip_address': '60.190.223.145',
        'bonding': 0,
        'mac': '08:94:EF:1B:C9:90',
        'name': 'eth1',
        'model': 'unknown'
    }]}
    return nic_data


# 测试数据
if __name__ == '__main__':
    data = mac_collect()
    print(data)
