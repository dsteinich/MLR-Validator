
from unittest import TestCase, mock

from ..error_validator import ErrorValidator

@mock.patch('mlrvalidator.validators.error_validator.SingleFieldValidator')
class ErrorValidatorErrorsTestCase(TestCase):

    def test_all_valid(self, msingle_field_class):
        msingle_field = msingle_field_class.return_value

        msingle_field.validate.return_value = True
        msingle_field.errors = {}

        validator = ErrorValidator()
        result = validator.validate({'A' : 'This', 'B' : 'That'}, {})

        self.assertTrue(result)
        self.assertEqual(len(validator.errors), 0)

    def test_single_field_invalid(self, msingle_field_class):
        msingle_field = msingle_field_class.return_value

        msingle_field.validate.return_value = False
        msingle_field.errors = {'A' : ['Invalid']}

        validator = ErrorValidator()
        result = validator.validate({'A': 'This', 'B': 'That'}, {})

        self.assertFalse(result)
        self.assertEqual(len(validator.errors), 1)









