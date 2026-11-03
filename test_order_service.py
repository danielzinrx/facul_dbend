import unittest
from order_service import PedidoService, Item

class TestPedidoService(unittest.TestCase):
    def setUp(self):
        self.service = PedidoService()
        self.item_a = Item(id=1, nome="Teclado Mecânico", preco=200.0, estoque=10)
        self.item_b = Item(id=2, nome="Mouse Gamer", preco=100.0, estoque=5)
        
        self.service.adicionar_produto_catalogo(self.item_a)
        self.service.adicionar_produto_catalogo(self.item_b)

    def test_calculo_pedido_simples(self):
        """Deve calcular subtotal sem cupom e sem frete corretamente."""
        itens = [{"item_id": 1, "quantidade": 2}] # 2 x 200 = 400
        total = self.service.calcular_total_pedido(itens)
        self.assertEqual(total, 400.0)

    def test_estoque_insuficiente(self):
        """Deve disparar ValueError se pedir mais do que há em estoque."""
        itens = [{"item_id": 2, "quantidade": 10}] # tem 5 em estoque
        with self.assertRaises(ValueError) as ctx:
            self.service.calcular_total_pedido(itens)
        self.assertIn("Estoque insuficiente", str(ctx.exception))

    def test_quantidade_invalida(self):
        """Deve disparar ValueError se quantidade for menor ou igual a zero."""
        itens = [{"item_id": 1, "quantidade": 0}]
        with self.assertRaises(ValueError):
            self.service.calcular_total_pedido(itens)

    def test_desconto_e_frete(self):
        """
        O desconto percentual só incide sobre os produtos (subtotal).
        O frete não recebe desconto.
        Exemplo: 2 * 100 = 200 de subtotal.
        Cupom 10% (0.10) => R$ 180 em produtos.
        Frete de R$ 20 => Total final = R$ 200.00
        """
        itens = [{"item_id": 2, "quantidade": 2}] # 200
        total = self.service.calcular_total_pedido(itens, cupom_desconto=0.10, frete=20.0)
        self.assertEqual(total, 200.0)

    def test_cupom_invalido(self):
        """Cupom negativo ou acima de 100% (1.0) deve ser rejeitado."""
        itens = [{"item_id": 1, "quantidade": 1}]
        with self.assertRaises(ValueError):
            self.service.calcular_total_pedido(itens, cupom_desconto=1.5)

if __name__ == "__main__":
    unittest.main()

