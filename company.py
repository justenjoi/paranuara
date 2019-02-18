from base import BaseHandler


class CompanyHandler(BaseHandler):
    """
    Given a company_id/index or company name, find all employees that belong to that company
    """
    def get(self):
        company_name = self.get_argument('company_name', default=None)
        company_id = self.get_argument('company_id', default=None)

        # If the company_id isn't supplied, we can find it by looking up by company name
        if not company_id:
            company_doc = self.companies_collection.find_one({'company': company_name.upper()})
            company_id = company_doc.get('index')

        people_list = []
        for people in self.people_collection.find({'company_id': int(company_id)}):
            people_list.append(people)

        # Handle no employees
        if not people_list:
            self.respond(error="ERR_NO_EMPLOYEES", message="No employees found for company")
        else:
            self.respond(employees=people_list, employee_count=len(people_list))
