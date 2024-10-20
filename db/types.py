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
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        self.id = id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.top_tracks_month = top_tracks_month
        self.top_tracks_half_year = top_tracks_half_year
        self.top_tracks_year = top_tracks_year
        self.created_at = created_at
        self.updated_at = updated_at
