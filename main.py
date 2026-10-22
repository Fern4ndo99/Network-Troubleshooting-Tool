from analyzer import analyze_network
from ping_parser import analyze_ping

print("=== Network Troubleshooting Assistant ===")

print("Paste your diagnostic output below.")
print("Type END on a new line when finished.\n")

lines = []
while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

output = "\n".join(lines)

print("\nAnalyzing network...\n")
analyze_ping(output)