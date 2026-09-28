class PagamentoPix:

    def processar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de pagamento inválido.")

        return {
            "forma": "Pix",
            "status": "aprovado",
            "valor": valor,
        }