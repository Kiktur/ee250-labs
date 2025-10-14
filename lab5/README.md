# Lab 5

## Team Members
- 
- team member 2

## Lab Question Answers

Answer for Questions:

1. dBm measures how strong a signal is, using decibels relative to 1mW. It's on a logarithmic scale, so small differences like 3dB can either double or halve the signal power.
2. OS needs to be checked because each operating system uses different commands for measuring Wi-Fi signal strength. For example, Linux uses iwconfig to show the signal level. Windows uses netsh wlan show interfaces, which shows the signal quality percentage, and macOS uses wdutil info to display the signal strength in dBm.
3. subprocess.check_output lets python run a terminal command and also gets its results back. The output comes back in bytes, so we convert it to regular readable text. But when the command fails Python shows an error rather than giving us a result.
4. Re.search checks a line of text to see any matching patterns. It finds one, it returns them to be able to analyze. If it sees nothing matching, then it returns None.
5. A conversion in dBm is needed because Window shows Wi-Fi strength as a percentage rather than dBm. A formula is needed for the conversion so it can be easier to compare with other Operating systems.
6. Standard deviation shows how much the measurements vary from the average. Here we can see and compare the Wi-Fi strength between the rooms. This way, we can see which ones are steady or which ones have signals that change a lot.
7. A DataFrame is a way to store data in Python. The Data is stored in rows and columns, it is good to use because the data can be organized. This way, calculation and creating plots become easier.
8. Error bars show us how much the signal changes from the average. They are useful  because it tells us if the signal is steady and how reliable the measurements are.
9. From the measurements and plot, we observed signal strength being stronger when near the router/Raspberry Pi, and this weakened the further we moved away. For example, when we were outside of the lab space, as the door was the barrier, the readings were in the  -60 dBm range, and the further we were in the halfway it was -80dB. This showed that distance and obstacles reduce Wi-Fi signal strength since walls and doors block or absorb radio waves, causing weaker signals.
