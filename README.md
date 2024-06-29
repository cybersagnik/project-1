# Bypassing Snort Scan Rules

## Overview

This project demonstrates methods to bypass Snort scan rules. Snort is an open-source Network Intrusion Detection System (NIDS) capable of performing real-time traffic analysis and packet logging.
It can also be set as an Intrusion Prevention System (IPS) making it an essential component for network security. Understanding how attackers might bypass Snort's preconfigured detection rules can help
security professionals improve their defenses and can help hardening the default rules to strengthen snort's overall funcationality

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Lab Configuration](#labconfiguration)
- [Disclaimer](#disclaimer)

## Installation

### Prerequisites
- Python 3.x
- Snort (installed and configured as per Lab Configuration)
- Scapy (Python library for packet manipulation install the packages via the requirements.txt)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/cybersagnik/project-1.git
   cd project-1
   ```
2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
### Usage

### Basic Usage

To run the script and test bypassing snort rules:
1. Ensure Snort is running and monitoring the network
2. Execute the bypass script:
   ```sh
   python poc-snort-bypass.py
   ```
### Lab Configuration

1. Vbox Lab Setup . Attacking Machine : kali linux , Lubuntu running snort , and metasploitable as target machine [**Note: The network settings of all the machines is on host-only mode]
   ![Lab-Setup](/images/lab_setup.png)

2. During Installation snort asks for the network range which it will monitor .But if its not configured correctly we can edit it later in the conf file by changing the $HOME_NET variable entry
   ![Snort-Conf](/images/snort_config_home_net.png)

3. And Lastly run Snort in IDS mode and log the alert messages in the console
   ![snort-ids-mode](/images/snort-conf.png)
