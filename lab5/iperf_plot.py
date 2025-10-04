import csv
import matplotlib.pyplot as plt
tcp_data = []
with open('iperf_tcp_2m.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    second_row = next(csv_reader)
    print(second_row)
    tcp_data = second_row[1].split(" ")

udp_data = []
with open('iperf_udp_2m.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    second_row = next(csv_reader)
    print(second_row)
    udp_data = second_row[1].split(" ")

tcp_data.pop(0)
udp_data.pop(0)

print(f"TCP data: {tcp_data}")
print(f"UDP data: {udp_data}")

with open('iperf_tcp_2m.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    second_row = next(csv_reader)
    print(second_row)
    tcp_data = second_row[1].split(" ")

plt.plot(tcp_data)
plt.plot(udp_data)
plt.xlabel("Runs")
plt.ylabel("Throughput")
plt.title("Signal Strength at 2m")
plt.savefig("signal_strength_runs.png")

# plt.show()
