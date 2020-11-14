from app import ma


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'company', 'description', 'qrcode')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class MonitorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'start_date', 'end_date')


monitor_schema = MonitorSchema()
monitors_schema = MonitorSchema(many=True)


class MonitorProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number', 'product_id', 'monitor_id')


monitor_product_schema = MonitorProductSchema()
monitors_products_schema = MonitorProductSchema(many=True)
