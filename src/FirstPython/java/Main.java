class Main {
    public static void main(String[] args) {
        String t1 = "4_1a2";
        String t2 = "5-5?3";
        int res = 0;
                        //0,1,2,3,4
        for (int i = 0; i<5 ; i++){
            try{
                res+= Character.getNumericValue( //interger형으로 바꾸면 res += 3 (3)
                    t2.charAt((Character.getNumericValue((t1.charAt(i))))) //= t2.charAt = "3" (2)
                );            //character 이  //integer으로 바꿈 =4 (1)
            } catch (Exception e){ //숫자로 바꾸지 못하는 구문이 나오면 에러 문 실행
                res -=1;
            } finally { //finally는 에러와 상관없이 실행
                res += 1;
            }
        }
        System.out.printf("%d",res);
    }
}

/*   i  res  catch    try_res
    0   3               4
    1        3          4
    2        3          4
    3        3          4
    4   5+4             10 */