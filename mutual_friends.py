from base import BaseHandler


class MutualFriendsHandler(BaseHandler):
    """
    Given a string of people ID's separated by '|', find their mutual friends that are;
    - Alive
    - Have brown eyes
    """

    def get(self):
        people = self.get_argument('people_ids')

        people_ids = people.split('|')

        # Could allow users to specify which fields to return via a request param rather than have this hard-coded
        people_docs = self.people_collection.find({'_id': {'$in': people_ids}},
                                                  {'name': True, 'address': True, 'age': True, 'phone': True,
                                                   'friends': True})

        people = [p for p in people_docs]
        if not people:
            self.respond(error="ERR_NO_PEOPLE", message="No people found with supplied IDs")
            return

        friends_lists = []
        # Not sure I'm a big fan of this, maybe when setting up the data, seeing as we're not using array index lookups,
        # I could change friends list to a list of GUIDs?
        for pd in people:
            friends_lists.append([friend.get('index') for friend in pd.get('friends', [])])

        mutual_friends = list(set.intersection(*map(set, friends_lists)))

        mutual_friend_docs = self.people_collection.find({'eyeColor': 'brown',
                                                          'has_died': False,
                                                          'index': {'$in': mutual_friends}}, {'name': 1})

        self.respond(people=self.filter_people_for_request(people, view='basic'),
                     mutual_friends=[mf for mf in mutual_friend_docs])
