from fastapi import FastAPI, Depends, Query

app = FastAPI()

db = [{"id": i, "label": f"item-{i}"} for i in range(1, 26)]


def pagination(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=50)
):
    return {"skip": skip, "limit": limit}


@app.get("/catalog")
def get_catalog(p=Depends(pagination)):
    skip = p["skip"]
    limit = p["limit"]

    sliced_items = db[skip:skip + limit]

    return {
        "skip": skip,
        "limit": limit,
        "total": 25,
        "items": sliced_items
    }


@app.get("/catalog/ids")
def get_catalog_ids(p=Depends(pagination)):
    skip = p["skip"]
    limit = p["limit"]

    sliced_items = db[skip:skip + limit]
    ids_list = [item["id"] for item in sliced_items]

    return {
        "skip": skip,
        "limit": limit,
        "ids": ids_list
    }