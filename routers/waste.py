from fastapi import APIRouter

router = APIRouter()


@router.get("/wastes/")
async def get_waste_items():
    return ""
