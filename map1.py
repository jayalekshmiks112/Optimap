import requests
import random

api_key = '############'
postal_code = '695001'
number_of_places = 10

places_list = []

latitude = random.uniform(8.47, 8.52)
longitude = random.uniform(76.90, 76.95)

url = f'https://api.geoapify.com/v1/geocode/reverse?lat={latitude}&lon={longitude}&postalCode={postal_code}&apiKey={api_key}&limit={number_of_places}'

response = requests.get(url)
data = response.json()

if 'features' in data and len(data['features']) > 0:
    places = data['features']
    print(f"Places suggested in the package:")
    for index, place in enumerate(places, start=1):
        place_name = place['properties'].get('formatted')
        coordinates = place['geometry'].get('coordinates')
        places_list.append([index, place_name, coordinates])
        print(f"{index}. {place_name} - Coordinates: {coordinates}")
else:
    print("No places found.")

def take_input():
    start = input("Enter the start location number: ")
    end = input("Enter the end location number: ")
    num = int(input("How many places you want to visit in between? "))
    btwn = []
    print("Enter the serial numbers of places you want to visit: ")
    for i in range(num):
        n = int(input())
        btwn.append(n)  

    return start, end, btwn

def distance(location):
    for place in places_list:
        if place[0] == location:
            return place[2]  

def main():
    start, end, to_visit = take_input()
    
    start_c = distance(int(start))
    end_c = distance(int(end))
    
    if start_c and end_c:
        bwtn_c = {loc: distance(loc) for loc in to_visit}
        
        print("Start coordinates:", start_c)
        print("End coordinates:", end_c)
        print("In-between coordinates:", bwtn_c)
    else:
        print("Please enter valid start and end locations.")

if __name__ == "__main__":
    main()
