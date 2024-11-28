/* 
 * num1     num2   
 * 3        7 
 * if 시작 :
 * 4 <=5 || 7>=5 1||1 True  ; print num1> 
 * num1 4
 * num2 8
 * 
 * print 출력문
 * 4
 * 8
 */

public class Problem{
    public static void main(String[] args) {
        int num1 = 3;
        int num2 = 7;
        
        if (++num1 <=5 || num2++ >=5)
        System.out.println(num1);
        System.out.println(num2);
    }
}