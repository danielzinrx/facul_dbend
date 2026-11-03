"""
BACKUP DO CÓDIGO COM BUGS PARA A DEMONSTRAÇÃO AO VIVO
Para resetar o arquivo antes da sua apresentação, rode no terminal:
cp order_service_buggy.py order_service.py
"""

class Item:
    def __init__(self, id: int, nome: str, preco: float, estoque: int):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


class PedidoService:
    def __init__(self):
        self.catalogo = {}

    def adicionar_produto_catalogo(self, item: Item):
        self.catalogo[item.id] = item

    def calcular_total_pedido(self, itens_pedido: list[dict], cupom_desconto: float = 0.0, frete: float = 0.0) -> float:
        subtotal = 0.0
        
        for entrada in itens_pedido:
            item_id = entrada["item_id"]
            qtd = entrada["quantidade"]
            
            if item_id not in self.catalogo:
                raise ValueError(f"Produto {item_id} não encontrado no catálogo.")
            
            item = self.catalogo[item_id]
            
            # BUG: Validação invertida e sem checar quantidade <= 0
            if item.estoque > qtd:
                raise ValueError(f"Estoque insuficiente para o produto '{item.nome}'.")
                
            subtotal += item.preco * qtd

        # BUG: Frete recebe desconto indevido e não valida cupom > 1.0 ou < 0.0
        total = (subtotal + frete) * (1 - cupom_desconto)
        
        return total

