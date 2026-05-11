import math

class Shape:
    """Ülemklass kõigile kujunditele."""
    
    def __init__(self, color: str):
        self.color = color
        
    def set_color(self, color: str):
        self.color = color
        
    def get_color(self) -> str:
        return self.color
        
    def get_area(self) -> float:
        # Baasklassis me pindala arvutada ei oska, seega tagastame näiteks 0.0
        # Alamklassid kirjutavad selle meetodi üle (override).
        return 0.0


class Circle(Shape):
    """Kujundi alamklass: ring."""
    
    def __init__(self, color: str, radius: float):
        # Kasutame ülemklassi (Shape) konstruktorit värvi määramiseks
        super().__init__(color)
        self.radius = radius
        
    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)
        
    def __repr__(self) -> str:
        return f"Circle (r: {self.radius}, color: {self.color})"


class Square(Shape):
    """Kujundi alamklass: ruut."""
    
    def __init__(self, color: str, side: float):
        super().__init__(color)
        self.side = side
        
    def get_area(self) -> float:
        return self.side * self.side
        
    def __repr__(self) -> str:
        return f"Square (a: {self.side}, color: {self.color})"


class Rectangle(Shape):
    """Kujundi alamklass: ristkülik."""
    
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.length = length
        self.width = width
        
    def get_area(self) -> float:
        return self.length * self.width
        
    def __repr__(self) -> str:
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"


class Paint:
    """Klass kujundite haldamiseks."""
    
    def __init__(self):
        # Hoiame kõik lisatud kujundid listis
        self.shapes = []
        
    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)
        
    def get_shapes(self) -> list:
        return self.shapes
        
    def calculate_total_area(self) -> float:
        # Polümorfismi võlu: me ei pea teadma, kas kujund on ring või ruut,
        # saame lihtsalt kutsuda get_area() ja õige klassi meetod teeb töö.
        total_area = 0.0
        for shape in self.shapes:
            total_area += shape.get_area()
        return total_area
        
    def get_circles(self) -> list:
        # 'isinstance' kontrollib, kas objekt on määratud klassist
        return [shape for shape in self.shapes if isinstance(shape, Circle)]
        
    def get_squares(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Square)]
        
    def get_rectangles(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Rectangle)]

if __name__ == "__main__":
    # 1. Loome uue "lõuendi" ehk Paint objekti
    minu_pilt = Paint()

    # 2. Loome mõned erinevad kujundid
    ring1 = Circle("punane", 5.0)
    ring2 = Circle("sinine", 2.5)
    ruut1 = Square("roheline", 4.0)
    ristkülik1 = Rectangle("kollane", 3.0, 6.0)

    # 3. Lisame loodud kujundid Paint objekti sisse
    minu_pilt.add_shape(ring1)
    minu_pilt.add_shape(ring2)
    minu_pilt.add_shape(ruut1)
    minu_pilt.add_shape(ristkülik1)

    # 4. Vaatame, mis kujundid meil listis on.
    # Siin teeb ilusa väljatrüki see __repr__ meetod, mille me igale klassile lisasime!
    print("--- Kõik kujundid ---")
    print(minu_pilt.get_shapes())
    print()

    # 5. Arvutame kõigi kujundite kogupindala
    kogupindala = minu_pilt.calculate_total_area()
    # Kujundame väljundi nii, et näitaks ainult 2 komakohta (:.2f)
    print(f"Kõigi kujundite kogupindala on: {kogupindala:.2f}")
    print()

    # 6. Küsime näiteks ainult ringe
    print("--- Ainult ringid ---")
    print(minu_pilt.get_circles())