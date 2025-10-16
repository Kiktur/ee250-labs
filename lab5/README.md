# Lab 5

## Team Members
Victor Gutierrez (USC ID: 9841169875)
Angie Vasquez (USC ID: 5537473368)


## Lab Question Answers

Answer for Questions:

Note on wifi measurements:
The router for the apartment is located near the bedroom, which is where the largest signal strength was measured. The hallway and bathroom are located near the bedroom, but the bathroom measurement was recorded with the door closed, leading to a lower signal strength than the hallway. The kitchen and living room are located the farthest from the router with no doors inbetween, but the kitchen is farther around a corner than the living room. This matches with the measurements, since the kitchen has the lowest recorded signal strength.

1. dBm measures how strong a signal is, using decibels relative to 1mW. It's on a logarithmic scale, so small differences like 3dB can either double or halve the signal power.
2. OS needs to be checked because each operating system uses different commands for measuring Wi-Fi signal strength. For example, Linux uses iwconfig to show the signal level. Windows uses netsh wlan show interfaces, which shows the signal quality percentage, and macOS uses wdutil info to display the signal strength in dBm.
3. subprocess.check_output lets python run a terminal command and also gets its results back. The output comes back in bytes, so we convert it to regular readable text. But when the command fails Python shows an error rather than giving us a result.
4. Re.search checks a line of text to see any matching patterns. It finds one, it returns them to be able to analyze. If it sees nothing matching, then it returns None.
5. A conversion in dBm is needed because Window shows Wi-Fi strength as a percentage rather than dBm. A formula is needed for the conversion so it can be easier to compare with other Operating systems.
6. Standard deviation shows how much the measurements vary from the average. Here we can see and compare the Wi-Fi strength between the rooms. This way, we can see which ones are steady or which ones have signals that change a lot.
7. A DataFrame is a way to store data in Python. The Data is stored in rows and columns, it is good to use because the data can be organized. This way, calculation and creating plots become easier.
8. Error bars show us how much the signal changes from the average. They are useful  because it tells us if the signal is steady and how reliable the measurements are.
9. From the measurements and plot, we observed signal strength being stronger when near the router/Raspberry Pi, and this weakened the further we moved away. For example, when we were outside of the lab space, as the door was the barrier, the readings were in the  -60 dBm range, and the further we were in the halfway it was -80dB. This showed that distance and obstacles reduce Wi-Fi signal strength since walls and doors block or absorb radio waves, causing weaker signals.

## Part 2 Questions
 After analyzing the data, students should answer the following:

1. How does distance affect TCP and UDP throughput?

Distance affects TCP and UDP throughput by decreasing them as the distance from the router increases.  

2. At what distance does significant packet loss occur for UDP? The significant packets losses happen around 15 meters, that's when the signal was weaker.

3. Why does UDP experience more packet loss than TCP?

UDP has more packet loss since it doesn't resend lost packets, and it doesn't know if there were lost packets. It kinda shouts the data out rather than TCP resending data.

4. What happens if we increase the UDP bandwidth (-b 100M)?

If the UDP bandwidth increases, the sender starts sending data fast for the network, so the packets would more likely get lost.

5. Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?

Yes, because on 5GHz the Wi-Fi is faster but has a shorter range; however, the 2.4GHz is slower and can travel farther, through walls too.
