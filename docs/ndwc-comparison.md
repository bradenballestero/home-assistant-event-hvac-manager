# Comparison with the NDWC installation

The live system inspected on October 29, 2026 has five dedicated zone managers, mode-application scripts, timers, expiry helpers, dashboard controls, and warning automations. The portable blueprints are an independent extraction; they have not been run through the same field testing.

| Behavior | Live installation | Portable project |
| --- | --- | --- |
| Decision priority | Admin, hold, blockers, unavailable calendar, event, Eco override, manual, schedule, Eco | Same ordering; optional occupancy is evaluated before schedule |
| Control response | Watches specific helpers and timers, plus 15-minute cadence | Watches entities selected by the user, plus configurable cadence |
| Thermostat application | Per thermostat; Youth Wing is cool-only | Per thermostat; choose dual-setpoint or cool-only per zone |
| Setpoints | Dashboard input-number helpers | Optional input-number helpers for cool targets; fixed low targets |
| Temporary controls | Scripts, timers, timestamps and cleanup within managers | Optional timer script and expiry automation; fixed duration per script |
| Fan and schedule | Dashboard-editable helpers | Optional fan and start/end time helpers |
| Other controls | Duration selector sync, admin-lock warnings, building-wide scripts | Not included |
| Occupancy | Temporarily disabled in Sanctuary | Optional sensor; omit it to match current Sanctuary behavior |

The church's Sanctuary script also clamps some cool setpoints to local limits; the reusable blueprint does not reproduce those site-specific clamps. Verify equipment limits and automation inputs. Mode and reason represent the chosen decision, not confirmation of device state. See automation and script traces for errors.
