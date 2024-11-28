daydate=input('오늘의 요일 :')
dateDay=input('오늘의 날짜 : ')
lowestTem=input('오늘의 최저기온 :')
highesetTem=input('오늘의 최고 기온 :')
rainingPercentage=input('강수 확률:')
fineDustStatue=input('미세먼지 상태 : ')
sunriseTime=input('일출 시간 : ')
sunsetTime=input('일몰 시간 : ')
southOceanWave=input('남해 바다물결 : ')
eastOceanWave=input('동해 바다 물결 :')
westOceanWave=input('서해 앞바다 물결 :')
#print("내일 날씨예보입니다.\n",daydate,'요일인 ', dateDay,'의 아침 최저 기온은',lowestTem,'도', ',낮 촤고 기온은',highesetTem,'도로 예보됐습니다.')
#print("비올 확률은 "+ rainingPercentage+'%이고, 미세먼지는 '+fineDustStatue+ " 수준일 것으로 예상됩니다.")

print(f"내일 날씨예보입니다.\n {daydate}요일인 {dateDay}의 아침 최저 기온은 {lowestTem}도, 낮 촤고 기온은 {highesetTem}도로 예보됐습니다.")
print(f"비올 확률은 {rainingPercentage}%이고, 미세먼지는 {fineDustStatue} 수준일 것으로 예상됩니다. 일출 시간은 {sunriseTime}이고, 일몰 시간은 {sunsetTime}입니다.")
print(f"바다의 물결은 남해 앞바다 {southOceanWave}m, 동해 앞바다 {eastOceanWave}m, 서해 앞바다 {westOceanWave}m 높이로 일겠습니다.")
print(f"지금까지 {dateDay} {daydate}요일 날씨 예보였습니다.")

print("-------------------")
print(f'내일 날씨예보입니다.\n {daydate}요일인 {dateDay}의 아침 최저 기온은 {lowestTem}도, 낮 촤고 기온은 {highesetTem}도로 예보됐습니다.'
      ,f'\n비올 확률은 {rainingPercentage}%이고, 미세먼지는 {fineDustStatue} 수준일 것으로 예상됩니다. 일출 시간은 {sunriseTime}이고,'
      ,f'일몰 시간은 {sunsetTime}입니다.'
      ,f'\n바다의 물결은 남해 앞바다 {southOceanWave}m, 동해 앞바다 {eastOceanWave}m, 서해 앞바다 {westOceanWave}m 높이로 일겠습니다.'
      ,f'\n지금까지 {dateDay} {daydate}요일 날씨 예보였습니다.')