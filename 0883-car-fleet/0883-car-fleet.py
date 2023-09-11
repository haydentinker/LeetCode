class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Approach:
        Use a list as a stack
        Combine position and speed into one list then sort based on positon.
        Loop over that array and calculate time until it reaches the target 
        and append that to the stack. After that check last two indexes of stack
        to see if the last is slower. If it is pop it and reduce the number of fleets
        '''
        cars = list()
        stack = list()
        for index in range(len(position)):
            cars.append([position[index], speed[index]])
        
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        #Sort array based on position
        for car_position, car_speed in cars:
            #Append the time until it reaches target to stack
            stack.append((target-car_position)/car_speed)
            #If the last element is slower than the element behind it, pop stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
