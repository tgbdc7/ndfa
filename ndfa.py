"""
Program to check when the name day is.
Returns a list of days on which a name day falls for the given name.
Data are taken from API https://api.abalin.net/
"""
try:
    import argparse
    import requests

except ModuleNotFoundError as exception:
    print(f'Ups something goes wrongs: {exception}')
    print(f"Install dependencies. Type: 'pip install -r requirements.txt'")
    exit()


def get_current_namedays(country='pl'):
    try:
        r = requests.get('https://api.abalin.net/today')
        r.encoding = 'utf-8'
        r_data = r.json()
        r_data_filter = r_data['data'][0]['namedays'][country]
        print(r_data_filter)
    except KeyError as e:
        print(f"We don't serve this country: {e}.\nList of supported countries and country codes: "
              f"Austria [at], Germany [de], Spain [es], Greece [gr], Italy [it], Poland [pl], Slovakia [sk], "
              f"Bulgaria [bg], Denmark [dk], Finland [fi], Croatia [hr], Lithuania [lt], Russian Federation [ru], "
              f"United States of America [us], Czechia [cz], Estonia [ee],  France [fr], Hungary [hu], "
              f"Latvia [lv], Sweden [se]")
        exit()
    return r_data_filter


def get_namedays_list(name_to_check, country='pl'):
    try:
        parameters = {'country': country, 'name': name_to_check}
        r = requests.get('https://api.abalin.net/getdate?', params=parameters)
        r.encoding = 'utf-8'
        r_data = r.json()
        r_data_filter = []
        for item in (r_data['results']):
            day = item['day']
            month = item['month']
            r_data_filter.append((day, month))
        print(r_data_filter)
        return r_data_filter
    except KeyError as e:
        print(f"Ups something goes wrongs: We don't have {e} for {name_to_check}. Please provide a valid name!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program to check when the name-days is.\n'
                                                 'Returns a list of days on which a name day falls for the given name.')
    parser.add_argument('name', nargs='?',
                        help="The name for which we want to check when the name day is. "
                             "If you don't give this argument, it returns a list of names that are celebrating today. "
                             "If name is not correct or is not in the database, it returns an empty list")
    parser.add_argument("-c", '--country',
                        choices=['cz', 'sk', 'pl', 'fr', 'hu', 'hr', 'se', 'us', 'at', 'it', 'es', 'de', 'dk', 'fi',
                                 'bg', 'lt', 'ee', 'lv', 'gr', 'ru'], default='pl',
                        help="Choose which country you want to check"
                             "Default is 'pl'"
                             "List of supported countries and country codes: "
                             f"Austria [at], Germany [de], Spain [es], Greece [gr], Italy [it], Poland [pl],"
                             f" Slovakia [sk], Bulgaria [bg], Denmark [dk], Finland [fi], Croatia [hr], "
                             f"Lithuania [lt], Russian Federation [ru], United States of America [us], Czechia [cz], "
                             f"Estonia [ee],  France [fr], Hungary [hu], Latvia [lv], Sweden [se]"
                        )

    args = parser.parse_args()
    name = args.name
    country = args.country
    if name:
        get_namedays_list(name, country)
    else:
        get_current_namedays(country)
