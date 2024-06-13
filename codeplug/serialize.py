import csv
import io

from codeplug.channel import Channel

CHIRP_NAMES = [
    "Location",
    "Name",
    "Frequency",
    "Duplex",
    "Offset",
    "Tone",
    "rToneFreq",
    "cToneFreq",
    "DtcsCode",
    "DtcsPolarity",
    "RxDtcsCode",
    "CrossMode",
    "Mode",
    "TStep",
    "Skip",
    "Power",
    "Comment",
    "URCALL",
    "RPT1CALL",
    "RPT2CALL",
    "DVCODE",
]


def serialize(channels: list[Channel]) -> str:
    file = io.StringIO()

    writer = csv.DictWriter(file, fieldnames=CHIRP_NAMES)
    writer.writeheader()
    for i, channel in enumerate(channels):
        if channel.site:
            name = channel.site.callsign
            description = f"{channel.site.operator} at {channel.site.location}"
        else:
            name = channel.label
            description = channel.description or ""

        if channel.mode == "duplex":
            duplex = "+" if channel.offset > 0 else "-"
        else:
            duplex = ""

        if channel.dtcs and channel.dtcs.tx:
            tone = "DTCS"
        elif channel.dtcs and channel.dtcs.rx:
            tone = "DTCS-R"
        elif channel.tone and channel.tone.tx and channel.tone.rx:
            tone = "TSQL"
        elif channel.tone and channel.tone.tx:
            tone = "Tone"
        elif channel.tone and channel.tone.rx:
            tone = "TSQL-R"
        else:
            tone = ""

        writer.writerow(
            {
                "Location": i + 1,
                "Name": name,
                "Frequency": channel.frequency,
                "Duplex": duplex,
                "Offset": channel.offset,
                "Tone": tone,
                "rToneFreq": (channel.tone.tx or 88.5) if channel.tone else 88.5,
                "cToneFreq": (channel.tone.rx or 88.5) if channel.tone else 88.5,
                "DtcsCode": (channel.dtcs.tx or 23) if channel.dtcs else 23,
                "DtcsPolarity": channel.dtcs.polarity if channel.dtcs else "NN",
                "RxDtcsCode": (channel.dtcs.rx or 23) if channel.dtcs else 23,
                "CrossMode": "Tone->Tone",  # TODO
                "Mode": channel.mode.name,
                "TStep": 5.0,  # TODO
                "Skip": "",  # TODO
                "Power": "50W",  # TODO
                "Comment": description,
                "URCALL": "",
                "RPT1CALL": "",
                "RPT2CALL": "",
                "DVCODE": "",
            }
        )

    return file.getvalue()
