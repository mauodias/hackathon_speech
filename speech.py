import os
import sys
import json
import random
from gtts import gTTS
from time import sleep

BYE = [
        {'text': 'Sayonara', 'lang': 'ja'},
        {'text': 'Tchau', 'lang': 'pt'},
        {'text': 'Au revoir', 'lang': 'fr'},
        {'text': 'Goodbye', 'lang': 'en'},
        {'text': 'Ciao', 'lang': 'it'},
        {'text': 'Auf Wiedersehen', 'lang': 'de'},
        {'text': 'Adiós', 'lang': 'es'},
        {'text': 'Vale', 'lang': 'la'}
        ]

class Speech:

    def __init__(self, text, language):
        try:
            self.tts = gTTS(text=text, lang=language, lang_check=True)
        except ValueError:
            print("Language not recognized. Check this link for a complete list (use the subtag field): https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry")

    def speak(self):
        self.tts.save('audio.mp3')
        os.system('afplay audio.mp3')
        os.remove('audio.mp3')

class TeamMember:
    def __init__(self, full_name, team):
        self.full_name = full_name
        self.team = team

    def __str__(self):
        return f"{self.full_name}: Você está no {self.team}"

class DataStore:
    def __init__(self, json_path):
        obj = json.loads(open(json_path).read())
        self.team_members  = {}
        for time in obj['times']:
            for member in time['membros']:
                m = TeamMember(member['nome_completo'], time['nome'])
                if self.team_members.get(member['primeiro_nome'], None):
                    raise Exception(f'{member["primeiro_nome"]} in {time["nome"]} is repeated')
                self.team_members[member['primeiro_nome']] = m

def cli(members):
    while(True):
        os.system('clear')
        name = input('> ')
        if name.lower() == 'q':
            b = random.choice(BYE)
            s = Speech(text=f'{b["text"]}!', language=f'{b["lang"]}')
            print(f'{b["text"]}!')
            s.speak()
            sys.exit(0)
        tm = members.get(name.lower(), None)
        if tm:
            s = Speech(text=str(tm), language='pt')
            print(str(tm))
            s.speak()
        else:
            s = Speech(text=f'{name}, nome não encontrado.', language='pt')
            print(f'{name}, nome não encontrado.')
            s.speak()
        sleep(2)

if __name__ == '__main__':
    datastore = DataStore('times.json')
    cli(datastore.team_members)
