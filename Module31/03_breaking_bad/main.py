import requests
import json


def search_episode():
    max_death = serial_info[0]
    for episode in serial_info:
        if episode['number_of_deaths'] > max_death['number_of_deaths']:
            max_death = episode
    return max_death


death_info = requests.get('https://www.breakingbadapi.com/api/deaths')
serial_info = json.loads(death_info.text)

episode = search_episode()


with open('BreakingBad.json', 'w') as file:
    json.dump(episode, file, indent=4)

print('ID эпизода - {id}'
      '\nНомер сезона - {season}'
      '\nНомер эпизода - {episode}'
      '\nОбщее количество смертей - {death}'
      '\nСписок погибших - {death_list}'.format(id=episode['death_id'],
                                                season=episode['season'],
                                                episode=episode['episode'],
                                                death=episode['number_of_deaths'],
                                                death_list=episode['death']))
