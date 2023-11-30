class DataUtilities:

    @staticmethod
    def calculate_difference(first_value: float, second_value: float) -> float:
        """Calculate increase/decrease between 2 numbers

        Args:
            first_value (float):
            second_value (float): 

        Returns:
            float: increase/descrease difference between 2 numbers
        """
        return (second_value - first_value) / first_value

    
## USAGE
# class_instance = DataUtilities()
# difference_calculation = class_instance.calculate_difference(10, 20)
# print(difference_calculation)