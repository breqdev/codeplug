import csv

from codeplug.channel import Channel, ChannelType, ChannelMode, CtcssTone, DtcsTone


def load_file(file: str, only_starred: bool = False) -> list[Channel]:
    channels = []

    with open(file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if only_starred and not row.get("starred", False):
                continue

            channels.append(
                Channel(
                    frequency=float(row["frequency"]),
                    type=ChannelType.from_str(row["type"]),
                    offset=float(row.get("offset", 0)),
                    tone=CtcssTone.from_data(row.get("tone"))
                    if ("tone" in row)
                    else None,
                    dtcs=DtcsTone.from_data(row.get("dtcs"))
                    if ("dtcs" in row)
                    else None,
                    mode=ChannelMode[row.get("mode", "FM").upper()],
                    label=row.get("label"),
                    description=row.get("description"),
                    site=None,
                )
            )

    return channels
