# Программа генерирует состав команды и карту для тренировки

# Немного поправил вывод

import random
import os
import json

class Generator():
    def __init__(self,
                 p_in_t = 2,        # число игроков в команде
                 #players ={},    # список игроков
                 #maps = {}        # список карт
                 ):
        #self.p_in_t = p_in_t
        #self.players = players
        #self.maps = maps
        global maps
        load()
        self.hystory = {} # история команд
        self.plent = ['A','B'] # пленты
        self.path = ['только Лонг',
                     'только Шорт',
                     'только Мид',
                     'Лонг+Шорт',
                     'Лонг+Мид',
                     'Шорт+Мид']

    def print_scenariy(self):
        print('----------------')
        print('Карта :',self.current_map)
        print('Игра на плент:',self.current_plent)
        print('Для передвижения разрешено использовать:',self.current_path)
        print('! Через другой плент не ходим !')
        print('Команда А атакует')
        print('Состав команды A (красные):')
        for i in range(len(self.teamA)):
            print('*',self.teamA[i])
        print('Состав команды B (синие):')
        for i in range(len(self.teamB)):
            print('*',self.teamB[i])
        print('\nИнформация по игрокам:')
        for i in self.used_players:
            print(i,':',players[i])
        rez=''
        rez+='Карта : '+self.current_map+'\n'
        rez+='Игра на плент: '+self.current_plent+'\n'
        rez+='Для передвижения разрешено использовать: '+self.current_path+'\n'
        rez+='! Через другой плент не ходим !\n'
        rez+='Команда А атакует\n'
        rez+='Состав команды A (красные):\n'
        for i in range(len(self.teamA)):
            rez+=' * '+self.teamA[i]+'\n'
        rez+='Состав команды B (синие):\n'
        for i in range(len(self.teamB)):
            rez+=' * '+self.teamB[i]+'\n'
        rez+='\nИнформация по игрокам:\n'
        for i in self.used_players:
            rez+=i+' : '+players[i]+'\n'
        # rez+='Тренеровка еще не началась.'

        return rez

    def print_team_players(self):
        print('----------------')
        print('Команда А атакует')
        print('Состав команды A (красные):')
        for i in range(len(self.teamA)):
            print('*',self.teamA[i])
        print('Состав команды B (синие):')
        for i in range(len(self.teamB)):
            print('*',self.teamB[i])
        print('\nИнформация по игрокам:')
        for i in self.used_players:
            print(i,':',players[i])
        rez=''
        rez+='Команда А атакует\n'
        rez+='Состав команды A (красные):\n'
        for i in range(len(self.teamA)):
            rez+=' * '+self.teamA[i]+'\n'
        rez+='Состав команды B (синие):\n'
        for i in range(len(self.teamB)):
            rez+=' * '+self.teamB[i]+'\n'

        return rez




    def run_scenariy(self,a,b):
        rez=self.set_team_players(a,b)
        self.current_map = self.get_map()
        self.current_path = self.get_path()
        self.current_plent = self.get_plent()
        return rez+'\n'+self.print_scenariy()

    def set_team_players(self,a=1,b=3):
        # a - (красные)
        # b - (синие)
        self.used_players = []
        self.teamA = []
        self.teamB = []
        a=int(a)
        b=int(b)

        if a+b>len(players):
            return 'Не могу набрать '+str(a+b)+' игроков, в базе '+str(len(players))
        for i in range(a):
            self.teamA.append(self.get_player())
        for i in range(b):
            self.teamB.append(self.get_player())
        return self.print_team_players()


    def get_player(self):
        f = True
        while f:
            key = [*players.keys()][random.randint(0,len(players)-1)]
            if key not in self.used_players:
                f = False
                self.used_players.append(key)
        return key

    def get_map(self):
        return maps[random.randint(0,len(maps)-1)]

    def get_path(self):
        return self.path[random.randint(0,len(self.path)-1)]

    def get_plent(self):
        return self.plent[random.randint(0,len(self.plent)-1)]




maps    = []
players = {}
def_players= {'Волос':'Крысюк, пушит',
          '^2phoenix':'Мастер раскида и фамаса',
          'Tima':'Принимает решения на лету, раздает хедшоты',
          'B.C':'Темная лошадка',
          'dsp':'Пушит, заходит в спину',
          'gg':'Крысюк, мастер по смене позиций',
          'KVADRAT':'Пушит, раздает хедшоты',
          'kub_4d':'Крысюк, везунчик'
          }
def_maps = ['dust2',
        'pipes',
        'oilrig',
        'Luxor',
        'Stockpile',
        'Seaside',
        'Reachsky',
        'Cache',
        'overpass',
        'mirage',
        'inferno',
        'legend',
        'train',
        'industry',
        'manor',
        'de_museum',
        'Stahlbrecher',
        'Dig',
        'Forest Ruins',
        'Herat',
        'Outpost',
        'Paperclip',
        'Poplar',
        #'Sarajevo', проверить что за карта
        'Remnant'
        ]

def players_print():
    rez='Игроки:\n'
    for i in players:
        rez+=' * '+i+'\n'
    rez+='\nИнформация по игрокам:\n'
    for i in players:
        rez+=i+' : '+players[i]+'\n'
    return rez

def maps_print():
    rez='Карты:\n'
    for i in maps:
        rez+=' * '+i+'\n'
    return rez

def players_shange(action, name, description):
    if action=='+':
        players[name]=description
        return 'Удачно.'
    elif action=='-':
        del players[name]
        return 'Удачно.'
    else:
        return 'Второй параметр должен быть + или -'

def maps_shange(action, name):
    if action=='+':
        if name not in maps:
            maps.append(name)
            return 'Удачно.'
        else:
            return 'Такая карта уже есть.'
    elif action=='-':
        if name not in maps:
            return 'Такой карты нет в базе.'
        else:
            maps.remove(name)
            return 'Удачно.'
    else:
        return 'Второй параметр должен быть + или -'

# сохраняет игроков и карты в базу
def save():
    #global maps
    file='maps.txt'
    json.dump(maps,open(file,"w"))
    file='players.txt'
    json.dump(players,open(file,"w"))
    return 'Изменения сохранены.'

def load():
    global maps
    global players
    file='maps.txt'
    if os.path.isfile(file):
        d = open(file).read()
        maps = json.loads(d)
        file='players.txt'
        if os.path.isfile(file):
            d = open(file).read()
            players = json.loads(d)
            return 'Изменения сохранены.'
        else:
            return 'Файл с игроками поврежден.'
    else:
        return 'Файл с картами поврежден.'

def default():
    global maps
    global players
    maps = def_maps
    players = def_players
    return 'Настройки восстановлены.'



import discord
from discord.ext import commands
#from config import settings

def discord_bot(def_for_run):
        settings = {'token': 'ODIyNTM1MTYwNjM3MjkyNjE0.YFTrkA.5ow3C1AODjP7YQaDpkgfd-TNY0s'}
        #self.bot = commands.Bot(command_prefix = self.settings['prefix'])
        client = discord.Client()
        @client.event
        async def on_message(message):
            if message.author == client.user:
                 return

            tmp=message.content
            #tmp=tmp.lower()
            print(str(message.author),'---',str(tmp))
            #if True:
            try:

                # print(tmp)
                
                # if str(message.author) == 'kub_4d#4832':
                #    print('!!!!')
                #if message.content.startswith('сценарий'):
                if str(message.author) == 'MaxGreenTvain#4630':
                    await message.channel.send('Слава Украине.')
                if tmp.find('<@!365300392650604544>')>-1: #Max
                    await message.channel.send('Слава Украине.')
                if tmp.find('<@!822535160637292614>')>-1: #Kurt
                    await message.channel.send('Это я!.')
                elif tmp.lower().find('сценарий')>-1:
                    if tmp.find(':')>-1:
                        a,b =tmp.split(' ')[1].split(':')
                        await message.channel.send(def_for_run.run_scenariy(a=a,b=b))
                        # def_for_run.run() Что это такое?
                    else:
                        await message.channel.send('Не правильно задано разбиение на команды')
                elif tmp.find(':')>-1:
                    a,b =tmp.split(':')
                    await message.channel.send(def_for_run.set_team_players(a=a,b=b))
                    #await message.channel.send('test')
                elif tmp.lower().find('помощь')>-1:
                    rez='Бот отвечает на следующе команды:\n'
                    rez+=' * сценарий 2:3                     - выдает план на тренировку\n'
                    rez+=' * 1:3                                        - выдает состав команд\n'
                    rez+=' * игроки                               - выдает список игроков\n'
                    rez+=' * карты                                 - выдает список карт\n'
                    rez+=' * игрок + имя описание   - Добавляет игрока с текущим именем и описанием в базу, если такой игрок уже есть, то меняет описание\n'
                    rez+=' * игрок - имя                       - Удаляет игрока с текущим именем из базы\n'
                    rez+=' * карта + название           - Добавляет карту в базу\n'
                    rez+=' * карта - название            - Удаляет карту из базы\n'
                    rez+=' * сохранить                                    - сохраняет изменения\n'
                    rez+=' * сбросить                                       - восстанавливает все к первоначальному виду\n'
                    rez+=' * помощь   - вызывает подсказку'
                    await message.channel.send(rez)
                elif tmp.lower().find('игроки')>-1:
                    await message.channel.send(players_print())
                elif tmp.lower().find('карты')>-1:
                    await message.channel.send(maps_print())
                elif tmp.lower().find('игрок')>-1:
                    if tmp.find('+')>-1:
                        cmd, action, name, description =tmp.split(' ', maxsplit=3)
                        await message.channel.send(players_shange(action, name, description))
                    else:
                        cmd, action, name =tmp.split(' ', maxsplit=2)
                        await message.channel.send(players_shange(action, name, ''))
                elif tmp.lower().find('карта')>-1:
                    if (tmp.find('+')>-1 or
                            tmp.find('-')>-1):
                        cmd, action, name =tmp.split(' ', maxsplit=2)
                        await message.channel.send(maps_shange(action, name))
                elif tmp.lower().find('сохранить')>-1:
                    await message.channel.send(save())
                elif tmp.lower().find('сбросить')>-1:
                    await message.channel.send(default())
                elif tmp.lower().find('вот мое мнение на этот счет')>-1:
                    await message.channel.send('Слава Украине.')
                elif tmp.lower().find('слава украине')>-1:
                    await message.channel.send('героям слава')
                else:
                    await message.channel.send('Вообще не похоже на комнду.')
            except:
                await message.channel.send('Не правильная команда!!!')

        client.run(settings['token'])






print('Запущен генератор для тренировок Impuls')
random.seed()

#generator = Generator(p_in_t=2,players=players,maps=maps)
generator = Generator(p_in_t=2)
discord_bot(generator)
