
from cerberus import Validator
from cerberus import schema_registry

schema = {'field1': {'required': False}, 'field2': {'required': False, 'dependencies': 'field1'}}
document = {'field1': 7}


v = Validator()
v.validate(document, schema)

# schema dict
schema = {'a_dict': {'type': 'dict', 'schema': {'address': {'type': 'string'},
                                                'city': {'type': 'string', 'required': True}}}}

document = {'a_dict': {'address': 'my address', 'city': 'my town'}}
print(v.validate(document, schema))

# schema list
schema = {'a_list': {'type': 'list', 'schema': {'type': 'integer'}}}
document = {'a_list': [3, 4, 5]}
print(v.validate(document, schema))

schema_registry.add('non-system user',
                    {'uid': {'min': 1000, 'max': 0xffff}})
schema = {'sender': {'schema': 'non-system user',
                     'allow_unknown': True},
          'receiver': {'schema': 'non-system user',
                       'allow_unknown': True}}
document = {'sender':{'uid':20000, 'allow_unknown': True}}
print(v.validate(document, schema))


# nomorlizer
class MyNormalizer(Validator):
    def __init__(self, multiplier, *args, **kwargs):
        super(MyNormalizer, self).__init__(*args, **kwargs)
        self.multiplier = multiplier

    def _normalize_coerce_multiply(self, value):
        return value * self.multiplier
    
    def _normalize_coerce_div(self, value):
        return value / self.multiplier
    


schema = {'foo': {'coerce': 'multiply'}}
document = {'foo': 2}
print(MyNormalizer(multiplier=3).normalized(document, schema))

schema = {'foo': {'coerce': 'div'}}
document = {'foo': 2}
print(MyNormalizer(multiplier=3).normalized(document, schema))

# check with
class MyValidator(Validator):
    def _check_with_oddity(self, field, value):
        if not value & 1:
            self._error(field, "Must be an odd number")

schema = {'amount': {'type': 'integer', 'check_with': 'oddity'}}
document = {'amount':2}
v= MyValidator()
print(v.validate(document, schema))


class MyValidator1(Validator):
    def _validate_is_odd(self, constraint, field, value):
        """ Test the oddity of a value.

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if constraint is True and not bool(value & 1):
            self._error(field, "Must be an odd number")
schema = {'amount': {'is odd': True, 'type': 'integer'}}
v = MyValidator1(schema)
print(v.validate({'amount': 10}))