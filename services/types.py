from typing import TypedDict, List, Dict, Optional

class ExternalUrls(TypedDict):
    spotify: str

class Artist(TypedDict):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str

class Image(TypedDict):
    height: int
    url: str
    width: int

class Album(TypedDict):
    album_type: str
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str

class ExternalIds(TypedDict):
    isrc: str

class Track(TypedDict):
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: Optional[str]
    track_number: int
    type: str
    uri: str