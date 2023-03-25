# Event Scheduler Integration

This integration allows Home Assistent events to be scheduled for future delivery. For example, if you have an automation that listens to `reminder` events, you could schedule an event to trigger that automation in the future. This is more flexible than a fixed time trigger, or even a time pattern.

## Use
The Event Scheduler integration offers 3 services:

- `event_scheduler.upsert_event`: Add or Update an event to be fired at a specific time.
- `event_scheduler.remove_event`: Remove a scheduled event.
- `event_scheduler.fire_events`: Fire the events that were scheduled at or before the current time.

The documentation for the fields in each service can most easily be viewed through the developer tools -> services UI. Specifically you can view the description in the GUI view and the fields documentation in the YAML view (HA quirk).

I suggest an automation that calls `event_scheduler.fire_events` every minute (which is good enough for my use cases).

## Install
You can most easily install the integration through HACS if you add it as a custom repository (3 dots in the top right corner -> custom repositories).

Alternatively you can copy the (`custom_component/`)`event_scheduler` folder to your `config/custom_components` folder.

https://github.com/jjbankert/hass_event_scheduler
