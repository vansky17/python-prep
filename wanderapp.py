class WanderSpeed:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    def calculate_speed(self):

        if self.distance <= 0:
            print("Distance must be greater than 0.")
            return None
        if self.duration <= 0:
            print("Duration must be greater than 0.")
            return None
               
        return self.distance / self.duration
    
    def show_info(self):
        if self.calculate_speed() is not None:
            print(f"Speed: The {self.distance} kilometers distance will take {self.duration} hours at {self.calculate_speed():.2f} km/h.")


wander_speed = WanderSpeed(10, 2)
wander_speed.show_info()

class WanderDuration:
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed

    def calculate_duration(self):

        if self.distance <= 0:
            print("Distance must be greater than 0.")
            return None
        if self.speed <= 0:
            print("Speed must be greater than 0.")
            return None
        
        return self.distance / self.speed

    def show_info(self):
        if self.calculate_duration() is not None:
            print(f"Duration: The {self.distance} kilometers distance will take {self.calculate_duration():.2f} hours at {self.speed} km/h.")


wander_duration = WanderDuration(20, 7)
wander_duration.show_info()

class WanderDistance:
    def __init__(self, duration, speed):
        self.duration = duration
        self.speed = speed

    def calculate_distance(self):

        if self.duration <= 0:
            print("Duration must be greater than 0.")
            return None 

        if self.speed <= 0:
            print("Speed must be greater than 0.")
            return None
        
        return self.duration * self.speed
    
    def show_info(self):
        if self.calculate_distance() is not None:
            print(f"Distance: The {self.duration} hours at {self.speed} km/h will cover {self.calculate_distance():.2f} kilometers.")


wander_distance = WanderDistance(2, 10)
wander_distance.show_info()

# The code defines three classes: WanderSpeed, WanderDuration, and WanderDistance. Each class calculates either speed, duration, or distance based on the provided inputs. The classes include error handling for invalid inputs and display the results with two decimal places.
