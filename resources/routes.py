from resources.Product import ProductApi, ProductDetailsApi
from resources.Monitor import MonitorApi, MonitorDetailsApi, MonitorStop
from resources.MonitorProduct import MonitorProductApi, MonitorProductDetailsApi


def initialize_routes(api):
    api.add_resource(ProductApi, '/api/smart_counting/product')
    api.add_resource(ProductDetailsApi, '/api/smart_counting/product/<id>')
    api.add_resource(MonitorApi, '/api/smart_counting/monitor')
    api.add_resource(MonitorDetailsApi, '/api/smart_counting/monitor/<id>')
    api.add_resource(MonitorStop, '/api/smart_counting/monitor_stop/<id>')
    api.add_resource(MonitorProductApi, '/api/smart_counting/monitor_product')
    api.add_resource(MonitorProductDetailsApi, '/api/smart_counting/monitor_product/<id>')
