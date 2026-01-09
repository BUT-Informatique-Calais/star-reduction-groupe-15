import requests

# On cherche "Hubble galaxy" pour avoir de belles images
url = "https://images-api.nasa.gov/search?q=hubble%20galaxy&media_type=image"

print("--- TEST NASA IMAGE LIBRARY ---")

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    
    # On récupère les 5 premiers résultats
    items = data['collection']['items'][:5]
    
    if not items:
        print("Aucun résultat trouvé.")
    else:
        for i, item in enumerate(items):
            title = item['data'][0]['title']
            # Le lien vers l'image est dans un fichier JSON secondaire ou directement dans 'links'
            img_url = item['links'][0]['href']
            
            print(f"\n[Image {i+1}] : {title}")
            print(f"Lien direct : {img_url}")
            
            # Test de téléchargement pour la première image
            if i == 0:
                img_data = requests.get(img_url).content
                with open("photo_nasa.jpg", "wb") as f:
                    f.write(img_data)
                    
except Exception as e:
    print(f"Erreur : {e}")

print("\n--- FIN DU TEST ---")