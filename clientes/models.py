from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=20)

    def __str__(self):
        return self.num_doc

class Pessoas(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    foto = models.ImageField(upload_to='fotos_pessoas', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Pessoas, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero