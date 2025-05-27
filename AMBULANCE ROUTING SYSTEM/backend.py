import heapq
nodes = {
    # Locations
    "ISBT": {"coords": (80, 100), "type": "location"},
    "Clock Tower": {"coords": (270, 100), "type": "location"},
    "Paltan Bazaar": {"coords": (320, 140), "type": "location"},
    "Rajpur Road": {"coords": (410, 80), "type": "location"},
    "Ballupur": {"coords": (240, 220), "type": "location"},
    "Prem Nagar": {"coords": (100, 300), "type": "location"},
    "Kaulagarh": {"coords": (420, 220), "type": "location"},
    "GMS Road": {"coords": (150, 160), "type": "location"},
    "Saharanpur Chowk": {"coords": (170, 80), "type": "location"},
    "Race Course": {"coords": (330, 280), "type": "location"},
    "Clement Town": {"coords": (70, 260), "type": "location"},
    "Araghar": {"coords": (460, 160), "type": "location"},
    "Subhash Nagar": {"coords": (70, 190), "type": "location"},
    "Nehru Colony": {"coords": (320, 340), "type": "location"},
    "Kargi Chowk": {"coords": (180, 340), "type": "location"},
    "Jakhan": {"coords": (500, 100), "type": "location"},
    "Raipur": {"coords": (570, 220), "type": "location"},
    "Vasant Vihar": {"coords": (350, 200), "type": "location"},
    "Ajabpur": {"coords": (160, 230), "type": "location"},
    "Dalanwala": {"coords": (440, 280), "type": "location"},
    "EC Road": {"coords": (300, 120), "type": "location"},
    "Indira Nagar": {"coords": (520, 180), "type": "location"},
    "Mothrowala": {"coords": (100, 230), "type": "location"},
    "Patel Nagar": {"coords": (200, 140), "type": "location"},
    "Majra": {"coords": (120, 140), "type": "location"},
    "Selaqui": {"coords": (60, 360), "type": "location"},
    "Brahmanwala": {"coords": (240, 260), "type": "location"},
    "Laxman Chowk": {"coords": (290, 200), "type": "location"},
    "Haridwar Road": {"coords": (300, 80), "type": "location"},
    "Chakrata Road": {"coords": (250, 180), "type": "location"},
    "Seema Dental": {"coords": (230, 320), "type": "location"},
    "Bhaniyawala": {"coords": (610, 280), "type": "location"},

    # Hospitals
    "Max Hospital": {"coords": (610, 100), "type": "hospital"},
    "Doon Hospital": {"coords": (370, 360), "type": "hospital"},
    "Synergy Hospital": {"coords": (490, 320), "type": "hospital"},
    "Shri Mahant Hospital": {"coords": (330, 380), "type": "hospital"},
    "CHC Premnagar": {"coords": (70, 330), "type": "hospital"},
    "Velmed Hospital": {"coords": (200, 60), "type": "hospital"},
    "City Hospital": {"coords": (180, 380), "type": "hospital"},
    "Suddh Anand Hospital": {"coords": (280, 400), "type": "hospital"},
    "AIIMS Rishikesh": {"coords": (40, 420), "type": "hospital"},
    "Combined Medical Institute": {"coords": (240, 420), "type": "hospital"},
    "Ashirwad Hospital": {"coords": (520, 340), "type": "hospital"},
    "Government Hospital Raipur": {"coords": (580, 260), "type": "hospital"},
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
    import heapq
    distances = {node: float('inf') for node in nodes}
    previous = {node: None for node in nodes}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor, weight in edges.get(current_node, {}).items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    curr = end
    while curr:
        path.insert(0, curr)
        curr = previous[curr]

    return distances[end], path

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
