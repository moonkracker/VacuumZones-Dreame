# VacuumZones

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

[Home Assistant](https://www.home-assistant.io/) custom component that helps control zone cleaning for [Dreame Vacuum](https://github.com/Tasshack/dreame-vacuum) cleaners with the help of voice assistants - Apple Siri, Google Assistant, Yandex Alice.

This component creates a virtual vacuum cleaner for each of your zone or room.

By adding these vacuums to your voice assistant, you can give voice commands, like "clean bedroom". If your voice assistant supports multiple device commands - you can say "clean up the hall and under the table".

All cleaning commands are **added to the queue**. The vacuum cleaner will start a new room only after it has finished the previous. Cleaning the next room starts when the vacuum goes into `returning` or `docked` state.

Current zone will be in `cleaning` state, next zones will be in `paused` state, other zones will be in `idle` state.

You can pause main vacuum entity, it won't reset the queue. You can stop any of the virtual vacuum cleaners - this will reset the queue, but will not stop cleaning in the current room. You can skip the current room by sending the main vacuum cleaner to the dock, the integration will automatically start the next element of the queue.

## Installation

**Method 1.** [HACS](https://hacs.xyz/) custom repo:

> HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: `moonkracker/VacuumZones-Dreame`, Category: Integration > Add > wait > VacuumZones > Install

## Configuration

Check [lovelace-xiaomi-vacuum-map-card](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) integration for coordinates and rooms extraction.

You can use multiple rooms/zones in one zone item.

`configuration.yaml` example:

```yaml
vacuum_zones:
  entity_id: vacuum.vacuum  # change to your vacuum
  zones:
    Hall:  # room name on your language
      rooms: 20  # one or more rooms

    Under the table:  # zone name on your language
      zones: [[23510,25311,25110,26361]]  # one or more zones
      repeats: 2  # optional, default 1

    Home:  # zone name on your language
      sequence:  # optional script sequence (run before command to vacuum)
      - service: persistent_notification.create
        data:
          message: Starting a complete house cleaning
      rooms: [15,16,17]
      suction_level: 1
      water_volume: 2

    Trash:  # point name on your language
      point: [25500, 25500]  # move to point
```

## Useful links

- [Dreame Vacuum](https://github.com/Tasshack/dreame-vacuum) - Dreame vacuum integration for Home Assistant

- [lovelace-xiaomi-vacuum-map-card](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) - Lovelace Vacuum Map card
