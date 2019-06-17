# 声明：
### 本项目为自学过程中的练手项目，不具有实际使用价值。
# 项目说明：
### 2.在info_collection.py文件收集Mac信息的代码中：
    @staticmethod
    # mac平台
    def darwin():
        from plugins.collect_mac_info import mac_collect
        return mac_collect()
    # 函数名不要写成mac，要根据自己电脑的实际系统填写，不然会报错。
### 3.本项目是在Mac下完成，没有测试Windows的数据。如果是在win下开发，需要安装：
    pip3.5 install wmi
    pip3.5 install pypiwin32
    或者手动下载安装包安装。
    
### 4.在handler.py文件中定义了两个方法，一个用来测试，一个用来实际的发送数据，使用方法：（进入到Client/bin/）
    python3.5 main.py report_data
    or
    python3.5 main.py collect_data

### 5.启动运行项目：
    1.本项目使用的是Django2版本
    2.makemigrations
    3.migrate
    4.创建一个admin管理用户
