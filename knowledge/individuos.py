def crear_individuos(onto):
    # ============= NUTRIENTES =============
    proteina_nutriente = onto.Nutriente("Nutriente_Proteina")
    carbohidrato_nutriente = onto.Nutriente("Nutriente_Carbohidrato")
    fibra = onto.Nutriente("Fibra")
    vitaminas = onto.Nutriente("Vitaminas")
    minerales = onto.Nutriente("Minerales")
    grasas_saludables = onto.Nutriente("GrasasSaludables")
    grasas_saturadas = onto.Nutriente("GrasasSaturadas")
    producto_animal = onto.Nutriente("ProductoAnimal")
    gluten = onto.Nutriente("Gluten")
    lactosa = onto.Nutriente("Lactosa")
    azucar = onto.Nutriente("Azucar")
    sodio = onto.Nutriente("Sodio")
    omega3 = onto.Nutriente("Omega3")
    antioxidantes = onto.Nutriente("Antioxidantes")

    # ============= RESTRICCIONES =============
    rest_vegetariano = onto.Vegetariano("RestriccionVegetariano")
    rest_vegano = onto.Vegano("RestriccionVegano")
    rest_sin_gluten = onto.SinGluten("RestriccionSinGluten")
    rest_sin_lactosa = onto.SinLactosa("RestriccionSinLactosa")
    rest_diabetico = onto.Diabetico("RestriccionDiabetico")
    rest_hipertenso = onto.Hipertenso("RestriccionHipertenso")

    # ============= OBJETIVOS =============
    obj_perder_peso = onto.Objetivo("PerderPeso")
    obj_ganar_musculo = onto.Objetivo("GanarMusculo")
    obj_mantenimiento = onto.Objetivo("Mantenimiento")
    obj_energia = onto.Objetivo("AumentarEnergia")
    obj_salud_cardiovascular = onto.Objetivo("SaludCardiovascular")

    # ============= CARNES Y AVES =============
    pollo = onto.Proteina("Pollo")
    pollo.calorias = 165
    pollo.proteinas_gramos = 31.0
    pollo.contiene = [proteina_nutriente, producto_animal]
    pollo.incompatibleCon = [rest_vegetariano, rest_vegano]
    pollo.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    pavo = onto.Proteina("Pavo")
    pavo.calorias = 135
    pavo.proteinas_gramos = 30.0
    pavo.contiene = [proteina_nutriente, producto_animal]
    pavo.incompatibleCon = [rest_vegetariano, rest_vegano]
    pavo.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    res = onto.Proteina("CarneRes")
    res.calorias = 250
    res.proteinas_gramos = 26.0
    res.contiene = [proteina_nutriente, producto_animal, minerales, grasas_saturadas]
    res.incompatibleCon = [rest_vegetariano, rest_vegano]
    res.apropiado_para = [obj_ganar_musculo]

    cerdo = onto.Proteina("CarneCerdo")
    cerdo.calorias = 242
    cerdo.proteinas_gramos = 27.0
    cerdo.contiene = [proteina_nutriente, producto_animal]
    cerdo.incompatibleCon = [rest_vegetariano, rest_vegano]
    cerdo.apropiado_para = [obj_ganar_musculo]

    cordero = onto.Proteina("Cordero")
    cordero.calorias = 294
    cordero.proteinas_gramos = 25.0
    cordero.contiene = [proteina_nutriente, producto_animal, grasas_saturadas]
    cordero.incompatibleCon = [rest_vegetariano, rest_vegano]
    cordero.apropiado_para = [obj_ganar_musculo]

    pato = onto.Proteina("Pato")
    pato.calorias = 337
    pato.proteinas_gramos = 19.0
    pato.contiene = [proteina_nutriente, producto_animal, grasas_saturadas]
    pato.incompatibleCon = [rest_vegetariano, rest_vegano]
    pato.apropiado_para = [obj_ganar_musculo]

    cuy = onto.Proteina("Cuy")
    cuy.calorias = 160
    cuy.proteinas_gramos = 20.0
    cuy.contiene = [proteina_nutriente, producto_animal]
    cuy.incompatibleCon = [rest_vegetariano, rest_vegano]
    cuy.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    conejo = onto.Proteina("Conejo")
    conejo.calorias = 173
    conejo.proteinas_gramos = 33.0
    conejo.contiene = [proteina_nutriente, producto_animal]
    conejo.incompatibleCon = [rest_vegetariano, rest_vegano]
    conejo.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    # ============= PESCADOS =============
    bonito = onto.Proteina("Bonito")
    bonito.calorias = 168
    bonito.proteinas_gramos = 26.0
    bonito.contiene = [proteina_nutriente, producto_animal, omega3]
    bonito.incompatibleCon = [rest_vegetariano, rest_vegano]
    bonito.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    jurel = onto.Proteina("Jurel")
    jurel.calorias = 158
    jurel.proteinas_gramos = 22.0
    jurel.contiene = [proteina_nutriente, producto_animal, omega3]
    jurel.incompatibleCon = [rest_vegetariano, rest_vegano]
    jurel.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    caballa = onto.Proteina("Caballa")
    caballa.calorias = 205
    caballa.proteinas_gramos = 19.0
    caballa.contiene = [proteina_nutriente, producto_animal, omega3]
    caballa.incompatibleCon = [rest_vegetariano, rest_vegano]
    caballa.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    anchoveta = onto.Proteina("Anchoveta")
    anchoveta.calorias = 131
    anchoveta.proteinas_gramos = 21.0
    anchoveta.contiene = [proteina_nutriente, producto_animal, omega3, minerales]
    anchoveta.incompatibleCon = [rest_vegetariano, rest_vegano]
    anchoveta.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    corvina = onto.Proteina("Corvina")
    corvina.calorias = 97
    corvina.proteinas_gramos = 18.0
    corvina.contiene = [proteina_nutriente, producto_animal]
    corvina.incompatibleCon = [rest_vegetariano, rest_vegano]
    corvina.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    lenguado = onto.Proteina("Lenguado")
    lenguado.calorias = 91
    lenguado.proteinas_gramos = 19.0
    lenguado.contiene = [proteina_nutriente, producto_animal]
    lenguado.incompatibleCon = [rest_vegetariano, rest_vegano]
    lenguado.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    pejerrey = onto.Proteina("Pejerrey")
    pejerrey.calorias = 105
    pejerrey.proteinas_gramos = 19.0
    pejerrey.contiene = [proteina_nutriente, producto_animal]
    pejerrey.incompatibleCon = [rest_vegetariano, rest_vegano]
    pejerrey.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    trucha = onto.Proteina("Trucha")
    trucha.calorias = 148
    trucha.proteinas_gramos = 20.0
    trucha.contiene = [proteina_nutriente, producto_animal, omega3]
    trucha.incompatibleCon = [rest_vegetariano, rest_vegano]
    trucha.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    paiche = onto.Proteina("Paiche")
    paiche.calorias = 96
    paiche.proteinas_gramos = 21.0
    paiche.contiene = [proteina_nutriente, producto_animal]
    paiche.incompatibleCon = [rest_vegetariano, rest_vegano]
    paiche.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    salmon = onto.Proteina("Salmon")
    salmon.calorias = 208
    salmon.proteinas_gramos = 20.0
    salmon.contiene = [proteina_nutriente, producto_animal, grasas_saludables, omega3]
    salmon.incompatibleCon = [rest_vegetariano, rest_vegano]
    salmon.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    atun = onto.Proteina("Atun")
    atun.calorias = 144
    atun.proteinas_gramos = 30.0
    atun.contiene = [proteina_nutriente, producto_animal, omega3]
    atun.incompatibleCon = [rest_vegetariano, rest_vegano]
    atun.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    # ============= MARISCOS =============
    camarones = onto.Proteina("Camarones")
    camarones.calorias = 99
    camarones.proteinas_gramos = 24.0
    camarones.contiene = [proteina_nutriente, producto_animal, minerales]
    camarones.incompatibleCon = [rest_vegetariano, rest_vegano]
    camarones.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    langostinos = onto.Proteina("Langostinos")
    langostinos.calorias = 106
    langostinos.proteinas_gramos = 24.0
    langostinos.contiene = [proteina_nutriente, producto_animal, minerales]
    langostinos.incompatibleCon = [rest_vegetariano, rest_vegano]
    langostinos.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    conchas_abanico = onto.Proteina("ConchasAbanico")
    conchas_abanico.calorias = 88
    conchas_abanico.proteinas_gramos = 17.0
    conchas_abanico.contiene = [proteina_nutriente, producto_animal, minerales]
    conchas_abanico.incompatibleCon = [rest_vegetariano, rest_vegano]
    conchas_abanico.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    choros = onto.Proteina("Choros")
    choros.calorias = 86
    choros.proteinas_gramos = 12.0
    choros.contiene = [proteina_nutriente, producto_animal, minerales]
    choros.incompatibleCon = [rest_vegetariano, rest_vegano]
    choros.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    pulpo = onto.Proteina("Pulpo")
    pulpo.calorias = 82
    pulpo.proteinas_gramos = 15.0
    pulpo.contiene = [proteina_nutriente, producto_animal]
    pulpo.incompatibleCon = [rest_vegetariano, rest_vegano]
    pulpo.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    pota = onto.Proteina("Pota")
    pota.calorias = 92
    pota.proteinas_gramos = 16.0
    pota.contiene = [proteina_nutriente, producto_animal]
    pota.incompatibleCon = [rest_vegetariano, rest_vegano]
    pota.apropiado_para = [obj_perder_peso, obj_ganar_musculo]

    # ============= HUEVOS Y LÁCTEOS =============
    huevos = onto.Proteina("Huevos")
    huevos.calorias = 155
    huevos.proteinas_gramos = 13.0
    huevos.contiene = [proteina_nutriente, producto_animal, vitaminas]
    huevos.incompatibleCon = [rest_vegano]
    huevos.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    huevos_codorniz = onto.Proteina("HuevosCoderniz")
    huevos_codorniz.calorias = 158
    huevos_codorniz.proteinas_gramos = 13.0
    huevos_codorniz.contiene = [proteina_nutriente, producto_animal, vitaminas]
    huevos_codorniz.incompatibleCon = [rest_vegano]
    huevos_codorniz.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    leche = onto.Lacteo("Leche")
    leche.calorias = 61
    leche.proteinas_gramos = 3.2
    leche.contiene = [proteina_nutriente, lactosa, producto_animal, minerales]
    leche.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    leche.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    yogurt = onto.Lacteo("Yogurt")
    yogurt.calorias = 59
    yogurt.proteinas_gramos = 10.0
    yogurt.contiene = [proteina_nutriente, lactosa, producto_animal]
    yogurt.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    yogurt.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    queso_fresco = onto.Lacteo("QuesoFresco")
    queso_fresco.calorias = 264
    queso_fresco.proteinas_gramos = 21.0
    queso_fresco.contiene = [proteina_nutriente, lactosa, producto_animal]
    queso_fresco.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    queso_fresco.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    mantequilla = onto.Grasa("Mantequilla")
    mantequilla.calorias = 717
    mantequilla.proteinas_gramos = 0.9
    mantequilla.contiene = [grasas_saturadas, lactosa, producto_animal]
    mantequilla.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    mantequilla.apropiado_para = [obj_ganar_musculo]

    # ============= MENESTRAS Y LEGUMBRES =============
    frijol_canario = onto.Proteina("FrijolCanario")
    frijol_canario.calorias = 347
    frijol_canario.proteinas_gramos = 21.0
    frijol_canario.contiene = [proteina_nutriente, fibra, minerales]
    frijol_canario.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    frijol_castilla = onto.Proteina("FrijolCastilla")
    frijol_castilla.calorias = 336
    frijol_castilla.proteinas_gramos = 24.0
    frijol_castilla.contiene = [proteina_nutriente, fibra, minerales]
    frijol_castilla.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    frijol_panamito = onto.Proteina("FrijolPanamito")
    frijol_panamito.calorias = 341
    frijol_panamito.proteinas_gramos = 22.0
    frijol_panamito.contiene = [proteina_nutriente, fibra, minerales]
    frijol_panamito.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    lentejas = onto.Proteina("Lentejas")
    lentejas.calorias = 116
    lentejas.proteinas_gramos = 9.0
    lentejas.contiene = [proteina_nutriente, fibra, minerales]
    lentejas.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    garbanzos = onto.Proteina("Garbanzos")
    garbanzos.calorias = 364
    garbanzos.proteinas_gramos = 19.0
    garbanzos.contiene = [proteina_nutriente, fibra, minerales]
    garbanzos.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    pallares = onto.Proteina("Pallares")
    pallares.calorias = 338
    pallares.proteinas_gramos = 21.0
    pallares.contiene = [proteina_nutriente, fibra, minerales]
    pallares.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    arvejas_secas = onto.Proteina("ArvejasSecas")
    arvejas_secas.calorias = 341
    arvejas_secas.proteinas_gramos = 25.0
    arvejas_secas.contiene = [proteina_nutriente, fibra, minerales]
    arvejas_secas.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    habas = onto.Proteina("Habas")
    habas.calorias = 341
    habas.proteinas_gramos = 26.0
    habas.contiene = [proteina_nutriente, fibra, minerales]
    habas.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    tarwi = onto.Proteina("Tarwi")
    tarwi.calorias = 371
    tarwi.proteinas_gramos = 44.0
    tarwi.contiene = [proteina_nutriente, fibra, grasas_saludables]
    tarwi.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    # ============= CEREALES Y GRANOS ANDINOS =============
    arroz_blanco = onto.Carbohidrato("ArrozBlanco")
    arroz_blanco.calorias = 130
    arroz_blanco.proteinas_gramos = 2.7
    arroz_blanco.contiene = [carbohidrato_nutriente]
    arroz_blanco.apropiado_para = [obj_ganar_musculo, obj_energia]

    arroz_integral = onto.Carbohidrato("ArrozIntegral")
    arroz_integral.calorias = 112
    arroz_integral.proteinas_gramos = 2.6
    arroz_integral.contiene = [carbohidrato_nutriente, fibra]
    arroz_integral.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    quinua = onto.Carbohidrato("Quinua")
    quinua.calorias = 368
    quinua.proteinas_gramos = 14.0
    quinua.contiene = [carbohidrato_nutriente, proteina_nutriente, fibra, minerales]
    quinua.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    kiwicha = onto.Carbohidrato("Kiwicha")
    kiwicha.calorias = 371
    kiwicha.proteinas_gramos = 13.0
    kiwicha.contiene = [carbohidrato_nutriente, proteina_nutriente, fibra, minerales]
    kiwicha.apropiado_para = [obj_ganar_musculo, obj_energia]

    cañihua = onto.Carbohidrato("Cañihua")
    cañihua.calorias = 350
    cañihua.proteinas_gramos = 15.0
    cañihua.contiene = [carbohidrato_nutriente, proteina_nutriente, fibra, minerales]
    cañihua.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    avena = onto.Carbohidrato("Avena")
    avena.calorias = 389
    avena.proteinas_gramos = 17.0
    avena.contiene = [carbohidrato_nutriente, fibra, proteina_nutriente]
    avena.apropiado_para = [obj_energia, obj_mantenimiento]

    cebada = onto.Carbohidrato("Cebada")
    cebada.calorias = 354
    cebada.proteinas_gramos = 12.0
    cebada.contiene = [carbohidrato_nutriente, fibra, gluten]
    cebada.incompatibleCon = [rest_sin_gluten]
    cebada.apropiado_para = [obj_mantenimiento, obj_energia]

    trigo = onto.Carbohidrato("Trigo")
    trigo.calorias = 339
    trigo.proteinas_gramos = 13.0
    trigo.contiene = [carbohidrato_nutriente, fibra, gluten]
    trigo.incompatibleCon = [rest_sin_gluten]
    trigo.apropiado_para = [obj_ganar_musculo, obj_energia]

    maiz_morado = onto.Carbohidrato("MaizMorado")
    maiz_morado.calorias = 365
    maiz_morado.proteinas_gramos = 9.0
    maiz_morado.contiene = [carbohidrato_nutriente, antioxidantes]
    maiz_morado.apropiado_para = [obj_energia, obj_salud_cardiovascular]

    maiz_choclo = onto.Carbohidrato("MaizChoclo")
    maiz_choclo.calorias = 86
    maiz_choclo.proteinas_gramos = 3.3
    maiz_choclo.contiene = [carbohidrato_nutriente, fibra]
    maiz_choclo.apropiado_para = [obj_energia, obj_mantenimiento]

    cancha = onto.Carbohidrato("Cancha")
    cancha.calorias = 346
    cancha.proteinas_gramos = 8.0
    cancha.contiene = [carbohidrato_nutriente, fibra]
    cancha.apropiado_para = [obj_energia, obj_mantenimiento]

    # ============= TUBÉRCULOS Y RAÍCES =============
    papa_blanca = onto.Carbohidrato("PapaBlanca")
    papa_blanca.calorias = 77
    papa_blanca.proteinas_gramos = 2.0
    papa_blanca.contiene = [carbohidrato_nutriente, vitaminas]
    papa_blanca.apropiado_para = [obj_ganar_musculo, obj_energia]

    papa_amarilla = onto.Carbohidrato("PapaAmarilla")
    papa_amarilla.calorias = 83
    papa_amarilla.proteinas_gramos = 2.1
    papa_amarilla.contiene = [carbohidrato_nutriente, vitaminas]
    papa_amarilla.apropiado_para = [obj_ganar_musculo, obj_energia]

    papa_huayro = onto.Carbohidrato("PapaHuayro")
    papa_huayro.calorias = 79
    papa_huayro.proteinas_gramos = 2.0
    papa_huayro.contiene = [carbohidrato_nutriente, vitaminas]
    papa_huayro.apropiado_para = [obj_ganar_musculo, obj_energia]

    camote = onto.Carbohidrato("Camote")
    camote.calorias = 86
    camote.proteinas_gramos = 1.6
    camote.contiene = [carbohidrato_nutriente, fibra, vitaminas]
    camote.apropiado_para = [obj_ganar_musculo, obj_energia]

    yuca = onto.Carbohidrato("Yuca")
    yuca.calorias = 159
    yuca.proteinas_gramos = 1.4
    yuca.contiene = [carbohidrato_nutriente, fibra]
    yuca.apropiado_para = [obj_ganar_musculo, obj_energia]

    oca = onto.Carbohidrato("Oca")
    oca.calorias = 61
    oca.proteinas_gramos = 1.0
    oca.contiene = [carbohidrato_nutriente, vitaminas]
    oca.apropiado_para = [obj_mantenimiento, obj_energia]

    olluco = onto.Carbohidrato("Olluco")
    olluco.calorias = 74
    olluco.proteinas_gramos = 1.5
    olluco.contiene = [carbohidrato_nutriente, vitaminas]
    olluco.apropiado_para = [obj_mantenimiento, obj_energia]

    mashua = onto.Carbohidrato("Mashua")
    mashua.calorias = 52
    mashua.proteinas_gramos = 1.2
    mashua.contiene = [carbohidrato_nutriente, vitaminas]
    mashua.apropiado_para = [obj_mantenimiento, obj_energia]

    arracacha = onto.Carbohidrato("Arracacha")
    arracacha.calorias = 101
    arracacha.proteinas_gramos = 0.8
    arracacha.contiene = [carbohidrato_nutriente, vitaminas]
    arracacha.apropiado_para = [obj_energia, obj_mantenimiento]

    dale_dale = onto.Carbohidrato("DaleDale")
    dale_dale.calorias = 118
    dale_dale.proteinas_gramos = 1.0
    dale_dale.contiene = [carbohidrato_nutriente]
    dale_dale.apropiado_para = [obj_energia, obj_ganar_musculo]

    # ============= VEGETALES =============
    tomate = onto.Vegetal("Tomate")
    tomate.calorias = 18
    tomate.proteinas_gramos = 0.9
    tomate.contiene = [vitaminas, antioxidantes]
    tomate.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    cebolla = onto.Vegetal("Cebolla")
    cebolla.calorias = 40
    cebolla.proteinas_gramos = 1.1
    cebolla.contiene = [vitaminas, antioxidantes]
    cebolla.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    ajo = onto.Vegetal("Ajo")
    ajo.calorias = 149
    ajo.proteinas_gramos = 6.4
    ajo.contiene = [antioxidantes, minerales]
    ajo.apropiado_para = [obj_salud_cardiovascular, obj_mantenimiento]

    zanahoria = onto.Vegetal("Zanahoria")
    zanahoria.calorias = 41
    zanahoria.proteinas_gramos = 0.9
    zanahoria.contiene = [fibra, vitaminas]
    zanahoria.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    brocoli = onto.Vegetal("Brocoli")
    brocoli.calorias = 34
    brocoli.proteinas_gramos = 2.8
    brocoli.contiene = [fibra, vitaminas, minerales]
    brocoli.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    coliflor = onto.Vegetal("Coliflor")
    coliflor.calorias = 25
    coliflor.proteinas_gramos = 1.9
    coliflor.contiene = [fibra, vitaminas]
    coliflor.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    lechuga = onto.Vegetal("Lechuga")
    lechuga.calorias = 15
    lechuga.proteinas_gramos = 1.4
    lechuga.contiene = [fibra, vitaminas]
    lechuga.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    espinaca = onto.Vegetal("Espinaca")
    espinaca.calorias = 23
    espinaca.proteinas_gramos = 2.9
    espinaca.contiene = [fibra, vitaminas, minerales]
    espinaca.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    acelga = onto.Vegetal("Acelga")
    acelga.calorias = 19
    acelga.proteinas_gramos = 1.8
    acelga.contiene = [fibra, vitaminas, minerales]
    acelga.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    col = onto.Vegetal("Col")
    col.calorias = 25
    col.proteinas_gramos = 1.3
    col.contiene = [fibra, vitaminas]
    col.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    apio = onto.Vegetal("Apio")
    apio.calorias = 16
    apio.proteinas_gramos = 0.7
    apio.contiene = [fibra, vitaminas]
    apio.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    pepino = onto.Vegetal("Pepino")
    pepino.calorias = 15
    pepino.proteinas_gramos = 0.7
    pepino.contiene = [vitaminas, fibra]
    pepino.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    zapallo = onto.Vegetal("Zapallo")
    zapallo.calorias = 26
    zapallo.proteinas_gramos = 1.0
    zapallo.contiene = [fibra, vitaminas]
    zapallo.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    calabaza = onto.Vegetal("Calabaza")
    calabaza.calorias = 26
    calabaza.proteinas_gramos = 1.0
    calabaza.contiene = [fibra, vitaminas]
    calabaza.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    pimiento = onto.Vegetal("Pimiento")
    pimiento.calorias = 31
    pimiento.proteinas_gramos = 1.0
    pimiento.contiene = [vitaminas, antioxidantes]
    pimiento.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    rocoto = onto.Vegetal("Rocoto")
    rocoto.calorias = 40
    rocoto.proteinas_gramos = 1.9
    rocoto.contiene = [vitaminas, antioxidantes]
    rocoto.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    aji_amarillo = onto.Vegetal("AjiAmarillo")
    aji_amarillo.calorias = 40
    aji_amarillo.proteinas_gramos = 2.0
    aji_amarillo.contiene = [vitaminas, antioxidantes]
    aji_amarillo.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    aji_panca = onto.Vegetal("AjiPanca")
    aji_panca.calorias = 42
    aji_panca.proteinas_gramos = 1.8
    aji_panca.contiene = [vitaminas, antioxidantes]
    aji_panca.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    rabanito = onto.Vegetal("Rabanito")
    rabanito.calorias = 16
    rabanito.proteinas_gramos = 0.7
    rabanito.contiene = [vitaminas, fibra]
    rabanito.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    betarraga = onto.Vegetal("Betarraga")
    betarraga.calorias = 43
    betarraga.proteinas_gramos = 1.6
    betarraga.contiene = [vitaminas, minerales, fibra]
    betarraga.apropiado_para = [obj_mantenimiento, obj_energia]

    nabo = onto.Vegetal("Nabo")
    nabo.calorias = 28
    nabo.proteinas_gramos = 0.9
    nabo.contiene = [fibra, vitaminas]
    nabo.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    vainita = onto.Vegetal("Vainita")
    vainita.calorias = 31
    vainita.proteinas_gramos = 1.8
    vainita.contiene = [fibra, vitaminas]
    vainita.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    arvejas_verdes = onto.Vegetal("ArvejasVerdes")
    arvejas_verdes.calorias = 81
    arvejas_verdes.proteinas_gramos = 5.4
    arvejas_verdes.contiene = [proteina_nutriente, fibra, vitaminas]
    arvejas_verdes.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    choclo = onto.Carbohidrato("Choclo")
    choclo.calorias = 86
    choclo.proteinas_gramos = 3.3
    choclo.contiene = [carbohidrato_nutriente, fibra]
    choclo.apropiado_para = [obj_energia, obj_mantenimiento]

    calabacin = onto.Vegetal("Calabacin")
    calabacin.calorias = 17
    calabacin.proteinas_gramos = 1.2
    calabacin.contiene = [fibra, vitaminas]
    calabacin.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    berenjena = onto.Vegetal("Berenjena")
    berenjena.calorias = 25
    berenjena.proteinas_gramos = 1.0
    berenjena.contiene = [fibra, vitaminas]
    berenjena.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    champiñones = onto.Vegetal("Champiñones")
    champiñones.calorias = 22
    champiñones.proteinas_gramos = 3.1
    champiñones.contiene = [proteina_nutriente, vitaminas, minerales]
    champiñones.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    esparragos = onto.Vegetal("Esparragos")
    esparragos.calorias = 20
    esparragos.proteinas_gramos = 2.2
    esparragos.contiene = [fibra, vitaminas, minerales]
    esparragos.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    alcachofa = onto.Vegetal("Alcachofa")
    alcachofa.calorias = 47
    alcachofa.proteinas_gramos = 3.3
    alcachofa.contiene = [fibra, vitaminas, minerales]
    alcachofa.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    # ============= FRUTAS PERUANAS =============
    platano = onto.Fruta("Platano")
    platano.calorias = 89
    platano.proteinas_gramos = 1.1
    platano.contiene = [carbohidrato_nutriente, vitaminas]
    platano.apropiado_para = [obj_energia, obj_ganar_musculo]

    manzana = onto.Fruta("Manzana")
    manzana.calorias = 52
    manzana.proteinas_gramos = 0.3
    manzana.contiene = [fibra, vitaminas]
    manzana.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    pera = onto.Fruta("Pera")
    pera.calorias = 57
    pera.proteinas_gramos = 0.4
    pera.contiene = [fibra, vitaminas]
    pera.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    naranja = onto.Fruta("Naranja")
    naranja.calorias = 47
    naranja.proteinas_gramos = 0.9
    naranja.contiene = [vitaminas, fibra]
    naranja.apropiado_para = [obj_mantenimiento, obj_energia]

    mandarina = onto.Fruta("Mandarina")
    mandarina.calorias = 53
    mandarina.proteinas_gramos = 0.8
    mandarina.contiene = [vitaminas, fibra]
    mandarina.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    limon = onto.Fruta("Limon")
    limon.calorias = 29
    limon.proteinas_gramos = 1.1
    limon.contiene = [vitaminas, antioxidantes]
    limon.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    papaya = onto.Fruta("Papaya")
    papaya.calorias = 43
    papaya.proteinas_gramos = 0.5
    papaya.contiene = [vitaminas, fibra]
    papaya.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    piña = onto.Fruta("Piña")
    piña.calorias = 50
    piña.proteinas_gramos = 0.5
    piña.contiene = [vitaminas, fibra]
    piña.apropiado_para = [obj_mantenimiento, obj_energia]

    mango = onto.Fruta("Mango")
    mango.calorias = 60
    mango.proteinas_gramos = 0.8
    mango.contiene = [vitaminas, fibra]
    mango.apropiado_para = [obj_energia, obj_mantenimiento]

    sandia = onto.Fruta("Sandia")
    sandia.calorias = 30
    sandia.proteinas_gramos = 0.6
    sandia.contiene = [vitaminas]
    sandia.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    melon = onto.Fruta("Melon")
    melon.calorias = 34
    melon.proteinas_gramos = 0.8
    melon.contiene = [vitaminas]
    melon.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    uvas = onto.Fruta("Uvas")
    uvas.calorias = 69
    uvas.proteinas_gramos = 0.7
    uvas.contiene = [vitaminas, antioxidantes]
    uvas.apropiado_para = [obj_energia, obj_mantenimiento]

    fresas = onto.Fruta("Fresas")
    fresas.calorias = 32
    fresas.proteinas_gramos = 0.7
    fresas.contiene = [vitaminas, fibra, antioxidantes]
    fresas.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    chirimoya = onto.Fruta("Chirimoya")
    chirimoya.calorias = 75
    chirimoya.proteinas_gramos = 1.6
    chirimoya.contiene = [vitaminas, fibra]
    chirimoya.apropiado_para = [obj_energia, obj_mantenimiento]

    lucuma = onto.Fruta("Lucuma")
    lucuma.calorias = 99
    lucuma.proteinas_gramos = 1.5
    lucuma.contiene = [carbohidrato_nutriente, vitaminas, fibra]
    lucuma.apropiado_para = [obj_energia, obj_mantenimiento]

    granadilla = onto.Fruta("Granadilla")
    granadilla.calorias = 97
    granadilla.proteinas_gramos = 2.2
    granadilla.contiene = [vitaminas, fibra]
    granadilla.apropiado_para = [obj_energia, obj_mantenimiento]

    maracuya = onto.Fruta("Maracuya")
    maracuya.calorias = 97
    maracuya.proteinas_gramos = 2.2
    maracuya.contiene = [vitaminas, fibra]
    maracuya.apropiado_para = [obj_energia, obj_mantenimiento]

    tumbo = onto.Fruta("Tumbo")
    tumbo.calorias = 78
    tumbo.proteinas_gramos = 0.8
    tumbo.contiene = [vitaminas, fibra]
    tumbo.apropiado_para = [obj_mantenimiento, obj_energia]

    aguaje = onto.Fruta("Aguaje")
    aguaje.calorias = 283
    aguaje.proteinas_gramos = 3.3
    aguaje.contiene = [vitaminas, grasas_saludables]
    aguaje.apropiado_para = [obj_energia, obj_ganar_musculo]

    camu_camu = onto.Fruta("CamuCamu")
    camu_camu.calorias = 17
    camu_camu.proteinas_gramos = 0.5
    camu_camu.contiene = [vitaminas, antioxidantes]
    camu_camu.apropiado_para = [obj_perder_peso, obj_salud_cardiovascular]

    cocona = onto.Fruta("Cocona")
    cocona.calorias = 36
    cocona.proteinas_gramos = 0.6
    cocona.contiene = [vitaminas, fibra]
    cocona.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    capuli = onto.Fruta("Capuli")
    capuli.calorias = 50
    capuli.proteinas_gramos = 1.0
    capuli.contiene = [vitaminas, antioxidantes]
    capuli.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    tuna = onto.Fruta("Tuna")
    tuna.calorias = 41
    tuna.proteinas_gramos = 0.7
    tuna.contiene = [vitaminas, fibra]
    tuna.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    pepino_dulce = onto.Fruta("PepinoDulce")
    pepino_dulce.calorias = 22
    pepino_dulce.proteinas_gramos = 0.6
    pepino_dulce.contiene = [vitaminas]
    pepino_dulce.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    pacae = onto.Fruta("Pacae")
    pacae.calorias = 68
    pacae.proteinas_gramos = 2.1
    pacae.contiene = [carbohidrato_nutriente, fibra]
    pacae.apropiado_para = [obj_energia, obj_mantenimiento]

    guanabana = onto.Fruta("Guanabana")
    guanabana.calorias = 66
    guanabana.proteinas_gramos = 1.0
    guanabana.contiene = [vitaminas, fibra]
    guanabana.apropiado_para = [obj_mantenimiento, obj_energia]

    # ============= FRUTOS SECOS Y SEMILLAS =============
    mani = onto.Grasa("Mani")
    mani.calorias = 567
    mani.proteinas_gramos = 26.0
    mani.contiene = [grasas_saludables, proteina_nutriente]
    mani.apropiado_para = [obj_ganar_musculo, obj_energia]

    nueces = onto.Grasa("Nueces")
    nueces.calorias = 654
    nueces.proteinas_gramos = 15.0
    nueces.contiene = [grasas_saludables, proteina_nutriente, omega3]
    nueces.apropiado_para = [obj_ganar_musculo, obj_salud_cardiovascular]

    almendras = onto.Grasa("Almendras")
    almendras.calorias = 579
    almendras.proteinas_gramos = 21.0
    almendras.contiene = [grasas_saludables, proteina_nutriente]
    almendras.apropiado_para = [obj_ganar_musculo, obj_energia]

    pecanas = onto.Grasa("Pecanas")
    pecanas.calorias = 691
    pecanas.proteinas_gramos = 9.0
    pecanas.contiene = [grasas_saludables, minerales]
    pecanas.apropiado_para = [obj_ganar_musculo, obj_energia]

    castañas = onto.Grasa("Castañas")
    castañas.calorias = 656
    castañas.proteinas_gramos = 14.0
    castañas.contiene = [grasas_saludables, proteina_nutriente, minerales]
    castañas.apropiado_para = [obj_ganar_musculo, obj_energia]

    pasas = onto.Fruta("Pasas")
    pasas.calorias = 299
    pasas.proteinas_gramos = 3.1
    pasas.contiene = [carbohidrato_nutriente, azucar, fibra]
    pasas.incompatibleCon = [rest_diabetico]
    pasas.apropiado_para = [obj_energia, obj_ganar_musculo]

    # ============= ACEITES Y GRASAS =============
    aceite_oliva = onto.Grasa("AceiteOliva")
    aceite_oliva.calorias = 884
    aceite_oliva.proteinas_gramos = 0.0
    aceite_oliva.contiene = [grasas_saludables]
    aceite_oliva.apropiado_para = [obj_mantenimiento, obj_salud_cardiovascular]

    aceite_vegetal = onto.Grasa("AceiteVegetal")
    aceite_vegetal.calorias = 884
    aceite_vegetal.proteinas_gramos = 0.0
    aceite_vegetal.contiene = [grasas_saludables]
    aceite_vegetal.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    aceite_girasol = onto.Grasa("AceiteGirasol")
    aceite_girasol.calorias = 884
    aceite_girasol.proteinas_gramos = 0.0
    aceite_girasol.contiene = [grasas_saludables]
    aceite_girasol.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    palta = onto.Grasa("Palta")
    palta.calorias = 160
    palta.proteinas_gramos = 2.0
    palta.contiene = [grasas_saludables, fibra, vitaminas]
    palta.apropiado_para = [obj_mantenimiento, obj_salud_cardiovascular]

    aceitunas = onto.Grasa("Aceitunas")
    aceitunas.calorias = 115
    aceitunas.proteinas_gramos = 0.8
    aceitunas.contiene = [grasas_saludables, sodio]
    aceitunas.incompatibleCon = [rest_hipertenso]
    aceitunas.apropiado_para = [obj_mantenimiento]

    # ============= PANES Y HARINAS =============
    pan_frances = onto.Carbohidrato("PanFrances")
    pan_frances.calorias = 265
    pan_frances.proteinas_gramos = 9.0
    pan_frances.contiene = [carbohidrato_nutriente, gluten]
    pan_frances.incompatibleCon = [rest_sin_gluten]
    pan_frances.apropiado_para = [obj_energia, obj_ganar_musculo]

    pan_integral = onto.Carbohidrato("PanIntegral")
    pan_integral.calorias = 247
    pan_integral.proteinas_gramos = 13.0
    pan_integral.contiene = [carbohidrato_nutriente, gluten, fibra]
    pan_integral.incompatibleCon = [rest_sin_gluten]
    pan_integral.apropiado_para = [obj_mantenimiento, obj_energia]

    pan_pita = onto.Carbohidrato("PanPita")
    pan_pita.calorias = 275
    pan_pita.proteinas_gramos = 9.0
    pan_pita.contiene = [carbohidrato_nutriente, gluten]
    pan_pita.incompatibleCon = [rest_sin_gluten]
    pan_pita.apropiado_para = [obj_energia, obj_mantenimiento]

    pan_ciabatta = onto.Carbohidrato("PanCiabatta")
    pan_ciabatta.calorias = 271
    pan_ciabatta.proteinas_gramos = 9.0
    pan_ciabatta.contiene = [carbohidrato_nutriente, gluten]
    pan_ciabatta.incompatibleCon = [rest_sin_gluten]
    pan_ciabatta.apropiado_para = [obj_energia, obj_ganar_musculo]

    chuta = onto.Carbohidrato("Chuta")
    chuta.calorias = 280
    chuta.proteinas_gramos = 8.0
    chuta.contiene = [carbohidrato_nutriente, gluten]
    chuta.incompatibleCon = [rest_sin_gluten]
    chuta.apropiado_para = [obj_energia, obj_ganar_musculo]

    # ============= FIDEOS Y PASTAS =============
    fideos = onto.Carbohidrato("Fideos")
    fideos.calorias = 371
    fideos.proteinas_gramos = 13.0
    fideos.contiene = [carbohidrato_nutriente, gluten]
    fideos.incompatibleCon = [rest_sin_gluten]
    fideos.apropiado_para = [obj_ganar_musculo, obj_energia]

    tallarines = onto.Carbohidrato("Tallarines")
    tallarines.calorias = 371
    tallarines.proteinas_gramos = 13.0
    tallarines.contiene = [carbohidrato_nutriente, gluten]
    tallarines.incompatibleCon = [rest_sin_gluten]
    tallarines.apropiado_para = [obj_ganar_musculo, obj_energia]

    fideo_cabello_angel = onto.Carbohidrato("FideoCabelloAngel")
    fideo_cabello_angel.calorias = 371
    fideo_cabello_angel.proteinas_gramos = 13.0
    fideo_cabello_angel.contiene = [carbohidrato_nutriente, gluten]
    fideo_cabello_angel.incompatibleCon = [rest_sin_gluten]
    fideo_cabello_angel.apropiado_para = [obj_ganar_musculo, obj_energia]

    # ============= SNACKS TRADICIONALES =============
    cancha_serrana = onto.Carbohidrato("CanchaSerrana")
    cancha_serrana.calorias = 346
    cancha_serrana.proteinas_gramos = 8.0
    cancha_serrana.contiene = [carbohidrato_nutriente, fibra]
    cancha_serrana.apropiado_para = [obj_energia, obj_mantenimiento]

    habas_tostadas = onto.Proteina("HabasTostadas")
    habas_tostadas.calorias = 341
    habas_tostadas.proteinas_gramos = 26.0
    habas_tostadas.contiene = [proteina_nutriente, fibra]
    habas_tostadas.apropiado_para = [obj_ganar_musculo, obj_energia]

    chifles = onto.Carbohidrato("Chifles")
    chifles.calorias = 519
    chifles.proteinas_gramos = 2.3
    chifles.contiene = [carbohidrato_nutriente, grasas_saturadas]
    chifles.apropiado_para = [obj_ganar_musculo, obj_energia]

    # ============= BEBIDAS TRADICIONALES =============
    chicha_morada = onto.Carbohidrato("ChichaMorada")
    chicha_morada.calorias = 80
    chicha_morada.proteinas_gramos = 0.5
    chicha_morada.contiene = [carbohidrato_nutriente, azucar, antioxidantes]
    chicha_morada.incompatibleCon = [rest_diabetico]
    chicha_morada.apropiado_para = [obj_energia, obj_mantenimiento]

    emoliente = onto.Vegetal("Emoliente")
    emoliente.calorias = 25
    emoliente.proteinas_gramos = 0.3
    emoliente.contiene = [vitaminas]
    emoliente.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    mate_coca = onto.Vegetal("MateCoca")
    mate_coca.calorias = 2
    mate_coca.proteinas_gramos = 0.0
    mate_coca.contiene = [antioxidantes]
    mate_coca.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    # ============= CONDIMENTOS Y HIERBAS =============
    culantro = onto.Vegetal("Culantro")
    culantro.calorias = 23
    culantro.proteinas_gramos = 2.1
    culantro.contiene = [vitaminas, antioxidantes]
    culantro.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    perejil = onto.Vegetal("Perejil")
    perejil.calorias = 36
    perejil.proteinas_gramos = 3.0
    perejil.contiene = [vitaminas, minerales]
    perejil.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    huacatay = onto.Vegetal("Huacatay")
    huacatay.calorias = 20
    huacatay.proteinas_gramos = 1.5
    huacatay.contiene = [vitaminas, antioxidantes]
    huacatay.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    oregano = onto.Vegetal("Oregano")
    oregano.calorias = 265
    oregano.proteinas_gramos = 9.0
    oregano.contiene = [antioxidantes, minerales]
    oregano.apropiado_para = [obj_mantenimiento, obj_salud_cardiovascular]

    comino = onto.Nutriente("Comino")
    comino.calorias = 375
    comino.proteinas_gramos = 18.0
    comino.contiene = [minerales, antioxidantes]
    comino.apropiado_para = [obj_mantenimiento, obj_salud_cardiovascular]

    palillo = onto.Nutriente("Palillo")
    palillo.calorias = 354
    palillo.proteinas_gramos = 8.0
    palillo.contiene = [antioxidantes]
    palillo.apropiado_para = [obj_mantenimiento, obj_salud_cardiovascular]

    return onto