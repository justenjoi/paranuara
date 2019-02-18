from tornado.options import define
import localsettings


def define_options():
    define('port', default=getattr(localsettings, 'PORT'), help='Server port')
    define('server', default=getattr(localsettings, 'SERVER'), help='Server port')
    define('debug', default=getattr(localsettings, 'DEBUG'), help='Tornado debug mode')

    define('database', default=getattr(localsettings, 'DATABASE'), help='MongoDB database name')
    define('mongo_server', default=getattr(localsettings, 'MONGO_SERVER'), help='MongoDB database server')
    define('mongo_port', default=getattr(localsettings, 'MONGO_PORT'), help='MongoDB database port')
