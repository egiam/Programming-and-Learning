import java.util.Scanner;

public class ScannerMethod {

    public static void main(String[] Args){
        System.out.print("Username: ");
        Scanner scan = new Scanner(System.in); //Para escribir en consola
        String txt = scan.next();

        System.out.println("Welcome: " + txt);

        Scanner scan1 = new Scanner(System.in);
        Double dbl = scan1.nextDouble();

        Scanner scan2 = new Scanner(System.in);
        Boolean bool = scan2.nextBoolean();

        System.out.println(dbl + " - " + bool);

    }
}
