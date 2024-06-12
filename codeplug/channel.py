from dataclasses import dataclass
from enum import Enum

class ChannelType(Enum):
    SIMPLEX = 1
    DUPLEX = 2
    NO_TX = 3

    @classmethod
    def from_str(cls, value: str) -> "ChannelType":
        if value == 'simplex':
            return cls.SIMPLEX
        elif value == 'duplex':
            return cls.DUPLEX
        elif value == 'no-tx':
            return cls.NO_TX
        else:
            raise ValueError(f"Invalid ChannelType: {value}")

class ChannelMode(Enum):
    FM = 1
    NFM = 2

@dataclass
class CtcssTone:
    tx: float | None
    rx: float | None

    @classmethod
    def from_data(cls, value: dict | float | str) -> "CtcssTone":
        if isinstance(value, dict):
            return cls(tx=float(value.get("tx")) if "tx" in value else None, rx=float(value.get("rx")) if "rx" in value else None)
        else:
            return cls(tx=float(value), rx=float(value))

@dataclass
class DtcsTone:
    tx: int
    rx: int
    polarity: str = 'NN'

    @classmethod
    def from_data(cls, value: dict | int) -> "DtcsTone":
        if isinstance(value, dict):
            return cls(tx=int(value["tx"]), rx=int(value["rx"]), polarity=value.get("polarity", 'NN'))
        else:
            return cls(tx=int(value), rx=int(value))

@dataclass
class Site:
    operator: str | None
    callsign: str | None
    location: str | None
    latitude: float | None
    longitude: float | None

@dataclass
class Channel:
    frequency: float
    type: ChannelType
    offset: float = 0
    tone: CtcssTone | None = None
    dtcs: DtcsTone | None = None
    mode: ChannelMode = ChannelMode.FM

    label: str | None = None
    description: str | None = None
    site: Site | None = None
