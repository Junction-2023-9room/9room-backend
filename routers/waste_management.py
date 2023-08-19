from fastapi import APIRouter
from ..database.connection import db

router = APIRouter()


class WasteItem(BaseModel):
    name: str
    description: str
    disposal_method: str


@router.get("/wastes/", response_model=List[WasteItem])
async def get_waste_items():
    waste_items = db.wastes.find()
    return list(waste_items)
