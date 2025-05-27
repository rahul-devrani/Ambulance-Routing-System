import heapq
nodes = {
    # Locations
    "ISBT": {"coords": (50, 50), "type": "location"},
    "Clock Tower": {"coords": (200, 50), "type": "location"},
    "Paltan Bazaar": {"coords": (280, 100), "type": "location"},
    "Rajpur Road": {"coords": (350, 30), "type": "location"},
    "Ballupur": {"coords": (180, 160), "type": "location"},
    "Prem Nagar": {"coords": (50, 220), "type": "location"},
    "Kaulagarh": {"coords": (400, 180), "type": "location"},
    "GMS Road": {"coords": (130, 110), "type": "location"},
    "Saharanpur Chowk": {"coords": (130, 30), "type": "location"},
    "Race Course": {"coords": (260, 220), "type": "location"},
    "Clement Town": {"coords": (30, 180), "type": "location"},
    "Araghar": {"coords": (420, 100), "type": "location"},
    "Subhash Nagar": {"coords": (30, 130), "type": "location"},
    "Nehru Colony": {"coords": (260, 280), "type": "location"},
    "Kargi Chowk": {"coords": (100, 280), "type": "location"},
    "Jakhan": {"coords": (470, 50), "type": "location"},
    "Raipur": {"coords": (550, 180), "type": "location"},
    "Vasant Vihar": {"coords": (300, 140), "type": "location"},
    "Ajabpur": {"coords": (120, 160), "type": "location"},
    "Dalanwala": {"coords": (400, 240), "type": "location"},
    "EC Road": {"coords": (260, 80), "type": "location"},
    "Indira Nagar": {"coords": (500, 140), "type": "location"},
    "Mothrowala": {"coords": (70, 160), "type": "location"},
    "Patel Nagar": {"coords": (160, 90), "type": "location"},
    "Majra": {"coords": (90, 90), "type": "location"},
    "Selaqui": {"coords": (30, 300), "type": "location"},
    "Brahmanwala": {"coords": (200, 200), "type": "location"},
    "Laxman Chowk": {"coords": (230, 140), "type": "location"},
    "Haridwar Road": {"coords": (260, 40), "type": "location"},
    "Chakrata Road": {"coords": (190, 130), "type": "location"},
    "Seema Dental": {"coords": (150, 250), "type": "location"},
    "Bhaniyawala": {"coords": (600, 220), "type": "location"},

    # Hospitals
    "Max Hospital": {"coords": (600, 50), "type": "hospital"},
    "Doon Hospital": {"coords": (370, 300), "type": "hospital"},
    "Synergy Hospital": {"coords": (470, 270), "type": "hospital"},
    "Shri Mahant Hospital": {"coords": (300, 320), "type": "hospital"},
    "CHC Premnagar": {"coords": (30, 260), "type": "hospital"},
    "Velmed Hospital": {"coords": (180, 20), "type": "hospital"},
    "City Hospital": {"coords": (130, 320), "type": "hospital"},
    "Suddh Anand Hospital": {"coords": (250, 340), "type": "hospital"},
    "AIIMS Rishikesh": {"coords": (20, 360), "type": "hospital"},
    "Combined Medical Institute": {"coords": (200, 360), "type": "hospital"},
    "Ashirwad Hospital": {"coords": (500, 300), "type": "hospital"},
    "Government Hospital Raipur": {"coords": (550, 240), "type": "hospital"},
}


edges = {
    "ISBT": {"GMS Road": 3, "Clock Tower": 7, "City Hospital": 3, "Majra": 3,"Ashirwad Hospital": 5},
    "Clock Tower": {"ISBT": 7, "Rajpur Road": 0.2, "Paltan Bazaar": 1.7, "EC Road": 1.6, "Haridwar Road": 2},
    "Paltan Bazaar": {"Clock Tower": 2, "Ballupur": 3, "Race Course": 2, "Laxman Chowk": 2},
    "Rajpur Road": {"Clock Tower": 4, "Jakhan": 3, "Indira Nagar": 4},
    "Ballupur": {"Paltan Bazaar": 3, "Kaulagarh": 3, "Prem Nagar": 5, "Ajabpur": 3},
    "Prem Nagar": {"Ballupur": 5, "CHC Premnagar": 3, "Clement Town": 2},
    "Kaulagarh": {"Ballupur": 3, "Araghar": 4, "Vasant Vihar": 2},
    "GMS Road": {"ISBT": 3, "Saharanpur Chowk": 2, "Patel Nagar": 3},
    "Saharanpur Chowk": {"GMS Road": 2, "Velmed Hospital": 3},
    "Race Course": {"Paltan Bazaar": 2, "Doon Hospital": 3, "Nehru Colony": 3},
    "Araghar": {"Kaulagarh": 4, "Dalanwala": 3,"Ashirwad Hospital": 5},
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
    "Subhash Nagar": {"Majra": 2},
    "Majra": {"ISBT": 3, "Subhash Nagar": 2, "Mothrowala": 3},
    "Mothrowala": {"Ajabpur": 2,"City Hospital": 3},
    "Patel Nagar": {"GMS Road": 3},
    "Selaqui": {"Prem Nagar": 7},
    "Brahmanwala": {"Ballupur": 3,"City Hospital": 2},
    "Laxman Chowk": {"Paltan Bazaar": 2},
    "Haridwar Road": {"Clock Tower": 2, "City Hospital": 3},
    "Chakrata Road": {"Ballupur": 2},
    "Seema Dental": {"Nehru Colony": 2, "City Hospital": 2},
    "Bhaniyawala": {"Raipur": 5, "City Hospital": 3},
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

def find_nearest_hospital(start):
    import heapq
    distances = {node: float('inf') for node in nodes}
    previous = {node: None for node in nodes}
    distances[start] = 0
    queue = [(0, start)]

    visited = set()
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        visited.add(current_node)

        if nodes[current_node]['type'] == 'hospital':
            path = []
            curr = current_node
            while curr:
                path.insert(0, curr)
                curr = previous[curr]
            return current_node, distances[current_node], path

        for neighbor, weight in edges.get(current_node, {}).items():
            if neighbor in visited:
                continue
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, float('inf'), []


