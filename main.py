



nome=input("Qual seu nome?")

qtd_frequencia_escolar = float(input(f"Qual a frequência máxima da sua escola {nome}?"))
qtd_frequencia_aluno = float(input(f"Qual foi sua frequêcia escolar {nome}?"))

nota_1_bimestre = float(input("Qual sua nota do primeiro bimestre?"))
nota_2_bimestre = float(input("Qual sua nota do segundo bimetre?"))
nota_3_bimestre = float(input("Qual sua nota do terceiro bimestre?"))
nota_4_bimestre = float(input("Qual sua nota do quarto bimestre?"))

media = (2*nota_1_bimestre + 2*nota_2_bimestre + 4*nota_3_bimestre + 2*nota_4_bimestre)/10
media_frequencia = (100*qtd_frequencia_aluno)/qtd_frequencia_escolar

if media>=7 and media_frequencia >= 70:
    print(f"Parabéns você foi aprovado(a), {nome}, sua média foi de {media}")

elif media >= 1.8 and media_frequencia >=70:
    media_final = float(input(f"Qual foi sua nota na recuperação {nome}?"))
    nota_rec = 7 - media_final
    nota_total = nota_rec + 7

    if media_final > nota_total:
        print (f"Parabéns {nome}, você foi aprovado(a)")


    elif media_final < nota_total:
        not_exame = float(input(f"Qual sua nota no exame {nome}?"))
    
        if not_exame < 4 and media_frequencia:
            print(f"Lamentamos {nome}, mas você foi reprovado(a)")

        else:
            print(f"Parabéns {nome}, você foi aprovado(a)")
        
else:
    print(f"Lamentamos {nome}, você reprovou")
