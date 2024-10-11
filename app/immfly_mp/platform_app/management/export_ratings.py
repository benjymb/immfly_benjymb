import csv

from platform_app.models import Channel
from .ratings import calculate_ratings

def _build_data_for_ratings() -> tuple:
    channels = {}
    channel_titles = {}
    contents = {}
    for channel in Channel.objects.all():
        to_add = []
        if channel.contents.count():
            for content in channel.contents.all():
                contents[str(content.pk)] = content.rating
                to_add.append(str(content.pk))
            to_add = (None, tuple(to_add))
        else:
            for subchannel in channel.subchannels.all():
                to_add.append(str(subchannel.pk))
            to_add = (tuple(to_add), None)
        channels[str(channel.pk)] = to_add
        channel_titles[str(channel.pk)] = channel.title

    return channels, contents, channel_titles

def _ratings_to_csv_file(calculated_ratings : dict, channel_titles : dict):
    ratings = sorted(calculated_ratings.items(), key=lambda item: item[1], reverse=True)
    with open('files/ratings/ratings.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Channel Title", "Rating"])
        for rating in ratings:
            csv_writer.writerow((channel_titles[rating[0]], rating[1]))

def export_ratings():
    channels, contents, channel_titles = _build_data_for_ratings()
    calculated_ratings = calculate_ratings(channels, contents)
    _ratings_to_csv_file(calculated_ratings, channel_titles)
