"""
Program to check when the name day is.
Returns a list of days on which a name day falls for the given name.
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


# def get_nameday_list(name_to_check):
#     """
#     :param name_to_check: Polish name or None
#     :return:  A list of days on which a name day falls for the given name.
#             When 'name_to_check' is None than it returns a list of names that are celebrating today.
#             When 'name_to_check'  is not correct or is not in the database, it returns an empty list.
#     """
#     try:
#         if name_to_check:
#             r = requests.post("http://www.kalendarzswiat.pl/imieniny/", data={'name': name_to_check})
#             r.encoding = 'utf-8'
#             tree = html.fromstring(r.text)
#             data = tree.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/ul/li/text()')
#
#         else:
#             r = requests.get("http://www.kalendarzswiat.pl/imieniny/")
#             r.encoding = 'utf-8'
#             tree = html.fromstring(r.text)
#             data = tree.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/p[3]/b/text()')
#
#     except Exception as exception:
#         print(f'Ups something goes wrongs: {exception}')
#         exit()
#
#     return data
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program to check when the name-days is.\n'
                                                 'Returns a list of days on which a name day falls for the given name.')
    parser.add_argument('name', nargs='?',
                        help="The name for which we want to check when the name day is. "
                             "If you don't give this argument, it returns a list of names that are celebrating today. "
                             "If name is not correct or is not in the database, it returns an empty list")
    args = parser.parse_args()
    name = args.name
    get_current_namedays()

