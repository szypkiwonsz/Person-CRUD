from peewee import SqliteDatabase, Model, chunked, TextField


class DatabaseHandler:
    db = SqliteDatabase('database.db', pragmas={
        'journal_mode': 'wal',
        'synchronous': 0,
    })

    def __init__(self):
        self.create_table(Person)

    @staticmethod
    def create_table(table_class):
        table_class.create_table()

    def insert_data_into_person(self, data):
        self.insert_data(data, Person)

    def insert_data(self, data, table_class):
        with self.db.atomic():
            for batch in chunked(data, 10):
                table_class.insert_many(batch).execute()

    @staticmethod
    def update_person(first_name, last_name, age, sex, person_id):
        query = Person.update(first_name=first_name, last_name=last_name, age=age, sex=sex).where(
            Person.id == person_id)
        query.execute()

    @staticmethod
    def delete_person(person_id):
        query = Person.delete().where(Person.id == person_id)
        query.execute()


class Person(Model):
    first_name = TextField()
    last_name = TextField()
    age = TextField()
    sex = TextField()

    class Meta:
        database = DatabaseHandler.db
