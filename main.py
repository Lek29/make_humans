import file_operations
from faker import Faker
from random import randint, choice, sample


def main():
    fake = Faker('ru_Ru')

    for num in range(1, 11):
        last_name, first_name, second_name = fake.name_male().split()
        characters_job = fake.job()
        characters_town = fake.city()
        list_random_numbers = [randint(3, 18) for _ in range(5)]
        skills_list = ['Стремительный прыжок',
                       'Электрический выстрел',
                       'Ледяной удар',
                       'Стремительный удар',
                       'Кислотный взгляд',
                       'Тайный побег',
                       'Ледяной выстрел',
                       'Огненный заряд', ]
        dict_mystical_sign = {
            'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
            'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
            'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
            'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
            'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
            'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
            'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
            'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
            'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
            'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
            'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
            'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
            'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
            'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
            'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
            'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
            'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
            'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
            'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
            'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
            'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
            'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
            ' ': ' ',
        }
        list_unidue_skils = sample(skills_list, 3)

        runic_skills = [''.join([sign.replace(sign, dict_mystical_sign[sign])
                                 for sign in world if sign in dict_mystical_sign])
                        for world in list_unidue_skils]

        context = {'first_name': first_name,
                   'last_name': last_name,
                   'job': characters_job,
                   'town': characters_town,
                   'strength': choice(list_random_numbers),
                   'agility': choice(list_random_numbers),
                   'intelligence': choice(list_random_numbers),
                   'luck': choice(list_random_numbers),
                   'endurance': choice(list_random_numbers),
                   'skill_1': runic_skills[0],
                   'skill_2': runic_skills[1],
                   'skill_3': runic_skills[2],
                   }
        file_operations.render_template('images/charsheet.svg', f'out_put_svg/card_for_game_{num}.svg', context)


if __name__ == '__main__':
    main()
