"""Event Scheduler Integration"""
import json
from typing import Any
from datetime import datetime, timezone
from homeassistant.core import Config, HomeAssistant, ServiceCall

DOMAIN = "event_scheduler"


def setup(hass: HomeAssistant, config: Config):
    def upsert_scheduled_event(call: ServiceCall):
        params: dict[str, Any] = dict(call.data)
        event_id = f"{DOMAIN}.{params.pop('id')}"
        hass.states.set(event_id, params.pop('trigger_time'), params)

    def remove_scheduled_event(call: ServiceCall):
        event_id = f"{DOMAIN}.{call.data['id']}"
        hass.states.remove(event_id)

    def fire_events(call: ServiceCall):
        # store the events before we start removing them
        events = hass.states.all(DOMAIN)

        for event in events:
            if datetime.fromisoformat(event.state) <= datetime.now(timezone.utc):
                # remove from scheduled events
                hass.states.remove(event.entity_id)

                # fire event
                hass.bus.fire(event.attributes['channel'], event.attributes['data'])



    hass.services.register(DOMAIN, "upsert_scheduled_event", upsert_scheduled_event)
    hass.services.register(DOMAIN, "remove_scheduled_event", remove_scheduled_event)
    hass.services.register(DOMAIN, "fire_events", fire_events)

    # Return boolean to indicate that initialization was successful.
    return True
