import re


def analyze_ping(output):

    output = output.lower()

    if "destination host unreachable" in output:
        print("\nPing Analysis:")
        print("Issue: Destination host unreachable")
        print("Possible routing, gateway, or local connectivity problem.")
        return

    loss_match = re.search(
        r"(\d+(?:\.\d+)?)%\s*(?:packet loss|loss)\b",
        output
    )

    if loss_match:

        packet_loss = float(loss_match.group(1))

        print("\nPing Analysis:")
        print(f"Packet Loss: {packet_loss}%")

        if packet_loss == 0:
            print("Result: No packet loss detected.")

        elif packet_loss == 100:
            print("Result: No ping replies received.")
            print("Possible connectivity or ICMP filtering issue.")

        else:
            print("Result: Partial packet loss detected.")
            print("Investigate network stability and congestion.")

    elif "request timed out" in output or "request timeout" in output:
        print("\nPing Analysis:")
        print("Result: Ping timeout detected.")
        print("No reply was received for at least one request.")