# SKILL LAB PRATICAL HACKATHON

## Final Project README

> **Project Weight:** 100%  
> **Team Size:** 4/3 students  
> **Project Duration:** 16 hours  
> **Total Time Available:** 32 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository

After forking this repository, rename it using the format:

`SKILLLAB_PROR-2026-TeamName`

### Example

`SKILLLAB_PROR-2026-AuroWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the build period.  
By the final review, this README should clearly show:

- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules

- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 SENTRI


## 1.2 Team Members

| Name                  | Primary Role                    | Secondary Role   | Strengths Brought to the Project |
| --------------        | ------------------------------- | --------------   | -------------------------------- |
| `Hrishikesh Pandit` | `[ Coding  ]` | `Documentation`  | `Documentation,  `|
| `Soham Pednekar`        | `[Electronics / Fabrication]`   | `[Coding]`       | `Material Handling, Hardware`    |
| `Shaunak Karambelkar`        | `[Electronics / Fabrication]`   | `[Coding]`       | `Material Handling, Hardware`    |
| `Muskan Jaiswal`        | `[Electronics / Fabrication]`   | `[Coding]`       | `Material Handling, Hardware`    |

## 1.3 SafeDrive System


`(because Project-or)`

<img width="1600" height="1131" alt="image" src="https://github.com/user-attachments/assets/c64bfbd4-b3b7-43d9-83ad-c203a5aa11bc" />

## 1.4 One-Line Pitch

SafeDrive System is an edge-computing safety node that fuses real-time cabin air quality and vehicle dynamics to instantly alert drivers of drowsiness risks or dangerous driving behaviors before accidents happen.

## 1.5 Expanded Project Idea

 
SafeDrive System is an edge-computing active safety monitor designed for vehicles that correlates environmental stressors with kinetic data to prevent accidents. For the driver and passengers, it creates a seamless, preventative safety experience by providing instant, real-time interventions. Instead of passively recording data, the system actively tracks cabin life-support conditions and immediately alerts the driver to severe $CO_2$ buildup or extreme heat that causes drowsiness, while simultaneously warning them of erratic driving behaviors like harsh braking or sudden impacts.


Technologically, the project is powered by a Raspberry Pi 4B acting as a local edge-processing hub to fuse multi-sensor data without requiring a cloud connection. The hardware stack integrates an MQ135 air quality sensor (interfaced safely to the Pi via a custom 10k/20k hardware voltage divider) and a DHT11 sensor for environmental monitoring, paired with an I2C-based MPU6050 6-DOF accelerometer for kinetic tracking. The system's logic is driven by Python and the Adafruit CircuitPython ecosystem, allowing the node to execute complex safety algorithms and trigger visual alerts in milliseconds.

---

# 2. Inspiration

## 2.1 References

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You                                                                         |
| ----------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Research Paper | `Real-Time Machine Learning-Based Driver Drowsiness Detection Using Visual Features` https://www.mdpi.com/2313-433X/9/5/91 | Inspired by the research on real-time drowsiness detection, I aimed to develop a preventative system that monitors the atmospheric and kinetic root causes of fatigue—such as $CO_2$ buildup and heat—rather than just the visual symptoms. |
|             |                                                                     |                                                                                           |
|             |                                                                     |                                                                                           |

## 2.2 Original Twist

While traditional vehicle safety systems (like OBD-II scanners or dashcams) are purely reactive—recording data after a mechanical failure or crash has already occurred—SafeDrive System is completely predictive and proactive.

Our originality lies in shifting the focus from the machine's health to the driver's physiological state, using a lean edge-computing architecture.

Here is what sets this project apart:

1) Multi-Domain Sensor Fusion: We successfully bridged two completely different domains of data. By combining Environmental Life-Support metrics (Gas/Air Quality and Temperature) with Kinetic Physics (G-force and acceleration), the system doesn't just know how the car is moving; it understands the conditions causing the driver to move that way.
2) Predictive Fatigue Modeling: Instead of using complex, expensive computer vision cameras to check if a driver's eyes are closing, we tackle the root cause of the drowsiness. By monitoring $CO_2$ buildup and heat stress, the system warns the driver to ventilate the cabin before the cognitive decline and microsleeps occur.
3) 100% Edge-Processed & Zero Latency: In a life-safety application, milliseconds matter. By keeping all data processing strictly local on the Raspberry Pi 4B, we eliminated the need for cloud computing, Wi-Fi dependency, or database logging. The system provides instantaneous visual interventions with zero network latency.
4) Scalable, Low-Overhead Architecture: Instead of relying on expensive, proprietary automotive diagnostic tools, we utilized accessible components integrated via custom signal-conditioning circuits. This proves the system can be mass-deployed across an entire commercial fleet at a fraction of the cost of traditional telematics, democratizing vehicle safety.  


---

# 3. Project Intent

## 3.1 User Journey 

Imagine Ashutosh, a driver embarking on a long evening commute after a tiring workday. As Ashutosh starts the car, the SafeDrive System—discreetly mounted on the dashboard—silently springs to life, its sensors immediately beginning to scan the cabin's "vitals."Halfway through the journey, the car windows are rolled up against the cold air, and the heater is humming. Ashutosh doesn't notice that the $CO_2$ levels are steadily rising and the cabin temperature has hit a stuffy 28°C. His eyes begin to feel heavy, a classic sign of early-stage drowsiness. Before Ashutosh even realizes he is at risk, the system's edge-processor correlates the air quality spike with the rising heat. Suddenly, a bright "DANGER: VENTILATE CABIN" alert flashes on the dashboard interface. Startled back into focus, Ashutosh rolls down the window, breathes in the fresh air, and feels instantly more alert.

A few miles later, a distracted driver suddenly cuts into Ashutosh’s lane. Ashutosh reacts quickly, slamming on the brakes. The MPU6050 sensor detects the violent deceleration and the sudden spike in G-force. Even before the car has come to a complete halt, the system displays a "CRITICAL: HARSH BRAKING DETECTED" alert. This immediate feedback serves as a digital co-pilot, helping Alex remain aware of his driving dynamics and the cabin environment. Ashutosh reaches his destination safely, guided by a system that watched for the dangers he couldn't see.

                                                  |



---

# 4. Definition of Success

## 4.1 Definition of “Usable”

A "usable" version of the SafeDrive System is defined by its ability to operate as a passive, non-distracting co-pilot that provides high-confidence alerts. To meet this standard, the system must achieve:

Glanceable UI: The output must be color-coded (Green/Yellow/Red) so the driver can understand the safety status in under 0.5 seconds without taking their eyes off the road for too long.

Zero-Latency Intervention: The time between a sensor detecting a threshold breach (like a sudden 2G impact or a gas spike) and the visual alert appearing must be less than 200ms.

Zero-Touch Operation: Once the vehicle starts, the system must initialize and begin monitoring automatically without requiring any manual calibration or user input.


## 4.2 Minimum Usable Version

The Minimum Usable Version (MVP) is the smallest functional iteration that demonstrates "Multi-Domain Sensor Fusion." This includes:

Core Hardware: Raspberry Pi 4B integrated with the MQ135 (via voltage divider) and the MPU6050.

Primary Logic: A single Python script that reads the Digital Output of the gas sensor and the Acceleration Magnitude of the MPU6050.

Basic Alert System: A terminal-based or simple HTML dashboard that toggles between "Safe" and "Warning" based on those two inputs.

Power Stability: The system must be able to run off a standard 5V USB car charger/power bank without crashing.

## 4.3 Stretch Features

While the core system focuses on real-time alerts, the following features would elevate the project from a prototype to a consumer-ready product:

Auditory Alarms: Integration of a piezo buzzer to provide distinct "Beep" patterns for different threats (e.g., a long tone for toxic air, rapid pulses for harsh braking).

Night Mode UI: An interface that automatically dims or switches to red-light tones during night-time driving to preserve the driver's night vision.

Cloud-Sync Dashboard: A secondary Flask-based web interface that allows a passenger or remote fleet manager to view the vehicle's "vitals" over a local Wi-Fi or 4G hotspot.

Historical Incident Snapshots: Capturing a 5-second "data snapshot" of all sensor values leading up to a harsh braking event to help the driver review their behavior later.


---

# 5. System Overview

## 5.1 Project Type

Check all that apply.

- [x] Electronics-based

- [ ] Mechanical

- [x] Sensor-based

- [ ] App-connected

- [x] Motorized

- [ ] Sound-based

- [ ] Light-based

- [ ] Screen/UI-based

- [ ] Fabricated structure

- [ ] Game logic based

- [x] Installation

- [ ] Other:

## 5.2 High-Level System Description

The SafeDrive System functions as an intelligent co-pilot that monitors the "health" of the vehicle's interior environment and the safety of its movement.

Input: The system continuously gathers data from three specialized sensors: the MQ135 (detecting $CO_2$, smoke, and alcohol vapors), the DHT11 (measuring cabin temperature and humidity), and the MPU6050 (tracking G-forces and sudden impacts).

Processing: All data is fed into a Raspberry Pi 4B. The Pi runs a Python-based processing engine that uses "game logic" to treat the vehicle's safety like a status bar. It filters the noise, compensates for environmental shifts, and determines if the current conditions cross the safety thresholds.

Output: The system provides immediate feedback through a Screen/UI-based dashboard and Light-based indicators (color-coded alerts). Additionally, it triggers a Motorized component (such as a cooling fan simulation) to provide physical feedback when danger is detected.

Physical Structure: The components are housed in a fabricated enclosure designed to be mounted on a standard vehicle dashboard, ensuring sensors are positioned for optimal airflow and movement detection.

App Interaction: The system hosts a local web server, allowing passengers or drivers to view a real-time App-connected dashboard on their mobile devices via Wi-Fi to monitor cabin "vitals" and history.

## 5.3 Input / Output Map

| System Part | Type | What It Does |
| :--- | :--- | :--- |
| **MQ135 Gas Sensor** | **Input** | Detects $CO_2$ levels and toxic vapors to identify air quality risks. |
| **MPU6050 Accelerometer** | **Input** | Measures kinetic forces to detect harsh braking or physical impacts. |
| **DHT11 Sensor** | **Input** | Monitors cabin temperature to prevent heat-related driver fatigue. |
| **Raspberry Pi 4B** | **Processor** | The central brain that fuses sensor data and executes safety logic. |
| **Web Dashboard / LCD** | **Output** | Displays real-time safety status and color-coded warnings (Green/Red). |
| **LED Indicators** | **Output** | Provides high-visibility light alerts when thresholds are breached. |
| **Haptic Motor / Actuator** | **Output** | Provides physical (motorized) feedback/vibration to alert a drowsy driver. |
| **Fabricated Enclosure** | **Structure** | Protects the electronics and secures the sensors for accurate readings. |---

# 6. System Design, Sketches and Visual Planning 

## 6.1 Concept Architecture/sketch/schematic

Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:

```md

```



## 6.2 Labeled Build Sketch/architecture/flow diagram/algorithm

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/95637f31-b4e7-4427-a9e1-4b63fbeb0ac5" />

## 6.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `16 cm` |
| Width            | `16 cm` |
| Height           | `8 cm`  |
| Estimated weight | `400 g` |

---

# 7. Electronics Planning

## 7.1 Electronics Used

| Component                 | Quantity | Purpose                               |
| ------------------------- | --------:| ------------------------------------- |
| `[Raspi/FPGA]`                 | `1`      | `[Main controller]`                   |
| `[L298N Motor Driver]`    | `1`      | `[Control Motors]`                    |
| `[BO Motors]`             | `2`      | `[Rotate wheels]`                     |
| `[Buck Converter]`        | `1`      | `[Power ESP32]`                       |
| `[Li Ion Battery Pack]`   | `2`      | `[Power]`                             |
| `[Projector]`             | `1`      | `[Display obstacles]`                 |
| `Camera (Webcam / Phone)` | `1`      | `[Tracks car position using markers]` |

## 7.2 Wiring Plan

Describe the main electrical connections.

**sample Response:**  
`The RASPI is connected to the motor driver (L298N) using four GPIO pins (18,19; 22,23) to control motor direction (IN1, IN2, IN3, IN4). Two PWM-capable pins (ENA and ENB; 25 and 26) are connected to control the speed of each motor.

The motors are connected to the output terminals of the motor driver. The motor driver is powered directly by the battery pack (higher voltage), while the ESP32 receives regulated 5V from the buck converter.

All components share a common ground to ensure stable operation. The projector and camera are connected to the laptop, which handles tracking and game logic separately.`

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `Battery (Li-ion pack)`                                                                                                                           |
| Voltage required | `~6–8.4V for motors (via driver), stepped down to 5V for ESP32 (buck converter)`                                                                  |
| Current concerns | `Motors can draw high current under load, which may cause voltage drops affecting ESP32 and WiFi stability`                                       |
| Safety concerns  | `Avoid over-discharging Li-ion batteries, ensure proper voltage regulation, prevent short circuits, and secure wiring to avoid loose connections` |

---

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| `[MicroPython]`                | `Control ESP32`                                |
| `[Python/PyGame/OpenCV]`       | `Track markers, game logic, create projection` |
| `[Fusion/Blender/Illustrator]` | `[Prototyping structure]`                      |
|                                |                                                |

## 8.2 Software Logic/Algorithm

Describe what the code must do.

Include:

- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`

- **Sample Startup behavior:**  
  The Raspi/FPGA initializes motor pins, PWM control, and starts a WiFi access point with a web server. The laptop initializes camera input, tracking system, and projection mapping.
- **Input handling:**  
  Movement commands are received from the laptop (pygame sends http requests)
- **Sensor reading:**  
  The camera continuously captures frames, and OpenCV detects ArUco markers to determine the car’s position and orientation.
- **Decision logic:**  
  The system maps the car’s position into a virtual coordinate system and checks for nearby obstacles or collisions. If movement is valid, the command is allowed; if not, it is blocked or replaced with a feedback action (like a slight shake).
- **Output behavior:**  
  The ESP32 drives the motors using PWM signals to control speed and direction. The projector displays the updated game environment, including obstacles, targets, and feedback visuals.
- **Communication logic:**  
  The laptop sends HTTP requests (e.g., `/forward`, `/left`) to the ESP32 over WiFi. The ESP32 parses these commands and executes motor actions.
- **Reset behavior:**  
  If no command is received within a short timeout, the ESP32 stops the motors. The game resets when a level is completed or restarted.`

## 8.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="" />
<img width="1600" height="1200" alt="image" src="" />




# 9. Bill of Materials

## 9.1 Full BOM

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| `[RASPI]`                        | `1`      | `Yes`   | `No`         | `0`            | `38 Pin ESP32`                | `[To control components]` |
| `[Motor Driver]`                 | `[1]`    | `[Yes]` | `[No]`       | `0`            | `[LN296]`                     | `[To drive both motors]`  |
| `[DC Motors and wheel]`          | `[2]`    | `[No]`  | `[Yes]`      | `[150]`        | `[BO Motors and 6 cm wheels]` | `[high torque motors]`    |
| `[Buck Converter]`               | `[1]`    | `[No]`  | `[Yes]`      | `[75]`         |                               |                           |
| `[Li-ion batteries with holder]` | `[1]`    | `[No]`  | `[Yes]`      | `[200]`        |                               |                           |

## 9.2 Material Justification

Explain why you selected your main materials and components.

**Response:**  
`DC motors (BO motors) were chosen instead of servos or steppers because the system requires continuous rotation for movement rather than precise angular control (Previously, we were considering using steppers as we were planning on tracking movement on the ESP using its relative position from an origin, but since we're using a camera now, this is not required). A motor driver (L298N) was used to allow bidirectional control and speed variation using PWM.`


## 9.3 Items You chose

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| `BO Motors + Wheels` | `Drive system for car`   | `robu.in`     | `15th April`                | `[Received]` |
| `Buck Converter`     | `Stable power for ESP32` | `local store` | `before testing`            | `[Received]` |
| `Li-ion Batteries`   | `Portable power`         | `local store` | `before testing`            | `Recieved`   |

## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Electronics           | `[400]`                     |
| Mechanical parts      | `[200]`                     |
| Fabrication materials | `[0 (Available on campus)]` |
| Purchased extras      | `[0]`                       |
| Contingency           | `[300]`                     |
| **Total**             | `[900]`                     |

## 9.5 Budget Reflection

If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  

---

# 10. Planning the Work

## 10.1 Team Working Agreement

Write how your team will work together.

Include:

- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  


## 10.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      | `[Finalize concept]`    | `[Both]` | `2`             | `1st April`  | `None`     | `Done` |


## 10.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | ----------     | ------------- |
| Concept              | `[Mrugendra]`  | `[Jyoti]`     |
| Electronics          | `[]`           | `[]`          |
| Coding               | `[]`           | `[]`          |
| Mechanical build     | `[]`           | `[]`          |
| Testing              | `[]`           | `[]`          |
| Documentation        | `[]`           | `[]`          |

---

# 11 hour Milestones

## 11.1 8-hour Plan(tentetively you may set)

### Bi Hour 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Bi Hour 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Bi Hour 3 — Integrate

Expected outcomes:

- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Bi Hour 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 12.2  Update Log

| Days   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
| Day 1 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 2 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 3 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 4 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |

---

# 13. Risks and Unknowns

## 13.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
| WiFi connection between laptop and ESP32 becomes unstable       | `Technical`  | `Medium`   | `High`   | Keep ESP32 close, ensure stable power supply, reduce network load, add fail-safe stop | `[Gopal]`           |


## 13.2 Biggest Unknown Right Now

What is the single biggest uncertainty in your project at this stage?

**Response:**  


---

# 14. Testing 

## 14.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `[Wifi connection]`    | `[Check if motor spins via app button]`                                              | `[Both motors accurately respond to wifi signals]`                                                   |
                       |
## 14.2 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
| `18th April`  | `Car not balancing properly`          | `Mechanical` | `Add low-friction caster support to one side` | `Worked`             | `improve caster structure`                     |


## 14.3 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Gopal` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |


---

# 15. Build Documentation

## 15.1 Fabrication Process(if any)

Describe how the project was physically made.

Include:

- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 16 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />





# 17. Final Outcome

## 17.1 Final Description

Describe the final version of your project.

**Response:**  


## 17.2 What Works Well



## 17.3 What Still Needs Improvement


## 17.4 What Changed From the Original Plan

How did the project change from the initial idea?

**Response:**  


---

# 18. Reflection

## 18.1 Team Reflection

What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  


## 18.2 Technical Reflection

What did you learn about:

- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  


## 18.3 Design Reflection

What did you learn about:

- designing ,
- delight,
- clarity,
- physical interaction,
- understanding,
- iteration?

**Response:**  


## 18.4 If You Had One More hour

What would you improve next?

**Response:**  

` `

---

# 19. Final Submission Checklist

Before submission, confirm that:

- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written
<img width="1131" height="1600" alt="image" src="" />

---


---


