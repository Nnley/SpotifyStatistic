from services.spotify_service import SpotifyService, TimeRange
from aiogram import types
from db.crud import UserManager
from aiogram import Dispatcher
from localization import get_text

async def create_inline_result(id: str, title: str, description: str, message_text: str, reply_markup=None) -> types.InlineQueryResultArticle:
    return types.InlineQueryResultArticle(
        id=id,
        title=title,
        description=description,
        input_message_content=types.InputTextMessageContent(
            message_text=message_text
        ),
        reply_markup=reply_markup
    )

async def get_user_top_tracks_message(user_profile, user_top_tracks, time_period: str, language_code: str) -> str:
    if user_top_tracks is not None and user_profile is not None:
        message_template = get_text(language_code, 'inline_query_message')
        message_text = message_template.format(
            display_name=user_profile.get('display_name'),
            country=user_profile.get('country'),
            time_period=time_period
        )
        
        message_text += '\n\n' + '\n'.join([f"{i + 1}. {track.get('name')} - {track.get('artist')}" for i, track in enumerate(user_top_tracks)])
    else:
        message_text = get_text(language_code, 'error_message')
    return message_text

async def inline_handler(query: types.InlineQuery):
    user_id = query.from_user.id
    user = UserManager.get_or_create_user(user_id)
    
    results = []
    
    if user.refresh_token is None:
        results.append(
            await create_inline_result(
                id='1',
                title=get_text(user.language_code, 'inline_query_title'),
                description=get_text(user.language_code, 'none_auth_get_stats'),
                message_text=get_text(user.language_code, 'none_auth_get_stats'),
                reply_markup=types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton(
                        text=get_text(user.language_code, 'auth_button_text'),
                        url='https://t.me/SpotifyStatisticBot?start=auth'
                    )  # type: ignore
                )
            )
        )
    else:
        spotify_service = SpotifyService()
        user_top_tracks_month = spotify_service.get_user_top_tracks(user_id, TimeRange.SHORT_TERM)
        user_top_tracks_half_year = spotify_service.get_user_top_tracks(user_id, TimeRange.MEDIUM_TERM)
        user_top_tracks_year = spotify_service.get_user_top_tracks(user_id, TimeRange.LONG_TERM)
        user_profile = spotify_service.get_user_profile(user_id)

        top_tracks_month_message_text = await get_user_top_tracks_message(user_profile, user_top_tracks_month, get_text(user.language_code, 'word_month'), user.language_code)
        top_tracks_half_year_message_text = await get_user_top_tracks_message(user_profile, user_top_tracks_half_year, get_text(user.language_code, 'word_half_year'), user.language_code)
        top_tracks_year_message_text = await get_user_top_tracks_message(user_profile, user_top_tracks_year, get_text(user.language_code, 'word_year'), user.language_code)

        description_template = get_text(user.language_code, 'inline_query_description')

        results.append(
            await create_inline_result(
                id='2',
                title=get_text(user.language_code, 'word_statistic').title(),
                description=description_template.format(time_period=get_text(user.language_code, 'word_month')),
                message_text=top_tracks_month_message_text,
            )
        )
        results.append(
            await create_inline_result(
                id='3',
                title=get_text(user.language_code, 'word_statistic').title(),
                description=description_template.format(time_period=get_text(user.language_code, 'word_half_year')),
                message_text=top_tracks_half_year_message_text,
            )
        )
        results.append(
            await create_inline_result(
                id='4',
                title=get_text(user.language_code, 'word_statistic').title(),
                description=description_template.format(time_period=get_text(user.language_code, 'word_year')),
                message_text=top_tracks_year_message_text,
            )
        )

    await query.answer(results, cache_time=1, is_personal=True)

def register_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_handler)
