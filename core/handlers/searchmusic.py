from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from core.spotify_settings import clientsettings
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

searchrouter = Router()

search_count = 5

@searchrouter.message(Command(commands=['search']))
async def search_track(message: Message):
    global search_count
    track_name = message.text.replace('/search', '').strip()

    client_credentials_manager = SpotifyClientCredentials(client_id=clientsettings.app.client_id,
                                                        client_secret=clientsettings.app.client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q=f'track:"{track_name}"', type='track', limit=search_count)
    tracks = results['tracks']['items']
    if tracks:
        response_message = "Список найденных песен:\n"
        for track in tracks:
            response_message += f'''Название трека: {track['name']}
Исполнитель: {track['artists'][0]['name']}
Альбом: {track['album']['name']}
Ссылка на трек: {track['external_urls']['spotify']}\n\n'''
        await message.answer(response_message)
    else:
        await message.answer('Информация о треке не найдена')

@searchrouter.message(Command(commands=['setcount']))
async def set_search_count(message: Message):
    global search_count
    input_count = message.text.replace('/setcount', '').strip()
    try:
        int(input_count)
    except:
        await message.answer('Количество должно быть целым числом')
        return
    if int(input_count) <= 0 or int(input_count) >= 25:
        await message.answer('Количество должно быть не менее 1 и не более 25')
        return
    search_count = input_count
    await message.answer(f'Количество треков для поиска успешно обновлено до {input_count}')