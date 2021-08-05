data = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    },
    {
        "color": "cyan",
        "value": "#0ff"
    }
]

if __name__ == "__main__":
    count: int = 1
    for x in data:
        print(f"Index %d has %s color with %s value" % (count, x.get("color"), x.get("value")))
        count += 1

    print()

    for index, item in enumerate(data):
        print(f"Index %d has %s color with %s value" % (index + 1, item.get("color"), item.get("value")))

