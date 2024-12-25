# Modularius
 is an advanced security tool designed to monitor and analyze the dynamic loading of modules in Windows environments. By leveraging Event Tracing for Windows (ETW), Modularius identifies suspicious or vulnerable modules in real-time, empowering administrators and security professionals to detect potential threats before they can exploit the system.


# Key Features:

Real-time Monitoring: Continuously tracks module loading events, providing immediate alerts for suspicious or known vulnerable modules.

Vulnerability Detection: Flags modules that match predefined known vulnerabilities (e.g., outdated drivers or compromised DLLs).

Suspicious Path Detection: Identifies modules loaded from untrusted or unexpected paths, providing early warnings of potential attacks.

Comprehensive Logging: Records detailed logs of all detected events, offering a full audit trail for security investigations.

System Protection: By detecting malicious modules early, ModTector enhances the security posture of your system, reducing the risk of exploitation through module-based attacks.

Whether you're safeguarding a critical server or monitoring a user workstation, ModTector acts as your first line of defense, providing proactive protection against the growing threat of module-based vulnerabilities.

Protect your system. Detect malicious modules with ModTector.


# How to Download and Set Up Modularius
Modularius is an easy-to-use, real-time security tool for detecting suspicious and vulnerable modules in Windows environments. Follow these simple steps to download and get started:

# 1. Download Modularius
To get the latest version of Modularius, follow these steps:

Visit the official Modularius GitHub repository at:
https://github.com/ahmedkhalifa8474/modularius

Click on the Releases section.

Download the latest Modularius.zip file for your Windows version.

# 2. Extract the Files
Once the download is complete:

Navigate to the folder where you downloaded the file.

Right-click on the Modularius.zip file and select Extract All.

Choose a destination folder to extract the contents.

# 3. Install Dependencies (if any)
Modularius requires some dependencies to function properly:

Make sure you have Python 3.x installed on your system. You can download it from https://www.python.org/downloads/.

Install any required Python libraries. In the extracted folder, open a command prompt and run:

pip install -r requirements.txt

# 4. Launch Modularius
Once you've extracted the files and installed dependencies:

Open a command prompt as Administrator (this may be necessary for accessing event logs).

Navigate to the folder where Modularius was extracted using the cd command:

cd C:\path\to\Modularius

Run the tool by executing:

# python modularius.py

# 5. Monitor and Protect

Once Modularius is running, it will automatically begin monitoring module loading events and display alerts in real-time. You will also find detailed logs saved in the byol_detector.log file within the same folder.

Additional Notes:

Modularius is designed to work on Windows 7 and later.

# Make sure you run the tool with administrative privileges to capture and monitor system events.

![image](https://github.com/user-attachments/assets/d6ddd361-01f4-4f8a-abc6-e7819fbfc241)


