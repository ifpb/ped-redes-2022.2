class Produto:
    def __init__(self, valor: float, descricao: str, codigo: int=""):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self) -> None:
        self.valor_total = 0.0
        self.itens = []

    def adicionar_item(self, item: ItemPedido):
        self.valor_total += ( item.produto.valor * item.quantidade )
        self.itens.append(item)

    def remover_item(self, item: ItemPedido):
        self.valor_total -= ( item.produto.valor * item.quantidade )
        self.itens.remove(item)

    def obter_total(self):
        return self.valor_total

if __name__ == '__main__':
    produto1 = Produto(50.00, "Galão de combustível")
    produto2 = Produto(120.00, "Camisa do Vasco")
    produto3 = Produto(400.00, "Camisa do Corinthians")
    produto4 = Produto(10.00, "Camisa do Flamengo")
    produto5 = Produto(2.00, "Caixa de Fósforo")

    print("Pedido 1: ")
    pedido = Pedido()
    pedido.adicionar_item(ItemPedido(produto3, 5))
    print(f"R$: {pedido.obter_total():.2f}")

    print("Pedido 2: ")
    p2 = Pedido()
    item1 = ItemPedido(produto4, 1000)
    p2.adicionar_item(item1)
    p2.adicionar_item(ItemPedido(produto5, 10))
    p2.adicionar_item(ItemPedido(produto1, 1))
    print(f"R$ {p2.obter_total():.2f}")