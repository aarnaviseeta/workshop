import json
import os

input_file = 'data.json'
output_folder = 'data/outputs'
output_file = os.path.join(output_folder, 'flat_properties.json')

def flatten_properties(input_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            properties = json.load(f)

        flat_list = []
        for prop in properties:
            info = prop.get("info", {})
            flat = {
                "id": prop.get("id"),
                "price": info.get("price"),
                "zone": info.get("zone"),
                "roomsNo": info.get("roomsNo"),
                "surface": info.get("surface"),
                "bathroomsNo": info.get("bathroomsNo"),
                "type": info.get("type"),
                "createdOn": info.get("createdOn"),
                "ccy": info.get("ccy"),
                "url": info.get("url"),
                "active": prop.get("active"),
                "created_datetime": prop.get("created_datetime"),
                "updated_datetime": prop.get("updated_datetime"),
            }
            flat_list.append(flat)

        os.makedirs(output_folder, exist_ok=True)
        with open(output_file, "w", encoding='utf-8') as f:
            json.dump(flat_list, f, indent=2, ensure_ascii=False)

        print("✅ Flat property data written to:", output_file)
        print("ℹ️  Total properties:", len(flat_list))

    except Exception as e:
        print(f"❌ Error: {str(e)}")

# Run it
flatten_properties(input_file)