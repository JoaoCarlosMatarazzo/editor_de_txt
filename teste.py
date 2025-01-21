def remover_subtexto(texto, sub_texto):
    return texto.replace(sub_texto,"")

texto = "Safira é linda como uma joia"    
sub_texto ="linda como "
resultado = remover_subtexto(texto, sub_texto)
print(resultado)
    
    
    
    
    