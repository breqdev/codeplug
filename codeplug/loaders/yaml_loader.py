import yaml

from codeplug.channel import (
    Channel,
    ChannelType,
    ChannelMode,
    CtcssTone,
    DtcsTone,
    Site,
)


def load_file(file: str) -> Channel:
    with open(file) as f:
        data = yaml.safe_load(f)

    if "site" in data:
        site = Site(
            operator=data["site"].get("operator"),
            callsign=data["site"].get("callsign"),
            location=data["site"].get("location"),
            latitude=data["site"].get("latitude"),
            longitude=data["site"].get("longitude"),
        )
    else:
        site = None

    return Channel(
        frequency=data["frequency"],
        type=ChannelType.from_str(data["type"]),
        offset=data.get("offset", 0),
        tone=CtcssTone.from_data(data.get("tone")) if ("tone" in data) else None,
        dtcs=DtcsTone.from_data(data.get("dtcs")) if ("dtcs" in data) else None,
        mode=ChannelMode[data.get("mode", "FM").upper()],
        label=data.get("label"),
        description=data.get("description"),
        site=site,
    )
