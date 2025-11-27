from math import pi

# 원 넓이
def get_circle():
    radius = float(input("원의 반지름을 입력하세요: "))
    return pi * radius * radius

# 삼각형 넓이
def triangle_area():
    base = float(input("삼각형의 밑변을 입력하세요: "))
    height = float(input("삼각형의 높이를 입력하세요: "))
    return (base * height) / 2

# 직육면체 부피
def cuboid_volume():
    width = float(input("직육면체의 가로 길이를 입력하세요: "))
    height = float(input("직육면체의 세로 길이를 입력하세요: "))
    depth = float(input("직육면체의 높이를 입력하세요: "))
    return width * height * depth
