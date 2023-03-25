"""Event Scheduler Integration"""
from datetime import datetime, timezone
from typing import Any

from homeassistant.core import Config, HomeAssistant, ServiceCall

DOMAIN = "event_scheduler"


def setup(hass: HomeAssistant, config: Config):
    def upsert_event(call: ServiceCall):
        params: dict[str, Any] = dict(call.data)
        event_id = f"{DOMAIN}.{params.pop('id')}"
        hass.states.set(event_id, params.pop("time"), params)

    def remove_event(call: ServiceCall):
        event_id = f"{DOMAIN}.{call.data['id']}"
        hass.states.remove(event_id)

    def fire_events(call: ServiceCall):
        # get all scheduled events
        events = hass.states.all(DOMAIN)

        for event in events:
            # find the events that should be fired now
            if datetime.fromisoformat(event.state) <= datetime.now(timezone.utc):
                # Remove from scheduled events first. This ensures that a triggered event
                # can schedule a new event with the same id without fear of race conditions.
                # It can be a potential issue if the hass.bus.fire fails for some reason.
                hass.states.remove(event.entity_id)

                # fire event
                hass.bus.fire(event.attributes["type"], event.attributes["data"])

    hass.services.register(DOMAIN, "upsert_event", upsert_event)
    hass.services.register(DOMAIN, "remove_event", remove_event)
    hass.services.register(DOMAIN, "fire_events", fire_events)

    # Return boolean to indicate that initialization was successful.
    return True
