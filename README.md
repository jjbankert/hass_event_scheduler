# Event Scheduler Integration

This integration allows Home Assistent events to be scheduled for future delivery. For example, if you have an automation that listens to `reminder` events, you could schedule an event to trigger that automation in the future. This is more flexible than a fixed time trigger, or even a time pattern.

The Event Scheduler integration offers 3 services:

- `event_scheduler.upsert_event`: Add or Update an event to be fired at a specific time.
- `event_scheduler.remove_event`: Remove a scheduled event.
- `event_scheduler.fire_events`: Fire the events that were scheduled at or before the current time.
