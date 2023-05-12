def prepair_data(data: dict) -> dict:
    res = {}
    res["id"] = int(data["id"])
    res["name"] = data["name"]
    res["description"] = f'{data["snippet"]["requirement"]}. {data["snippet"]["responsibility"]}'
    if "salary" in data and data["salary"] is not None:
        res["salary"] = data["salary"]["from"]
    else:
        res["salary"] = None
    res["published_at"] = data["published_at"]
    res["url"] = data["url"]
    return res
