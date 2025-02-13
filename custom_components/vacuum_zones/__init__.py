import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import CONF_ENTITY_ID, CONF_SEQUENCE
from homeassistant.helpers.typing import HomeAssistantType

DOMAIN = 'vacuum_zones_dreame'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_ENTITY_ID): cv.entity_id,
        vol.Required('zones'): {
            cv.string: vol.Schema({
                vol.Optional('rooms'): vol.Any(list, int),
                vol.Optional('zones'): list,
                vol.Optional('repeats'): int,
                vol.Optional('suction_level'): int,
                vol.Optional('water_volume'): int,
                vol.Optional('point'): list,
                vol.Optional(CONF_SEQUENCE): cv.SCRIPT_SCHEMA
            })
        }
    })
}, extra=vol.ALLOW_EXTRA)


async def async_setup(hass: HomeAssistantType, hass_config: dict):
    hass.async_create_task(hass.helpers.discovery.async_load_platform(
        'vacuum', DOMAIN, hass_config[DOMAIN], hass_config
    ))
    return True
