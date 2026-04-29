import java.util.Scanner;

public class refeicaoRestaurante{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Quantas refeições foram consumidas? ");
        int quantidadeRefeicao = input.nextInt();

        final double precoFixoPorRefeicao = 18;
        final double desconto = 30;
        double precoTotalDaRefeicao = quantidadeRefeicao * precoFixoPorRefeicao;

        if (precoTotalDaRefeicao > 360) {
        precoTotalDaRefeicao = precoTotalDaRefeicao - desconto;
        }
    
        System.out.printf("O valore total do consumo foi de %.2f", precoTotalDaRefeicao);

        input.close();
    }
}