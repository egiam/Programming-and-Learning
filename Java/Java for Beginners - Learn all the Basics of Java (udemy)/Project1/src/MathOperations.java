public class MathOperations {

    public static void main(String[] Args){
        System.out.println(10*5);
        System.out.println(10/5);
        System.out.println(10-5);
        System.out.println(10+5);

        double var1 = 5;
        double var2 = 7;
        double var3 = 10;
        double var4 = 20;
        double var5 = var1 / var2;
        double var6 = var3 * var4;

        String str1 = "I have ";
        String str2 = " things";

        double total;

        if (var5 < 1) {
            total = var5 + var6;
            System.out.println("Menor a 1");
        }
        else {
            total = var5 - var6;
            System.out.println("Mayor a 1");
        }

        System.out.print(str1);
        System.out.print(total);
        System.out.print(str2);

    }

}
