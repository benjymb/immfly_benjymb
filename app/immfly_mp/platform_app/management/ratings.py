from typing import Dict, List

def calculate_ratings(channels : Dict, contents: Dict) -> Dict[str, tuple]:
    print(channels, contents)
    ratings = {}
    while channels:
        to_remove = []
        for channel_id, channel_children in channels.items():
            content_ids = channel_children[1]
            if content_ids:
                ratings[channel_id] = _calculate_average(content_ids, contents)
                to_remove.append(channel_id)
        for calculated in to_remove:
            del channels[calculated]
        to_remove = []
        for channel_id, channel_children in channels.items():
            averages_to_add = []
            subchannel_ids = channel_children[0]
            for subchannel_id in subchannel_ids:
                if ratings.get(subchannel_id):
                    averages_to_add.append(ratings[subchannel_id])
            ratings[channel_id] = _calculate_subchannel_average(averages_to_add)
            to_remove.append(channel_id)
        for calculated in to_remove:
            del channels[calculated]
            
    return _clean_ratings(ratings)


def _calculate_average(content_ids : tuple, contents: Dict) -> tuple:
    total = 0
    for content_id in content_ids:
        total += contents[content_id]
    if total and len(content_ids):
        return (total / len(content_ids), len(content_ids))
    
def _calculate_subchannel_average(averages: List) -> tuple:
    total = 0
    elements = 0
    if len(averages) > 1:
        for average in averages:
            total += average[0]
            elements += average[1]
        return (total / elements, elements)
    else:
        return averages[0]
    
def _clean_ratings(ratings : dict) -> dict:
    cleaned = {}
    for channel_id, rating in ratings.items():
        cleaned[channel_id] = rating[0]
    return cleaned