# Bypassing Snort Scan Rules

## Overview

This project demonstrates methods to bypass Snort scan rules. Snort is an open-source Network Intrusion Detection System (NIDS) capable of performing real-time traffic analysis and packet logging.
It can also be set as an Intrusion Prevention System (IPS) making it an essential component for network security. Understanding how attackers might bypass Snort's preconfigured detection rules can help
security professionals improve their defenses and can help hardening the default rules to strengthen snort's overall funcationality

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Lab Configuration](#labconfig)
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
