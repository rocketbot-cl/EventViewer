



# Windows Event Viewer
  
Module to read and filter records from the Windows Event Viewer.  

*Read this in other languages: [English](Manual_EventViewer.md), [Português](Manual_EventViewer.pr.md), [Español](Manual_EventViewer.es.md)*
  
![banner](imgs/BANNEREVENTVIEWER.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to Use This Module
This module allows you to read and filter entries from the Windows Event Viewer.

1. **Log:** Select the Windows log you want to view. Note that accessing the **Security** log may require administrator permissions.

2. **Source:** Allows you to filter events by source name (for example, `UserModePowerService`).

3. **Event ID:** Allows you to filter entries by event ID.

4. **Event Type:** Select the event type you want to include in the results.

5. **From:** Sets the start date and time to include events generated from that point onward.

6. **To:** Sets the end date and time to include events generated up to that point.

7. **Filtered by message:** The value entered must exactly match the name of the event source (*Source*, for example, `UserModePowerService`) or a specific error code included in the event’s general description. This filter does not support keyword searches or partial text matches.

8. **Maximum records to review:** Specifies the maximum 
number of records to be queried, starting with the most recent ones. By default, 1,000 records are reviewed.


## Description of the commands

### Get Windows events
  
Read and filter Windows event log records.
|Parameters|Description|example|
| --- | --- | --- |
|Log name|Select the Windows event log to read. Security may require administrator permissions.|Select log|
|Source contains|Filter events whose source name contains this text.|Optional|
|Event ID|Filter by an exact event ID.|Optional|
|Event type|Select the event type to include in the results.|Select event type|
|From (DD/MM/YYYY HHmmss)|Include events generated at or after this date and time.|14/10/2026 10:57:15|
|To (DD/MM/YYYY HHmmss)|Include events generated at or before this date and time.|14/10/2026 10:57:15|
|Message filter|Filter events by source or specific error code.|Optional|
|Maximum records to inspect|Maximum number of records to inspect, starting with the newest. Defaults to 1000.|1000|
|Assign result to variable|Variable where the event log results will be stored.|event_logs|
