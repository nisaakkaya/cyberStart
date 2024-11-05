# 2D uzaydaki noktaları temsil eden liste oluşturma
def create_points():
    # Boş bir liste oluşturuyoruz
    points = []
    
    # Kullanıcıdan nokta sayısını alıyoruz
    n = int(input("Kaç nokta eklemek istersiniz? "))
    
    # Döngü ile her bir nokta için x ve y koordinatlarını alıyoruz
    for i in range(n):
        x = float(input(f"{i+1}. noktanın x koordinatını girin: "))
        y = float(input(f"{i+1}. noktanın y koordinatını girin: "))
        points.append((x, y))  # (x, y) demetini listeye ekliyoruz
    
    return points

# Noktaların yazdırılması
def print_points(points):
    print("\nNoktalarınız:")
    for point in points:
        print(f"({point[0]}, {point[1]})")

# Ana fonksiyon
def main():
    points = create_points()  # Noktaları oluştur
    print_points(points)  # Noktaları ekrana yazdır

# Programı çalıştır
if __name__ == "__main__":
    main()
