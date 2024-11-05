import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    # Noktalar arasındaki farkları hesapla
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    
    # Öklid mesafesi formülüne göre mesafeyi hesapla
    distance = math.sqrt(dx**2 + dy**2)
    
    return distance

# 2D uzaydaki noktalar
points = [(1, 2), (4, 6), (7, 8), (2, 3)]

# Mesafelerin saklanacağı liste
distances = []

# Noktalar arasındaki mesafeleri hesaplamak için çiftler oluştur
for i in range(len(points)):
    for j in range(i+1, len(points)):  # i+1 ile yalnızca bir kere hesaplanmasını sağlıyoruz
        dist = euclideanDistance(points[i], points[j])  # Mesafeyi hesapla
        distances.append(dist)  # Hesaplanan mesafeyi distances listesine ekle

# Sonuçları yazdır
print("Noktalar arasındaki mesafeler:")
for dist in distances:
    print(f"{dist:.2f}")