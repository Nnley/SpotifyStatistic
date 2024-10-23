from typing import Optional, List
from typing_extensions import TypedDict
from datetime import datetime


class TopTracksType(TypedDict):
    song_name: str
    artist: str
    updated_at: str

    
class TopArtistsType(TypedDict):
    artist: str
    updated_at: str
    

class IUser:
    def __init__(
        self,
        id: int,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        top_tracks_month: Optional[List[TopTracksType]] = None,
        top_tracks_half_year: Optional[List[TopTracksType]] = None,
        top_tracks_year: Optional[List[TopTracksType]] = None,
        top_artists_month: Optional[List[TopArtistsType]] = None,
        top_artists_half_year: Optional[List[TopArtistsType]] = None,
        top_artists_year: Optional[List[TopArtistsType]] = None,
        display_name: Optional[str] = None,
        country: Optional[str] = None,
        language_code: str = 'en',
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        authorization_code: Optional[str] = None
    ):
        self.id = id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.top_tracks_month = top_tracks_month
        self.top_tracks_half_year = top_tracks_half_year
        self.top_tracks_year = top_tracks_year
        self.top_artists_month = top_artists_month
        self.top_artists_half_year = top_artists_half_year
        self.top_artists_year = top_artists_year
        self.display_name = display_name
        self.country = country
        self.language_code = language_code
        self.created_at = created_at
        self.updated_at = updated_at
        self.authorization_code = authorization_code


class ExplicitContent(TypedDict):
    filter_enabled: bool
    filter_locked: bool


class ExternalUrls(TypedDict):
    spotify: str


class Followers(TypedDict):
    href: str
    total: int


class Image(TypedDict):
    url: str
    height: int
    width: int


class IUserProfile(TypedDict, total=False):
    country: str
    display_name: str
    email: str
    explicit_content: ExplicitContent
    external_urls: ExternalUrls
    followers: Followers
    href: str
    id: str
    images: List[Image]
    product: str
    type: str
    uri: str