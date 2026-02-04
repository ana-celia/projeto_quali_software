from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=250)
    nacionalidade = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    nome = models.CharField(max_length=250)
    sinopse = models.CharField(max_length=500)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    dataHoraEmprestimo = models.DateTimeField()
    dataHoraDevolucao = models.DateTimeField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.livro.nome} emprestado para {self.usuario.nome}"

class Reserva(models.Model):
    dataHoraReserva= models.DateTimeField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.livro.nome} reserva para {self.usuario.nome}"
    