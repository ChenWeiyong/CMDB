import sys
import platform


# 自动识别当前系统，并执行相应行法
class InfoCollection(object):

    def collect(self):
        try:
            func = getattr(self, platform.system().lower())
            info_data = func()
            formated_data = self.build_report_data(info_data)
            return formated_data
        except AttributeError as e:
            sys.exit("不支持当前操作系统： [%s]! " % platform.system())

    @staticmethod
    def linux():
        from plugins.collect_linux_info import lin_collect
        return lin_collect()

    @staticmethod
    def windows():
        from plugins.collect_windows_info import Win32Info
        return Win32Info.collect()

    @staticmethod
    # mac平台
    def darwin():
        from plugins.collect_mac_info import mac_collect
        return mac_collect()

    @staticmethod
    def build_report_data(data):
        pass
        return data
