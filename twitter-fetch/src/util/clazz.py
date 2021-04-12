def get_attributes(clazz):
    """Gets the attribbutes of a class"""
    return [attr for attr in clazz.__dataclass_fields__]
