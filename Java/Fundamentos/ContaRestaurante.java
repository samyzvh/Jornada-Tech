import java.util.Scanner;

public class ContaRestaurante {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Valor do consumo de alimento: ");
        double alimento = scanner.nextDouble();
        System.out.print("Valor do consumo de bebida: ");
        double bebida = scanner.nextDouble();
        System.out.print("Valor do couvert artístico: ");
        double couvert = scanner.nextDouble();

        System.out.print("Quantidade de homens: ");
        int numHomens = scanner.nextInt();
        System.out.print("Quantidade de mulheres: ");
        int numMulheres = scanner.nextInt();
        System.out.print("Quantidade de crianças: ");
        int numCriancas = scanner.nextInt();

        double valorConsumo = alimento + bebida;
        double taxaServico = valorConsumo * 0.10;
        double valorTotal = valorConsumo + taxaServico + couvert;

        double totalPartes = (numHomens * 4) + (numMulheres * 2) + (numCriancas * 1);
        double valorBase = valorTotal / totalPartes;

        double pagoHomem = valorBase * 4;
        double pagoMulher = valorBase * 2;
        double pagoCrianca = valorBase;

        System.out.println("\n--- Resumo da Conta ---");
        System.out.printf("Valor do consumo: R$ %.2f%n", valorConsumo);
        System.out.printf("Taxa de serviço (10%%): R$ %.2f%n", taxaServico);
        System.out.printf("Valor total: R$ %.2f%n", valorTotal);
        System.out.println("--- Valor por pessoa ---");
        System.out.printf("Cada homem deve pagar: R$ %.2f%n", pagoHomem);
        System.out.printf("Cada mulher deve pagar: R$ %.2f%n", pagoMulher);
        System.out.printf("Cada criança deve pagar: R$ %.2f%n", pagoCrianca);

        scanner.close();
    } 
}
