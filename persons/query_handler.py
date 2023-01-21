from database import Person


class QueryHandler:

    @staticmethod
    def get_all_persons():
        return Person.select()

    def get_all_elements(self):
        persons = self.get_all_persons().dicts()
        return [person for person in persons]

    def get_person_elements(self, person_id):
        all_elements = self.get_all_elements()
        return [person for person in all_elements if person['id'] == person_id]
