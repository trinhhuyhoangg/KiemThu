import cmath

def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        x = -c / b
        return (x)
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + cmath.sqrt(delta)) / (2*a)
            x2 = (-b - cmath.sqrt(delta)) / (2*a)
            return (x1, x2)
        elif delta == 0:
            x = -b / (2*a)
            return (x)
        else:
            x1 = (-b + cmath.sqrt(delta)) / (2*a)
            x2 = (-b - cmath.sqrt(delta)) / (2*a)
            return (x1, x2)

print(giai_phuong_trinh_bac_hai(0, 1, 1))
print(giai_phuong_trinh_bac_hai(1, -3, 2))
print(giai_phuong_trinh_bac_hai(1, -2, 1))
print(giai_phuong_trinh_bac_hai(1, 2, 5))