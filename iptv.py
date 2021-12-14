import requests

api_url = "https://iptv-org.github.io/iptv/channels.json"


class Channel:
    channel_name: str
    channel_url: str

    def __init__(self, channel_name, channel_url):
        self.channel_name = channel_name
        self.channel_url = channel_url

    def __str__(self):
        return f"""Channel({self.channel_name}, {self.channel_url}) """

    def __repr__(self):
        return f"""Channel({self.channel_name}, {self.channel_url}) """


def get_data(): return list(filter(lambda tv: tv["category"] != "XXX", requests.get(api_url).json()))


def get_by_country(c):
    filter_country = list(
        filter(lambda x: x["countries"] and c in [country["code"] for country in x["countries"]], get_data()))
    obj_list = list(map(lambda channel: Channel(channel["name"], channel["url"]), filter_country))
    return [ob.__dict__ for ob in obj_list]


def get_by_category(c):
    filter_category = list(filter(lambda x: x["category"] and x["category"].lower() == c.lower(), get_data()))
    obj_list = list(map(lambda channel: Channel(channel["name"], channel["url"]), filter_category))
    return [ob.__dict__ for ob in obj_list]


def get_by_name(c):
    filter_category = list(filter(lambda x: x["name"] and c.lower() in x["name"].lower(), get_data()))
    obj_list = list(map(lambda channel: Channel(channel["name"], channel["url"]), filter_category))
    return [ob.__dict__ for ob in obj_list]



def get_by_lang(c):
    filter_country = list(
        filter(lambda x: x["languages"] and c.lower() in [country["name"].lower() for country in x["languages"]], get_data()))
    obj_list = list(map(lambda channel: Channel(channel["name"], channel["url"]), filter_country))
    return [ob.__dict__ for ob in obj_list]

def get_all_cats():

    return set(map(lambda x: x["category"], get_data()))


