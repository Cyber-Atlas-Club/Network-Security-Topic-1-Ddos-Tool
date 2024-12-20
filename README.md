# Network Security - Topic 1 - DDoS Tool

This repository contains a simple Distributed Denial of Service (DDoS) tool created in Python. It simulates a DDoS attack by sending continuous HTTP GET requests to a target server using multiple threads. This tool is intended purely for educational purposes as part of the **Cyber Atlas Club**’s learning series.

**Important:** This tool should **only** be used on servers you own or have explicit permission to test. **Misuse of this tool is illegal** and **Cyber Atlas Club is not responsible for any damage or consequences caused by this tool.**

## Overview

This Python script simulates a DDoS attack by creating multiple threads to send HTTP GET requests to a target URL. The tool will continuously send requests until you decide to stop it. After sending 1000 requests, the script will ask whether to continue or stop the attack.

### Features:
- **Simulate multiple concurrent threads** to perform the attack.
- Track and display the HTTP status code for each request sent.

## Requirements

Make sure Python 3.x is installed on your system along with the necessary library:

### Install dependencies:
```bash
pip install requests
```
