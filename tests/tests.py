import json
import main

from tornado.testing import AsyncHTTPTestCase


class TestParanuara(AsyncHTTPTestCase):
    def get_app(self):
        return main.make_app()

    def test_company(self):
        response = self.fetch('/v1/company/employees?company_id=41')
        self.assertEqual(response.code, 200)

        body = json.loads(response.body)

        self.assertIn('employees', body)
        self.assertIn('employee_count', body)

    def test_company_with_no_employees(self):
        response = self.fetch('/v1/company/employees?company_id=0')
        self.assertEqual(response.code, 200)

        body = json.loads(response.body)

        self.assertIn('error', body.get('meta'))
        self.assertIn('message', body.get('meta'))

        self.assertEqual(body.get('meta', {}).get('message'), 'No employees found for company')

    def test_mutual_friends(self):
        response = self.fetch('/v1/people/mutual_friends?people_ids=595eeb9b96d80a5bc7afb106|595eeb9bfa3a6e19be68df9e')
        self.assertEqual(response.code, 200)

        body = json.loads(response.body)

        self.assertIn('people', body)
        self.assertIn('mutual_friends', body)

    def test_food(self):
        response = self.fetch('/v1/people/food?person_id=595eeb9bfa3a6e19be68df9e')
        self.assertEqual(response.code, 200)

        body = json.loads(response.body)

        self.assertIn('people', body)

        person = body.get('people', {})
        self.assertIn('favourite_fruit', person)
        self.assertIn('favourite_veg', person)
