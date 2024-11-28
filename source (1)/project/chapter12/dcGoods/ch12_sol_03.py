import dcGoods as dg

if __name__ == '__main__':
    flag = True
    goodPrices = []

    while flag:
        
        purchase = int(input('상품을 구매 하시겠습니까? 1.구매, 2.종료 '))
        
        if purchase == 1:
            price = int(input('구매한 상품의 금액을 입력하세요. '))
            goodPrices.append(price)
        elif purchase == 2:
            result = dg.calcTotalPrice(goodPrices)
            flag = False

    print('할인율 : ', result[0], '%')
    print('총합계 : ', result[1], '원')
