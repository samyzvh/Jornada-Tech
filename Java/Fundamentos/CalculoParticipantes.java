import java.util.Scanner;

public class CalculoParticipantes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Qual a quantidade de participantes associados? ");
        int participantesAss = scanner.nextInt();

        System.out.print("Qual a quantidade de participantes não associados? ");
        int participantesNass = scanner.nextInt();

        double valorAss = participantesAss * 100.0;
        double valorNass = participantesNass * 150.0;
        double valorTotal = valorAss + valorNass;

        System.out.printf("O valor total apurado dos associados e não associados é de %.2f reais%n", valorTotal);

//        tarara

        scanner.close();
    }
}
