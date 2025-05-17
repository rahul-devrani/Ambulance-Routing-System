import heapq
nodes = {
    # Locations
    "ISBT": {"coords": (100, 100), "type": "location"},
    "Clock Tower": {"coords": (200, 100), "type": "location"},
    "Paltan Bazaar": {"coords": (250, 150), "type": "location"},
    "Rajpur Road": {"coords": (300, 80), "type": "location"},
    "Ballupur": {"coords": (180, 200), "type": "location"},
    "Prem Nagar": {"coords": (80, 250), "type": "location"},
    "Kaulagarh": {"coords": (320, 200), "type": "location"},
    "GMS Road": {"coords": (150, 150), "type": "location"},
    "Saharanpur Chowk": {"coords": (150, 50), "type": "location"},
    "Race Course": {"coords": (220, 250), "type": "location"},
    "Clement Town": {"coords": (60, 200), "type": "location"},
    "Araghar": {"coords": (350, 150), "type": "location"},
    "Subhash Nagar": {"coords": (50, 150), "type": "location"},
    "Nehru Colony": {"coords": (220, 300), "type": "location"},
    "Kargi Chowk": {"coords": (100, 300), "type": "location"},
    "Jakhan": {"coords": (400, 100), "type": "location"},
    "Raipur": {"coords": (450, 200), "type": "location"},
    "Vasant Vihar": {"coords": (280, 180), "type": "location"},
    "Ajabpur": {"coords": (120, 180), "type": "location"},
    "Dalanwala": {"coords": (370, 250), "type": "location"},
    "EC Road": {"coords": (260, 120), "type": "location"},
    "Indira Nagar": {"coords": (480, 180), "type": "location"},
    "Mothrowala": {"coords": (70, 180), "type": "location"},
    "Patel Nagar": {"coords": (160, 130), "type": "location"},
    "Majra": {"coords": (90, 130), "type": "location"},
    "Selaqui": {"coords": (30, 300), "type": "location"},
    "Brahmanwala": {"coords": (200, 220), "type": "location"},
    "Laxman Chowk": {"coords": (210, 160), "type": "location"},
    "Haridwar Road": {"coords": (260, 200), "type": "location"},
    "Chakrata Road": {"coords": (190, 180), "type": "location"},
    "Seema Dental": {"coords": (150, 270), "type": "location"},
    "Bhaniyawala": {"coords": (500, 250), "type": "location"},

    # Hospitals
    "Max Hospital": {"coords": (500, 100), "type": "hospital"},
    "Doon Hospital": {"coords": (320, 300), "type": "hospital"},
    "Synergy Hospital": {"coords": (400, 280), "type": "hospital"},
    "Shri Mahant Hospital": {"coords": (280, 320), "type": "hospital"},
    "CHC Premnagar": {"coords": (50, 280), "type": "hospital"},
    "Velmed Hospital": {"coords": (370, 50), "type": "hospital"},
    "City Hospital": {"coords": (150, 320), "type": "hospital"},
    "Suddh Anand Hospital": {"coords": (250, 330), "type": "hospital"},
    "AIIMS Rishikesh": {"coords": (20, 350), "type": "hospital"},
    "Combined Medical Institute": {"coords": (200, 350), "type": "hospital"},
    "Ashirwad Hospital": {"coords": (450, 320), "type": "hospital"},
    "Government Hospital Raipur": {"coords": (480, 240), "type": "hospital"},
}

edges = {
    "ISBT": {"GMS Road": 3, "Clock Tower": 4},
    "Clock Tower": {"ISBT": 4, "Rajpur Road": 4, "Paltan Bazaar": 2, "EC Road": 2},
    "Paltan Bazaar": {"Clock Tower": 2, "Ballupur": 3, "Race Course": 2},
    "Rajpur Road": {"Clock Tower": 4, "Jakhan": 3, "Indira Nagar": 4},
    "Ballupur": {"Paltan Bazaar": 3, "Kaulagarh": 3, "Prem Nagar": 5, "Ajabpur": 3},
    "Prem Nagar": {"Ballupur": 5, "CHC Premnagar": 3, "Clement Town": 2},
    "Kaulagarh": {"Ballupur": 3, "Araghar": 4, "Vasant Vihar": 2},
    "GMS Road": {"ISBT": 3, "Saharanpur Chowk": 2, "Patel Nagar": 3},
    "Saharanpur Chowk": {"GMS Road": 2, "Velmed Hospital": 3},
    "Race Course": {"Paltan Bazaar": 2, "Doon Hospital": 3, "Nehru Colony": 3},
    "Araghar": {"Kaulagarh": 4, "Dalanwala": 3},
    "Nehru Colony": {"Race Course": 3, "Shri Mahant Hospital": 2, "Suddh Anand Hospital": 3, "Combined Medical Institute": 2},
    "Kargi Chowk": {"Nehru Colony": 3, "City Hospital": 2},
    "Jakhan": {"Rajpur Road": 3, "Max Hospital": 2},
    "Raipur": {"Jakhan": 5, "Government Hospital Raipur": 2, "Ashirwad Hospital": 4},
    "Dalanwala": {"Araghar": 3, "Synergy Hospital": 2},
    "CHC Premnagar": {"Prem Nagar": 3, "AIIMS Rishikesh": 7},
    "Velmed Hospital": {"Saharanpur Chowk": 3},
    "City Hospital": {"Kargi Chowk": 2},
    "Suddh Anand Hospital": {"Nehru Colony": 3},
    "Combined Medical Institute": {"Nehru Colony": 2},
    "Ashirwad Hospital": {"Raipur": 4},
    "Government Hospital Raipur": {"Raipur": 2},
}

def dijkstra(start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return (cost, path)
        for neighbor, weight in edges.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return (float("inf"), [])
