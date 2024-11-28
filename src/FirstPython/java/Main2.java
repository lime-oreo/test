class Pos {
    private int x =0, y=0;
    Pos(int x , int y)
    {
        this.x = x;
        this.y= y;
    }
    public int sum() {return x+y;}
    public int sum(int x) {return x+y;}
}

public class Main2{
    public static void main(String[] args) {
        Pos[] list = new Pos[2];
        list[0] = new Pos(1,1);
        list[1] = new Pos(2,2);
        int res = 0;
        for (int i=0; i<list.length; i++)
        res += list[i].sum(i);
        System.out.print(res);
    }
}