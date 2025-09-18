from fastapi import APIRouter, Query
from typing import Optional

from app.repo.record_repo import RecordRepo
from app.models.schemas import Filter


class RecordRouter:
    def __init__(self):
        self.recordRepo = RecordRepo()
        self.router = APIRouter()

        self.router.get("/sort_ascending", status_code=200)(self.sort_ascending)
        self.router.get("/cheapest", status_code=200)(self.cheapest)
        self.router.get("/most_expensive", status_code=200)(self.most_expensive)
        self.router.post("/output_filter", status_code=200)(self.output_filter)

    async def sort_ascending(self):
        res = self.recordRepo.get()
        sorted_res = sorted(res, key=lambda x: x["price"])

        return sorted_res

    async def cheapest(self, quantity: int = Query(..., ge=1)):
        res = self.recordRepo.get()
        sorted_res = sorted(res, key=lambda x: x["price"])

        return sorted_res[:quantity]

    async def most_expensive(self, quantity: int = Query(..., ge=1)):
        res = self.recordRepo.get()
        sorted_res = sorted(res, key=lambda x: x["price"], reverse=True)

        return sorted_res[:quantity]

    async def output_filter(self, filter: Filter):
        filter_dict = filter.dict(exclude_none=True)
        res = self.recordRepo.get(filter_dict)

        return res
