from base import BaseHandler


class FoodHandler(BaseHandler):
    """
    Given a person_id, return that person's details along with their favourite fruit and veg!
    """

    def get(self):
        person_id = self.get_argument('person_id')

        person = self.people_collection.find_one({'_id': person_id}, {'favourite_fruit': True,
                                                                      'favourite_veg': True,
                                                                      'name': True,
                                                                      'age': True})

        # Handle people not found
        if not person:
            self.respond(error="ERR_NO_PEOPLE", message="No people found with supplied ID")
        else:
            self.respond(people=person)
