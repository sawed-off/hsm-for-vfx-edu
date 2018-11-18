# hsm-for-vfx-edu

Hello and welcome!

This is an opensource project for people to learn production management for vfx and gamedev with a complete set of free digital assets including characters and environments.

---

Another goal is to provide some automation so that any school can follow these steps to start using the Maya Hyperspace Madness project data together with a starter Shotgun project that leverages that data.

See https://area.autodesk.com/hyperspacemadness/ for more information about the Hyperspace Madness project, license, etc.

See https://shotgunsoftware.com/ for more information about Shotgun Software.

For developers, this playlist is an introduction to the Shotgun Ecosystem: https://www.youtube.com/watch?v=QP44cM51aEY&list=PLEOzU2tEw33r4yfX7_WD7anyKrsDpQY2d

See http://developer.shotgunsoftware.com/rest-api/ about how to access and use the REST API.

---
These are now three example files that log the manual actions for the first attempt of making things more procedural and automatic:

[get_data.sh](/get_data.sh)  is the log of manual commands as per the header in that file.

[Shotgun...json](/Shotgun-REST-API-v1-for-HSM.postman_collection.json) is exported from Postman as I am trying to use the REST API for this exercise to learn it.

*NEW* [create_hsm-edu.py](/create_hsm-edu.py) is a Python script that creates the Project and Assets in a Shotgun site.
