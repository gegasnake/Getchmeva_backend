import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

country = "thailand"
base_url = f"https://world.openfoodfacts.org/country/{country}/{{}}.json"
output_file = "thai_products.txt"

with open(output_file, "w", encoding="utf-8") as file:
    page = 1
    total_products = 0
    max_pages = 100

    while True:
        print(f"Fetching page {page}...")
        url = base_url.format(page)
        try:
            response = requests.get(url, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            break

        if response.status_code != 200:
            print(f"Failed to fetch page {page} (status {response.status_code})")
            break

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Invalid JSON. Here's the raw response:")
            print(response.text[:500])
            break

        products = data.get("products", [])
        if not products:
            print("No more products.")
            break

        for product in products:
            product_name = product.get("product_name", "N/A")
            brands = product.get("brands", "N/A")
            categories = product.get("categories", "N/A")
            file.write(f"Name: {product_name}\n")
            file.write(f"Brands: {brands}\n")
            file.write(f"Categories: {categories}\n")
            file.write("-" * 40 + "\n")
            total_products += 1

        page += 1
        if page > max_pages:
            print(f"Reached page limit ({max_pages}).")
            break

        time.sleep(1)

print(f"✅ Finished. Total products saved: {total_products}")
