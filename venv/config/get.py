import configparser
import  os
def init():
    config=configparser.ConfigParser().read(os.path.join(os.path.dirname(__file__))+'/config.ini',encoding='utf-8')
    print(config.sections())
    value=config.get('bian', 'url')
    print(value)
    pass


if __name__ == '__main__':
    init()