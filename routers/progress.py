from fastapi import APIRouter
import random
import time

router = APIRouter()


@router.get("/progress/calculate")
def get_progress():
    sleep_time = random.uniform(1.5, 3.5)
    time.sleep(sleep_time)
    return {"your progress time:": f"{sleep_time} seconds"}
