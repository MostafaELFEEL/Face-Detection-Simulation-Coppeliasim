# Face-Detection-Simulation-Coppeliasim

## Overview

This project demonstrates real-time face detection using CoppeliaSim. We employ computer vision techniques to detect human faces, showcasing its applicability in robotics and AI-driven systems.

## Features

- **Real-time Face Detection:** Utilize the simulation environment of CoppeliaSim to detect human faces in a simulated environment.
- **Integration with ROS2:** Seamlessly integrate face detection algorithms with Robot Operating System (ROS2) for enhanced robotic applications.
- **Visual Representation:** Visualize the face detection process through CoppeliaSim's graphical user interface, providing insights into the detection mechanisms.

## Setup and Execution

### Prerequisites

- Download [Coppeliasim edu v.4.5.1](https://www.coppeliarobotics.com/files/V4_5_1_rev4/CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu22_04.tar.xz).

### Installation
1. Clone this repository:
```bash
mkdir ros2_ws && cd ros2_ws
https://github.com/MostafaELFEEL/Face-Detection-Simulation-Coppeliasim.git
colcon build
```

### Running the Simulation

1. Open CoppeliaSim:
```bash
cd ~/<Path_to_Coppeliasim_Folder> && ./coppeliaSim.sh
```
Make sure to change **<Path_to_Coppeliasim_Folder>** with Coppeliasim folder path.

2. Execute the Python script for face detection:

```bash
cd ~/ros2_ws && ros2 run face_detection face_detection
```

## Results:

![image](https://github.com/MostafaELFEEL/Face-Detection-Simulation-Coppeliasim/assets/106331831/0a4e287a-362b-4202-828c-537a7febc472)


