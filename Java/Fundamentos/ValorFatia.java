import java.util.Scanner;

public class ValorFatia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quanto custa o quilo da torta? ");
        double quiloTorta = scanner.nextDouble();

        System.out.print("Qual o peso da fatia (em gramas)? ");
        double pesoFatia = scanner.nextDouble();

        double quantidade = 1000 / pesoFatia;
        double valorFatia = quiloTorta / quantidade;

        System.out.printf("O valor dessa fatia custa %.2f reais%n", valorFatia);
        
        scanner.close();
    }
}