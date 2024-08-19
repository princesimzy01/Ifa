from Knowledge_base import OduIfa
import sqlite3

def get_all_odu_ifa():
    conn = sqlite3.connect('ifa_divination.db')
    c = conn.cursor()

    # Retrieve all Odu Ifa data
    c.execute('SELECT odu_name, verses, meanings, advice, keys FROM odu_ifa')
    odu_ifa_list = c.fetchall()

    conn.close()

    # Convert data to OduIfa objects
    return [OduIfa(odu_name, verses.split('\n'), meanings.split('\n'), advice.split('\n'), keys.split('\n'))  for odu_name, verses, meanings, advice, keys in odu_ifa_list]


def get_odu_ifa_by_name(odu_name: str):
    conn = sqlite3.connect('ifa_divination.db')
    c = conn.cursor()

    # Retrieve Odu Ifa data by name
    c.execute('SELECT odu_name, verses, meanings, advice, keys FROM odu_ifa WHERE odu_name = ?', (odu_name,))
    result = c.fetchone()

    conn.close()

    if result:
        return OduIfa(result[0], result[1].split('\n'), result[2].split('\n'), result[3].split('\n'))
    else:
        return None


all_odu_ifa = get_all_odu_ifa()

