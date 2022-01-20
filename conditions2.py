  if lamp_counter & fan_counter == 1:
        lamp_on()
        fan_on()
        # 10 seconds
        time.sleep(10)
        lamp_counter += 1

    if fan_counter >= 60:
       fan_on()
       fan_counter = 1

    if lamp_counter >= 5760.1:
        while x <= 2880:
          lamp_off()
          x =+ 1
        lamp_counter = 1