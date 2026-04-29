import java.util.Scanner;

public class diaria{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Quantos dias você/vocês permaneceram no hotel? ");
        int diasNoHotel = input.nextInt();

        System.out.println("Qual a categoria do quarto? (Standard/Master/Delux) ");
        char categoriaQuarto = input.next().charAt(0);

        System.out.println("Qual a tipo do quarto? (Solteiro/Duplo/Casal) ");
        char tipoQuarto = input.next().charAt(0);

        final double diariaFixa = 120;
        final double desconto = 120;
        double valorTotalDaDiaria = diasNoHotel * diariaFixa;

        if (valorTotalDaDiaria > 600 && (tipoQuarto == 'D' || tipoQuarto == 'C') && categoriaQuarto == 'C') {
            valorTotalDaDiaria = valorTotalDaDiaria - desconto;
        }
        input.close();
    }
}