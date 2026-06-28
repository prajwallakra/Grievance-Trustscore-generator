from pydantic import BaseModel
from typing import List, Optional


class ComplaintRequest(BaseModel):
    grievanceId: str
    complaintId: str

    category: str
    subcategory: str
    description: str

    district: str
    ward: str

    locationLat: float
    locationLng: float

    evidenceUrls: List[str]

    preferredLanguage: str

    isEmergency: bool
    isAnonymous: bool

    mobile: Optional[str] = None

    isVerifiedIdentity: bool

    sourceChannel: str

    linkToClusterId: Optional[str] = None