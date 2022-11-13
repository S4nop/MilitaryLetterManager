from configparser import ConfigParser

from utils.crypto_utils import encrypt, decrypt


class ConfigHelper:
    @staticmethod
    def create_config_file():
        ConfigHelper.unset_auto_login()

    @staticmethod
    def set_auto_login(id_, password):
        encrypted_pw = encrypt(password)
        config = ConfigParser()
        config.read('config.ini')
        config['AUTOLOGIN'] = {'auto_login': 'True', 'id': id_, 'password': encrypted_pw}
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
            decrypted_pw = decrypt(config['AUTOLOGIN']['password'])
            return True, config['AUTOLOGIN']['id'], decrypted_pw
        else:
            return False, None, None
