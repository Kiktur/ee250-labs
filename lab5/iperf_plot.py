import csv
import matplotlib.pyplot as plt
run_values = [1, 2, 3, 4, 5]
tcp_data = []
with open('iperf_tcp_20m.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    second_row = next(csv_reader)
    print(second_row)
    tcp_data = second_row[1].split(" ")

udp_data = []
with open('iperf_udp_20m.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    second_row = next(csv_reader)
    print(second_row)
    udp_data = second_row[1].split(" ")

tcp_data.pop(0)
tcp_data = [float(s) for s in tcp_data]
udp_data.pop(0)
udp_data = [float(s) for s in udp_data]


print(f"TCP data: {tcp_data}")
print(f"UDP data: {udp_data}")


fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Run Number')
ax1.set_ylabel('Throughput (Mbps)', color=color)
ax1.plot(run_values, tcp_data, marker='s', linestyle='--', color=color, markersize=10, linewidth=2, label="TCP Throughput (Mbps)")
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'tab:red'
ax2.set_ylabel('Throughput (Mbps)', color=color)
ax2.plot(run_values, udp_data, marker='s', linestyle='--', color=color, markersize=10, linewidth=2, label="UDP Throughput (Mbps)")
ax2.tick_params(axis='y', labelcolor=color)
fig.legend(loc='lower right')
plt.title('TCP and UDP Connection Speeds at 20m')
fig.tight_layout()
plt.show()

fig.savefig("signal_strengths_20m.png")

