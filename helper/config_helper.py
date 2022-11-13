from configparser import ConfigParser


class ConfigHelper:
    @staticmethod
    def create_config_file():
        ConfigHelper.unset_auto_login()

    @staticmethod
    def set_auto_login(id_, password):
        config = ConfigParser()
        config.read('config.ini')
        config['AUTOLOGIN'] = {'auto_login': 'True', 'id': id_, 'password': password}
        config.write(open('config.ini', 'w'))

    @staticmethod
    def unset_auto_login():
        config = ConfigParser()
        config['AUTOLOGIN'] = {'auto_login': 'False'}
        config.write(open('config.ini', 'w'))

    @staticmethod
    def get_auto_login_info():
        config = ConfigParser()
        config.read('config.ini')
        if config['AUTOLOGIN']['auto_login'] == 'True':
            return True, config['AUTOLOGIN']['id'], config['AUTOLOGIN']['password']
        else:
            return False, None, None
