import os


class Config(object):
    token = "1921635851:AAHgKoe5MV_jmnuRi6VIw-4yj5Zzsig4o2E"
    api_id = "5689646"
    api_hash = "895de5ae804308803c19814afabb0de7"
    log_id = "-1001177104541"
    start_msg = os.environ.get("START_MSG", None)
    ownerID = "1808767615"
    if ownerID:
        try:
            ownerID = [int(ID) for ID in ownerID.split("|")]
        except:
            ownerID = []
