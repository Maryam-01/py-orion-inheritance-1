# 🛰️ Sprint: Sensor Hierarchy at Orion 7

_Inheritance, Composition & Polymorphism_

## Orion 7 Recap

You have worked with Orion 7 before. They are an independent space agency, privately funded, scientifically rigorous, with a startup energy. They run satellites, crewed missions, and uncrewed probes. They employ around 400 people. The software team builds the tools that hold all of that together.

### The Team

**Commander Yara Osei**: Director of Mission Operations.

**Felix Ramos**: Lead Software Engineer.

**Dr. Anika Sørensen**: Data Scientist.

## About the Sensor Library

## The Brief

Felix has raised a ticket. The sensor library is in good shape for the satellite fleet and the orbital lab. But the Rover mission needs some additional sensors, the navigation system uses a composite sensor that combines two distance readings into a single position. Meanwhile, a new requirement has arrived from the ground station team: some sensors need calibration (offset and scale correction), some need output smoothing (a moving average), some need both, and some need neither.

Felix has left a note in the ticket:

> _"Before you start, get familiar with what's already there. The existing sensors share a pattern and you'll want to understand it. Once you've added the new sensors, we can talk about the calibrations and rover. Tests are expected throughout. Decisions go in NOTES.md."_

## Project Structure

The starter looks like this. You will add to it as the day progresses.

```
sensors/
│
├── src/
│   ├── sensor.py
│   ├── temperature_sensor.py
│   ├── heading_sensor.py
│   └── battery_sensor.py
│
├── tests/
│   ├── test_sensor.py
│   └── test_sensor_subclasses.py
│
├── NOTES.md
└── README.md
```
