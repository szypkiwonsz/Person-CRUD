import click

from database import DatabaseHandler
from query_handler import QueryHandler


@click.group()
def cli():
    pass


@cli.command()
def start_program():
    while True:
        temp_query_handler = QueryHandler()
        temp_database_handler = DatabaseHandler()
        option = input('Wybierz opcję co chcesz wykonać... 1 - dodać osobę, 2 - wyświetlić dane osób, '
                       '3 - edytować użytkownika, 4 - usunąć użytkownika, 0 - wyjść z programu: ')
        if int(option) == 1:
            first_name = input('Podaj imię: ')
            last_name = input('Podaj nazwisko: ')
            age = input('Podaj wiek: ')
            sex = input('Podaj płeć: ')
            temp_database_handler = DatabaseHandler()
            temp_database_handler.insert_data_into_person(
                [{'first_name': first_name, 'last_name': last_name, 'age': age,
                  'sex': sex}])
            print(f'Użytkownik {first_name} został poprawnie stworzony.')
        elif int(option) == 2:
            temp_query_handler = QueryHandler()
            print(temp_query_handler.get_all_elements())
        elif int(option) == 3:
            person_id = input('Podaj ID użytkownika do aktualizacji danych: ')
            person_elements = temp_query_handler.get_person_elements(int(person_id))
            if not person_elements:
                print(f'Brak użytkownika o ID: {person_id}.')
                continue
            else:
                person_elements = person_elements[0]
            choice = input(
                'Wybierz jakie dane chcesz zmienić... 1 - imię, 2 - nazwisko, 3 - wiek, 4 - płeć, 5 - wszystko: '
                '')
            if int(choice) == 1:
                new_first_name = input('Podaj nowe imię użytkownika: ')
                temp_database_handler.update_person(first_name=new_first_name, last_name=person_elements['last_name'],
                                                    age=person_elements['age'], sex=person_elements['sex'],
                                                    person_id=person_id)
                print(
                    f'Poprawnie zaaktualizowano imię {person_elements["first_name"]} na {new_first_name} dla '
                    f'użytkownika o ID: {person_id}')
            elif int(choice) == 2:
                new_last_name = input('Podaj nowe nazwisko użytkownika: ')
                temp_database_handler.update_person(first_name=person_elements['first_name'], last_name=new_last_name,
                                                    age=person_elements['age'], sex=person_elements['sex'],
                                                    person_id=person_id)
                print(f'Poprawnie zaaktualizowano nazwisko {person_elements["last_name"]} na {new_last_name} dla '
                      f'użytkownika o ID: {person_id}')
            elif int(choice) == 3:
                new_age = input('Podaj nowy wiek użytkownika: ')
                temp_database_handler.update_person(first_name=person_elements['first_name'],
                                                    last_name=person_elements['last_name'],
                                                    age=new_age, sex=person_elements['sex'],
                                                    person_id=person_id)
                print(f'Poprawnie zaaktualizowano wiek {person_elements["age"]} na {new_age} dla użytkownika o ID: '
                      f'{person_id}')
            elif int(choice) == 4:
                new_sex = input('Podaj nową płeć użytkownika: ')
                temp_database_handler.update_person(first_name=person_elements['first_name'],
                                                    last_name=person_elements['last_name'],
                                                    age=person_elements['age'], sex=new_sex,
                                                    person_id=person_id)
                print(f'Poprawnie zaaktualizowano płeć {person_elements["sex"]} na {new_sex} dla użytkownika o ID: '
                      f'{person_id}')
            elif int(choice) == 5:
                new_first_name = input('Podaj nowe imię użytkownika: ')
                new_last_name = input('Podaj nowe nazwisko użytkownika: ')
                new_age = input('Podaj nowy wiek użytkownika: ')
                new_sex = input('Podaj nową płeć użytkownika: ')
                temp_database_handler.update_person(first_name=new_first_name, last_name=new_last_name, age=new_age,
                                                    sex=new_sex, person_id=person_id)
                print(f'Poprawnie zaaktualizowano dane dla użytkownika o ID: {person_id}')
            else:
                print('Brak takiej opcji.')
        elif int(option) == 4:
            person_id = input('Podaj ID użytkownika do usunięcia danych: ')
            person_elements = temp_query_handler.get_person_elements(int(person_id))
            if not person_elements:
                print(f'Brak użytkownika o ID: {person_id}.')
                continue
            temp_database_handler.delete_person(person_id)
            print(f'Poprawnie usunięto użytkownika o ID: {person_id}')
        elif int(option) == 0:
            break
        else:
            print('Brak takiej opcji.')


if __name__ == '__main__':
    cli()
