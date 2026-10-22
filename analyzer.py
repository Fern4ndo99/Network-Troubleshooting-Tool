import ipaddress



def analyze_network(output):
    ip_address = None
    subnet_mask = None
    gateway = None

    for line in output.splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.replace(".", "").strip().lower()
        value = value.strip()

        if key in ("ipv4 address", "ip address"):
            ip_address = value

        elif key == "subnet mask":
            subnet_mask = value

        elif key == "default gateway":
            gateway = value

    if not any([ip_address, subnet_mask, gateway]):
        return

    print("IP Address:", ip_address)
    print("Subnet Mask:", subnet_mask)
    print("Gateway:", gateway)

    if ip_address is None or subnet_mask is None or gateway is None:
        print("\nNot enough information to analyze the gateway.")
        return

    try:
        network = ipaddress.ip_network(
            f"{ip_address}/{subnet_mask}",
            strict=False
        )

        gateway_ip = ipaddress.ip_address(gateway)

    except ValueError:
        print("\nInvalid IP address, subnet mask, or gateway.")
        return

    if gateway_ip not in network:

        print("\nPossible Issue: Incorrect Default Gateway")

        print("Reason:")
        print("The default gateway is outside the device's subnet.")

        print("\nSuggested Steps:")
        print("1. Check the device's default gateway.")
        print("2. Verify the router interface IP address.")
        print("3. Correct the gateway if necessary.")
        print("4. Ping the gateway to test connectivity.")

    else:

        print("\nThe gateway belongs to the device's subnet.")
        print("Further checks are needed to confirm connectivity.")