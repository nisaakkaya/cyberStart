import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    # Noktalar arasındaki farkları hesapla
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    
    # Öklid mesafesi formülüne göre mesafeyi hesapla
    distance = math.sqrt(dx**2 + dy**2)
    
    return distance

# Test etmek için iki nokta
point1 = (1, 2)
point2 = (4, 6)

# Mesafeyi hesapla ve ekrana yazdır
distance = euclideanDistance(point1, point2)
print(f"Öklid mesafesi: {distance}")