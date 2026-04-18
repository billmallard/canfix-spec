# CAN-FIX Protocol Specification

**Status:** Open Source Specification — Creative Commons Licensed  
**Format:** Sphinx documentation source (builds to PDF and HTML)  
**Scope:** Experimental Amateur-Built (E-AB) Aircraft Avionics

---

## What This Is

This repository contains the **authoritative specification** for the CAN-FIX communication protocol — the CAN bus implementation of the Flight Information eXchange (FIX) protocol family. CAN-FIX defines how avionics nodes on an aircraft CAN network identify themselves, publish flight data parameters, and consume data from other nodes.

The specification is licensed under Creative Commons, meaning anyone can read, implement, modify, and distribute compliant devices without licensing fees or vendor lock-in.

## What CAN-FIX Defines

- **Parameter namespace:** Every flight data value (airspeed, altitude, heading, GPS position, engine temperatures, control surface positions, etc.) has a named identifier. Parameters are organized by type and support multiple simultaneous sources (e.g., two independent EGT sensors for two engines).
- **Frame structure:** How 11-bit CAN identifiers are allocated across parameter types, node IDs, and index bytes for multi-instance data.
- **Node types and device IDs:** Standard device type identifiers so nodes can announce their role on the network.
- **Multi-source design:** The protocol explicitly accommodates redundant nodes publishing the same parameter type using separate identifier ranges, avoiding CAN arbitration conflicts.
- **Data types:** float, int, bool, string with defined units and ranges per parameter.

## Parameter Coverage

The specification covers the full avionics parameter set for a modern aircraft:

| Domain | Example Parameters |
|---|---|
| Navigation | LAT, LONG, ALT, IAS, TAS, GS, heading, track |
| AHRS | Pitch, roll, yaw rate, accelerations |
| Engine (×2) | RPM, MAP, EGT (×N cylinders), CHT, oil temp/pressure, fuel flow |
| Control surfaces | Pitch, roll, yaw, flap, trim positions |
| Electrical | Bus voltage, current, alternator status |
| Fuel | Quantity (×N tanks), flow, pressure |
| COM/NAV radios | Active/standby frequencies |
| Systems | Gear position, door status, general annunciators |

## Repository Contents

| Path | Description |
|---|---|
| `src/canfix.json` | Machine-readable parameter definitions (primary reference) |
| `src/canfix.xml` | XML form of parameter definitions |
| `src/parameters.rst` | Human-readable parameter documentation source |
| `src/framedef.rst` | CAN frame format specification |
| `src/datatypes.rst` | Data type definitions |
| `src/physical.rst` | Physical layer requirements (wiring, termination, bit rate) |
| `src/requirements.rst` | Protocol requirements |
| `src/practices.rst` | Recommended implementation practices |

## Building the Documentation

Requires Python with Sphinx and supporting packages:

```bash
sudo pip install pyexcel pyexcel-ods sphinx
sudo apt install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texlive-xetex latexmk
cd src
make latexpdf   # builds PDF
make html       # builds HTML
```

## Important Disclaimer

> This specification is developed for Experimental Amateur-Built aircraft use only.  
> It is not FAA-approved avionics software or a certified communication standard.  
> All implementations are the builder's responsibility.
