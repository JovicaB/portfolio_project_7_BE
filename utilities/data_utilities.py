class DataUtilities:

    @staticmethod
    def calculate_difference(new_value: float, old_value: float) -> float:
        """Calculate increase/decrease between 2 numbers

        Args:
            new_value (float):
            old_value (float): 

        Returns:
            float: increase/descrease difference between 2 numbers
        """
        return round((old_value - new_value) / new_value, 4)

    
## USAGE
# class_instance = DataUtilities()
# difference_calculation = class_instance.calculate_difference(10, 20)
# print(difference_calculation)