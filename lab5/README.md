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
9. From the plot, the signal strength was strongest near the bedroom where the router is located, and it became weaker in the areas farther away, such as the kitchen and livingroom. The bathroom also had a lower signal since the measurement was taken with the door closed, which likely blocked part of the signal. The weaker signal in certain locations is caused by distance from the router and obstacles like the walls,doors,and corners that absorb or reflect the Wi-Fi signal. Ultimately, this matches the results; the stronger signal areas had higher and more stable TCP/UDP speeds, while the weaker areas showed slower and less consistent performance. 

## Part 2 Questions
 After analyzing the data, students should answer the following:

1. How does distance affect TCP and UDP throughput?

Distance affects TCP and UDP throughput by decreasing them as the distance from the router increases. At 12m the speeds were highest and most stable, while at 15m and 20m they dropped and became less consistent. TCP stayed faster overall but UDP seemed to be more affected by distance and packet loss.

2. At what distance does significant packet loss occur for UDP? Significant packets losses happen around 15 meters, that's when the signal was weaker. The thoughput droppsed close to 0Mbps in some runs after being stable in the 12m test.

3. Why does UDP experience more packet loss than TCP?

UDP has more packet loss since it doesn't resend lost packets, and it doesn't know if there were lost packets. It kinda shouts the data out rather than TCP resending data. In our expirement weaker Wi-Fi spots like the bathroom with the door closed and the kitchen father from the router coused more packet loss, as we saw a lower thoughout seen in those locations.

4. What happens if we increase the UDP bandwidth (-b 100M)?

If the UDP bandwidth increases, the sender starts sending data faster to the network, so the packets are more likely to get lost. In our testing, the throughput would be more unstable, and the packetloss percentage would rise significantly as the router struggles to keep up with the higher send rate.

5. Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?

Yes, because 5GHz Wi-Fi is faster but has a shorter range,while 2.4GHz is slower and can travel farther and pass though walls better. In our experiment, 5GHz would likely give us higher throughput at short distances, but performance would drop off more quickly as we moved farther from the router.
