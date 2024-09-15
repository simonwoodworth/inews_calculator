import unittest

# Import the function to be tested
from inews_calculator import calculate_inews_score  # Assuming the function is in a file called inews_calculator.py


class TestINEWSCalculator(unittest.TestCase):
    def test_all_normal_values(self):
        # All parameters are within the normal range
        self.assertEqual(calculate_inews_score(16, 97, 'Air', 120, 75, 'Alert', 37.0), 0)

    def test_critical_resp_rate(self):
        # Critical respiratory rate should return high score
        self.assertEqual(calculate_inews_score(7, 97, 'Air', 120, 75, 'Alert', 37.0), 3)

    def test_critical_spo2(self):
        # Critical SpO2 should return high score
        self.assertEqual(calculate_inews_score(16, 90, 'Air', 120, 75, 'Alert', 37.0), 3)

    def test_oxygen_usage(self):
        # Any O2 should return score of 2
        self.assertEqual(calculate_inews_score(16, 97, 'O2', 120, 75, 'Alert', 37.0), 2)

    def test_low_systolic_bp(self):
        # Low systolic BP should return a high score
        self.assertEqual(calculate_inews_score(16, 97, 'Air', 85, 75, 'Alert', 37.0), 3)

    def test_high_heart_rate(self):
        # High heart rate should return a high score
        self.assertEqual(calculate_inews_score(16, 97, 'Air', 120, 135, 'Alert', 37.0), 3)

    def test_confused_patient(self):
        # Confused patient should return a high score
        self.assertEqual(calculate_inews_score(16, 97, 'Air', 120, 75, 'Confusion', 37.0), 3)

    def test_high_temperature(self):
        # High temperature should return a high score
        self.assertEqual(calculate_inews_score(16, 97, 'Air', 120, 75, 'Alert', 39.5), 3)

    def test_low_temperature(self):
        # Low temperature should return a high score
        self.assertEqual(calculate_inews_score(16, 97, 'Air', 120, 75, 'Alert', 34.5), 3)

    def test_mixed_critical_values(self):
        # A case with multiple critical values should return the correct total score
        self.assertEqual(calculate_inews_score(7, 90, 'O2', 85, 135, 'Confusion', 39.5),
                         3 + 3 + 2 + 3 + 3 + 3 + 3)  # Total 20


if __name__ == '__main__':
    unittest.main()
