localization: dict[str, dict[str, str]] = {
    'ru': {
        'none_auth_start': 'Привет! Я способен отображать ваше статистику Spotify!\nЧтобы получить статистику, Вам необходимо авторизоваться через Spotify. Для этого введите команду /auth.\n\nIf you want to change the language, enter the command /change_language',
        'none_auth_get_stats': 'Чтобы получить статистику, Вам необходимо авторизоваться в боте через Spotify',
        'auth_start': 'Привет! Я способен отображать ваше статистику Spotify!\nДоступные команды: /stats, /change_language',
        'auth_button_text': 'Авторизоваться',
        'auth_button_description': 'Для авторизации нажмите на кнопку ниже:',
        'auth_success': 'Вы успешно прошли авторизацию',
        'already_authorized': 'Вы уже авторизованы',
        
        'change_language_button_text': 'Русский | Russian',
        'change_language_buttons_description': 'Выберите язык:',
        
        'help': 'Этот бот так же работает в inline режиме! В любом чате напиши @SpotifyStatisticBot и нажми пробел, высветится контекстное меню с выбором действий!\nВсе доступные команды: /stats, /auth, /change_language',
        'stats': 'Напишите <code>@SpotifyStatisticBot</code> в поле ввода сообщения и нажмите пробел, чтобы вызвать контекстное меню с выбором действий',
        
        'inline_query_title': 'Моя статистика Spotify',
        'inline_query_description': 'Посмотреть топ моих самых прослушиваемых треков за {time_period}',
        'inline_query_message': 'Статистика {display_name} ({country}) в Spotify за {time_period}:',
        'inline_query_error': 'Возникла ошибка при получении статистики',
        
        'word_month': 'месяц',
        'word_half_year': 'полгода',
        'word_year': 'год',
        'word_statistic': 'статистика'
    },
    'en': {
        'none_auth_start': 'Hello! I can display your Spotify statistics!\nTo get the statistics, you need to authorize Spotify. To do this, enter the command /auth.\n\nЕсли хотите сменить язык, введите команду /change_language',
        'none_auth_get_stats': 'To get the statistics, you need to authorize the bot with Spotify',
        'auth_start': 'Hello! I can display your Spotify statistics!\nAvailable commands: /stats, /change_language',
        'auth_button_text': 'Authorize',
        'auth_button_description': 'To authorize, press the button below:',
        'auth_success': 'You have successfully authorized',
        'already_authorized': 'You are already authorized',
        
        'change_language_button_text': 'English',
        'change_language_buttons_description': 'Choose a language:',
        
        'help': 'This bot also works in inline mode! In any chat, write @SpotifyStatisticBot and press space, you will see a context menu with options!\nAll available commands: /stats, /auth, /change_language',
        'stats': 'Write <code>@SpotifyStatisticBot</code> in the message input field and press space to call the context menu with options',
      
        'inline_query_title': 'My Spotify statistics',
        'inline_query_description': 'See my top Spotify tracks for {time_period}',
        'inline_query_message': 'Statistics of {display_name} ({country}) on Spotify for {time_period}:',
        'inline_query_error': 'Failed to get statistics',
        
        'word_month': 'month',
        'word_half_year': 'half-year',
        'word_year': 'year',
        'word_statistic': 'statistic'
    },
    'lv': {
        'none_auth_start': 'Sveiki! Es varu parādīt jūsu Spotify statistiku!\nLai iegūtu statistiku, ir nepieciešams autorizēt Spotify. Lai to izdarītu, ievadiet komandu /auth.\n\nIf you want to change the language, enter the command /change_language',
        'none_auth_get_stats': 'Lai iegūtu statistiku, ir nepieciešams autorizēt robotu pakalpojumā Spotify',
        'auth_start': 'Sveiki! Es varu parādīt jūsu Spotify statistiku!\nPieejamās komandas: /stats, /change_language',
        'auth_button_text': 'Pierakstīties',
        'auth_button_description': 'Noklikšķiniet uz pogas zemāk, lai autorizētu:',
        'auth_success': 'Jūs esat veiksmīgi autorizēts',
        'already_authorized': 'Jūs jau esat pieteicies',
        
        'change_language_button_text': 'Latviešu | Latvian',
        'change_language_buttons_description': 'Choose a language:',
        
        'help': 'Šis robots darbojas arī inline! Jebkurā tērzēšanas režīmā ierakstiet @SpotifyStatisticBot un nospiediet atstarpes taustiņu, parādīsies konteksta izvēlne ar dažādām darbībām!\nVisas pieejamās komandas: /stats, /auth, /change_language.',
        'stats': 'Ierakstiet <code>@SpotifyStatisticBot</code> ziņojuma ievades lodziņā un nospiediet atstarpes taustiņu, lai atvērtu kontekstuālo izvēlni ar darbību izvēli.',
     
        'inline_query_title': 'Mana Spotify statistika',
        'inline_query_description': 'Pārbaudiet manu {time_period} visvairāk klausīto dziesmu topu',
        'inline_query_message': 'Statistika {display_name} ({country}) Spotify par {time_period}:',
        'inline_query_error': 'Iegūstot statistiku, radās kļūda',
        
        'word_month': 'mēnesis',
        'word_half_year': 'pusgads',
        'word_year': 'gads',
        'word_statistic': 'statistika'
    }
}

def get_text(language: str, key: str) -> str:
    return localization.get(language, localization['en']).get(key, '')