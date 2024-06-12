# codeplug

An automated codeplug generator covering simplex channels, amateur radio repeaters, railroad channels, and more. Currently focused on US & Canada.

## Format

```yaml name=CALLSIGN.yaml
frequency: <number>
type: simplex | duplex | no-tx
offset: _signed_ number (default 0)
tone:
    tx: number (default off)
    rx: number (default off)
dtcs:
    tx: number (default off)
    rx: number (default off)
    polarity: NN | NR | RN | RR
mode: FM | NFM

label: string

site:
    operator: string
    callsign: string
    location: string
    latitude: number
    longitude: number
```
