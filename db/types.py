from typing import Optional, List
from typing_extensions import TypedDict


class TopTracksType(TypedDict):
    song_name: str
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
        display_name: Optional[str] = None,
        country: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        self.id = id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.top_tracks_month = top_tracks_month
        self.top_tracks_half_year = top_tracks_half_year
        self.top_tracks_year = top_tracks_year
        self.display_name = display_name
        self.country = country
        self.created_at = created_at
        self.updated_at = updated_at


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


class IUserProfile(TypedDict):
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