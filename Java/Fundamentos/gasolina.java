import java.util.Scanner;

public class gasolina{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Qual foi a quantidade em Litro consumida? ");
        int quantidadeLitroGasolina = input.nextInt();
        
        System.out.println("Qual foi o timo da gasolina escolhida? (Aditiva ou Comum) ");
        char tipoGasolina = input.next().charAt(0);

        final double precoFixoGasolina = 6;
        final double desconto = 5;
        double precoTotalGasolina = quantidadeLitroGasolina * precoFixoGasolina;

        if (tipoGasolina == 'A' && precoTotalGasolina > 150) {
            precoTotalGasolina = precoTotalGasolina - desconto;
        }
        
    System.out.printf("O valor total do preço da gasolina é %.2f ", precoTotalGasolina);
    
    input.close();
    }
}