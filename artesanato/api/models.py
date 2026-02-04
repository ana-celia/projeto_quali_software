from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.IntegerField()
    redeSocialLink = models.URLField()

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=250)
    nuemero = models.IntegerField()
    bairro = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    cep = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.rua

class Servico(models.Model):
    nome = models.CharField(max_length=250)
    valor = models.FloatField()
    tempoPrevisto = models.DateTimeField()

    def __str__(self):
        return self.nome

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=500)
    taxa = models.FloatField()

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    SITUACAO = (("pg","pago"), ("op", "aberto"), ("cc", "cancelado"))
    situacaoPedido = models.CharField(max_length=250, choices=SITUACAO)
    descricao = models.CharField(max_length=500)
    valorAssociado = models.FloatField()
    valorTotal = models.FloatField()
    taxaExtra = models.FloatField()
    dataRecebimento = models.DateTimeField()
    dataEntrega = models.DateTimeField()
    formaPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    def __str__(self):
        return self.situacaoPedido

class Relacao(models.Model):
    TIPOS = (("ia", "Indicação amigos"), ("if", "Indicação familia"), ("rs", "Redes Sociais"))
    pessoa1 = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="Relacionamento")
    pessoa2 = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=250, choices=TIPOS)
    parentesco = models.CharField(max_length=250)
            
    def __str__(self):
        return f"{self.pessoa1.nome} + {self.pessoa2.nome}"
