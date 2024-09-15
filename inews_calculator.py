def calculate_inews_score(resp_rate, spo2, oxygen, systolic_bp, heart_rate, acvpu, temp):
    # Respiratory Rate (bpm)
    if resp_rate <= 8:
        resp_score = 3
    elif 9 <= resp_rate <= 11:
        resp_score = 2
    elif 12 <= resp_rate <= 20:
        resp_score = 0
    elif 21 <= resp_rate <= 24:
        resp_score = 1
    else:
        resp_score = 3

    # SpO2 (%)
    if spo2 <= 91:
        spo2_score = 3
    elif 92 <= spo2 <= 93:
        spo2_score = 2
    elif 94 <= spo2 <= 95:
        spo2_score = 1
    else:
        spo2_score = 0

    # Inspired O2 (Fi O2)
    o2_score = 0 if oxygen == "Air" else 2

    # Systolic Blood Pressure (mmHg)
    if systolic_bp <= 90:
        bp_score = 3
    elif 91 <= systolic_bp <= 100:
        bp_score = 2
    elif 101 <= systolic_bp <= 110:
        bp_score = 1
    elif 111 <= systolic_bp <= 249:
        bp_score = 0
    else:
        bp_score = 3

    # Heart Rate (BPM)
    if heart_rate <= 40:
        hr_score = 3
    elif 41 <= heart_rate <= 50:
        hr_score = 2
    elif 51 <= heart_rate <= 90:
        hr_score = 0
    elif 91 <= heart_rate <= 110:
        hr_score = 1
    elif 111 <= heart_rate <= 130:
        hr_score = 2
    else:
        hr_score = 3

    # ACVPU/CNS Response
    if acvpu == "Alert":
        acvpu_score = 0
    elif acvpu == "Confusion" or acvpu == "Voice" or acvpu == "Pain" or acvpu == "Unresponsive":
        acvpu_score = 3
    else:
        acvpu_score = 0

    # Temperature (°C)
    if temp <= 35.0:
        temp_score = 3
    elif 35.1 <= temp <= 36.0:
        temp_score = 1
    elif 36.1 <= temp <= 38.0:
        temp_score = 0
    elif 38.1 <= temp <= 39.0:
        temp_score = 1
    else:
        temp_score = 3

    # Calculate total INEWS score
    total_score = resp_score + spo2_score + o2_score + bp_score + hr_score + acvpu_score + temp_score

    return total_score


# Example of using the function

if __name__ == "__main__":
    resp_rate = 20  # Example input values
    spo2 = 88
    oxygen = "Air"
    systolic_bp = 120
    heart_rate = 85
    acvpu = "Alert"
    temp = 38.9

    inews_score = calculate_inews_score(resp_rate, spo2, oxygen, systolic_bp, heart_rate, acvpu, temp)
    print(f"The iNEWS score is: {inews_score}")
