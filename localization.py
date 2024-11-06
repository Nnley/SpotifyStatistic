localization: dict[str, dict[str, str]] = {
    'ru': {
        'none_auth_start': 'Привет! Я способен отображать вашу статистику Spotify!\nЧтобы получить статистику, Вам необходимо авторизоваться через Spotify. Для этого введите команду /auth.\n\nIf you want to change the language, enter the command /change_language',
        'none_auth_get_stats': 'Чтобы получить статистику, Вам необходимо авторизоваться в боте через Spotify',
        'none_auth_inline_query_title': 'Моя статистика Spotify',
        'auth_start': 'Привет! Я способен отображать вашу статистику Spotify!\nДоступные команды: /stats, /change_language, /help, /github',
        'auth_button_text': 'Авторизоваться',
        'auth_button_description': 'Для авторизации нажмите на кнопку ниже:',
        'auth_success': 'Вы успешно прошли авторизацию',
        'already_authorized': 'Вы уже авторизованы',
        
        'github': 'Этот бот является некоммерческим проектом. Исходным кодом бота вы можете посмотреть здесь: https://github.com/Nnley/SpotifyStatistics-TGBot',
        
        'change_language_button_text': 'Русский | Russian',
        'change_language_buttons_description': 'Выберите язык:',
        
        'help': 'Этот бот способен отправлять вашу статистику Spotify!\nВ любом чате напишите <code>@SpotifyStatisticBot</code> и нажмите пробел, высветится контекстное меню с выбором действий!\nВсе доступные команды: /stats, /auth, /change_language, /github',
        'stats': 'Напишите <code>@SpotifyStatisticBot</code> в поле ввода сообщения и нажмите пробел, чтобы вызвать контекстное меню с выбором действий',
        
        'currently_playing_inline_query_title': 'Сейчас играет',
        'currently_playing_inline_query_message': '{display_name} ({country}) сейчас слушает:\nТрек: <a href="{song_link}">{song}</a>\nАртист: <b>{artist}</b>\nАльбом: <b>{album}</b>',
        
        'tracks_inline_query_title': 'Статистика по трекам',
        'tracks_inline_query_description': 'Посмотреть топ моих самых прослушиваемых треков за {time_period}',
        'tracks_inline_query_message': 'Самые прослушиваемые треки {display_name} ({country}) в Spotify за {time_period}:',
        
        'artists_inline_query_title': 'Статистика по артистам',
        'artists_inline_query_description': 'Посмотреть топ моих самых прослушиваемых артистов за {time_period}',
        'artists_inline_query_message': 'Самые прослушиваемые артисты {display_name} ({country}) в Spotify за {time_period}:',
        
        'inline_query_error': 'Возникла ошибка при получении статистики',
        
        'word_month': 'месяц',
        'word_half_year': 'полгода',
        'word_year': 'год',
        'word_statistic': 'статистика'
    },
    'en': {
        'none_auth_start': 'Hello! I can display your Spotify statistics!\nTo get the statistics, you need to authorize Spotify. To do this, enter the command /auth.\n\nЕсли хотите сменить язык, введите команду /change_language',
        'none_auth_get_stats': 'To get the statistics, you need to authorize the bot with Spotify',
        'none_auth_inline_query_title': 'My Spotify statistics',
        'auth_start': 'Hello! I can display your Spotify statistics!\nAvailable commands: /stats, /change_language, /help, /github',
        'auth_button_text': 'Authorize',
        'auth_button_description': 'To authorize, press the button below:',
        'auth_success': 'You have successfully authorized',
        'already_authorized': 'You are already authorized',
        
        'github': 'This bot is a non-commercial project. You can see the source code of the bot here: https://github.com/Nnley/SpotifyStatistics-TGBot',
        
        'change_language_button_text': 'English',
        'change_language_buttons_description': 'Choose a language:',
        
        'help': 'This bot can send your Spotify statistics!\nIn any chat, write <code>@SpotifyStatisticBot</code> and press space, you will see a context menu with options!\nAll available commands: /stats, /auth, /change_language, /github',
        'stats': 'Write <code>@SpotifyStatisticBot</code> in the message input field and press space to call the context menu with options',
      
        'currently_playing_inline_query_title': 'Currently playing',
        'currently_playing_inline_query_message': '{display_name} ({country}) is currently listening to:\nSong: <a href="{song_link}">{song}</a>\nArtist: <b>{artist}</b>\nAlbum: <b>{album}</b>',
      
        'tracks_inline_query_title': 'Statistics by top tracks',
        'tracks_inline_query_description': 'See my top Spotify tracks for {time_period}',
        'tracks_inline_query_message': 'Top Spotify tracks {display_name} ({country}) for {time_period}:',
        
        'artists_inline_query_title': 'Statistics by top artists',
        'artists_inline_query_description': 'See my top Spotify artists for {time_period}',
        'artists_inline_query_message': 'Top Spotify artists {display_name} ({country}) for {time_period}:',
        
        'inline_query_error': 'Failed to get statistics',
        
        'word_month': 'month',
        'word_half_year': 'half-year',
        'word_year': 'year',
        'word_statistic': 'statistic'
    },
    'lv': {
        'none_auth_start': 'Sveiki! Es varu parādīt jūsu Spotify statistiku!\nLai iegūtu statistiku, ir nepieciešams autorizēt Spotify. Lai to izdarītu, ievadiet komandu /auth.\n\nIf you want to change the language, enter the command /change_language',
        'none_auth_get_stats': 'Lai iegūtu statistiku, ir nepieciešams autorizēt robotu pakalpojumā Spotify',
        'none_auth_inline_query_title': 'Mana Spotify statistika',
        'auth_start': 'Sveiki! Es varu parādīt jūsu Spotify statistiku!\nPieejamās komandas: /stats, /change_language, /help, /github',
        'auth_button_text': 'Pierakstīties',
        'auth_button_description': 'Noklikšķiniet uz pogas zemāk, lai autorizētu:',
        'auth_success': 'Jūs esat veiksmīgi autorizēts',
        'already_authorized': 'Jūs jau esat pieteicies',
        
        'github': 'Šis robots ir nekomerciāls projekts. Bota pirmkodu varat apskatīt šeit: https://github.com/Nnley/SpotifyStatistics-TGBot',
        
        'change_language_button_text': 'Latviešu | Latvian',
        'change_language_buttons_description': 'Choose a language:',
        
        'help': 'Šis robots var nosūtīt jūsu Spotify statistiku!\nJebkurā tērzēšanas režīmā ierakstiet <code>@SpotifyStatisticBot</code> un nospiediet atstarpes taustiņu, parādīsies konteksta izvēlne ar dažādām darbībām!\nVisas pieejamās komandas: /stats, /auth, /change_language, /github',
        'stats': 'Ierakstiet <code>@SpotifyStatisticBot</code> ziņojuma ievades lodziņā un nospiediet atstarpes taustiņu, lai atvērtu kontekstuālo izvēlni ar darbību izvēli.',
     
        'currently_playing_inline_query_title': 'Šobrīd tiek atskaņota dziesma',
        'currently_playing_inline_query_message': '{display_name} ({country}) pašlaik klausās:\nSong: <a href="{song_link}">{song}</a>\nArtist: <b>{artist}</b>\nAlbum: <b>{album}</b>',
     
        'tracks_inline_query_title': 'Statistika pēc populārākajām dziesmām',
        'tracks_inline_query_description': 'Skatiet manas {time_period} Spotify populārākās dziesmas',
        'tracks_inline_query_message': 'Spotify populārākās dziesmas {display_name} ({country}) par {time_period}:',
        
        'artists_inline_query_title': 'Statistikas dati par labākajiem māksliniekiem',
        'artists_inline_query_description': 'Skatiet manus {time_period} Spotify populārākos māksliniekus',
        'artists_inline_query_message': 'Spotify populārākie mākslinieki {display_name} ({country}) par {time_period}:',
        
        'inline_query_error': 'Iegūstot statistiku, radās kļūda',
        
        'word_month': 'mēnesis',
        'word_half_year': 'pusgads',
        'word_year': 'gads',
        'word_statistic': 'statistika'
    }
}

def get_text(language: str, key: str) -> str:
    return localization.get(language, localization['en']).get(key, '')