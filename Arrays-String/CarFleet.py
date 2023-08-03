def CarFleet(target, position, speed):
    cars = []
    stack = []
    for index in range(len(position)):
        cars.append([position[index], speed[index]])
    print(cars)
    cars = sorted(cars, key=lambda x: x[0], reverse=True)
    print(cars)
    for car_position, car_speed in cars:
        stack.append((target - car_position) / car_speed)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


# print(CarFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
# print(CarFleet(100, [0, 2, 4], [4, 2, 1]))
print(CarFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
