def crear_individuos(onto):
    proteina_nutriente = onto.Nutriente("Nutriente_Proteina")
    carbohidrato_nutriente = onto.Nutriente("Nutriente_Carbohidrato")
    fibra = onto.Nutriente("Fibra")
    vitaminas = onto.Nutriente("Vitaminas")
    minerales = onto.Nutriente("Minerales")
    grasas_saludables = onto.Nutriente("GrasasSaludables")
    producto_animal = onto.Nutriente("ProductoAnimal")
    gluten = onto.Nutriente("Gluten")
    lactosa = onto.Nutriente("Lactosa")
    azucar = onto.Nutriente("Azucar")

    rest_vegetariano = onto.Vegetariano("RestriccionVegetariano")
    rest_vegano = onto.Vegano("RestriccionVegano")
    rest_sin_gluten = onto.SinGluten("RestriccionSinGluten")
    rest_sin_lactosa = onto.SinLactosa("RestriccionSinLactosa")
    rest_diabetico = onto.Diabetico("RestriccionDiabetico")

    obj_perder_peso = onto.Objetivo("PerderPeso")
    obj_ganar_musculo = onto.Objetivo("GanarMusculo")
    obj_mantenimiento = onto.Objetivo("Mantenimiento")
    obj_energia = onto.Objetivo("AumentarEnergia")

    pollo = onto.Proteina("Pollo")
    pollo.calorias = 165
    pollo.proteinas_gramos = 31.0
    pollo.contiene = [proteina_nutriente, producto_animal]
    pollo.incompatibleCon = [rest_vegetariano, rest_vegano]
    pollo.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    pescado = onto.Proteina("Pescado")
    pescado.calorias = 140
    pescado.proteinas_gramos = 26.0
    pescado.contiene = [proteina_nutriente, producto_animal, grasas_saludables]
    pescado.incompatibleCon = [rest_vegetariano, rest_vegano]
    pescado.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    huevos = onto.Proteina("Huevos")
    huevos.calorias = 155
    huevos.proteinas_gramos = 13.0
    huevos.contiene = [proteina_nutriente, producto_animal]
    huevos.incompatibleCon = [rest_vegano]
    huevos.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    tofu = onto.Proteina("Tofu")
    tofu.calorias = 76
    tofu.proteinas_gramos = 8.0
    tofu.contiene = [proteina_nutriente]
    tofu.apropiado_para = [obj_ganar_musculo, obj_perder_peso, obj_mantenimiento]

    lentejas = onto.Proteina("Lentejas")
    lentejas.calorias = 116
    lentejas.proteinas_gramos = 9.0
    lentejas.contiene = [proteina_nutriente, fibra, minerales]
    lentejas.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    garbanzos = onto.Proteina("Garbanzos")
    garbanzos.calorias = 164
    garbanzos.proteinas_gramos = 8.9
    garbanzos.contiene = [proteina_nutriente, fibra]
    garbanzos.apropiado_para = [obj_mantenimiento, obj_energia]

    arroz_integral = onto.Carbohidrato("ArrozIntegral")
    arroz_integral.calorias = 112
    arroz_integral.proteinas_gramos = 2.6
    arroz_integral.contiene = [carbohidrato_nutriente, fibra]
    arroz_integral.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    quinoa = onto.Carbohidrato("Quinoa")
    quinoa.calorias = 120
    quinoa.proteinas_gramos = 4.4
    quinoa.contiene = [carbohidrato_nutriente, proteina_nutriente, fibra]
    quinoa.apropiado_para = [obj_ganar_musculo, obj_mantenimiento, obj_energia]

    avena = onto.Carbohidrato("Avena")
    avena.calorias = 68
    avena.proteinas_gramos = 2.4
    avena.contiene = [carbohidrato_nutriente, fibra]
    avena.apropiado_para = [obj_energia, obj_mantenimiento]

    papa = onto.Carbohidrato("Papa")
    papa.calorias = 77
    papa.proteinas_gramos = 2.0
    papa.contiene = [carbohidrato_nutriente, vitaminas]
    papa.apropiado_para = [obj_ganar_musculo, obj_energia]

    pan_integral = onto.Carbohidrato("PanIntegral")
    pan_integral.calorias = 247
    pan_integral.proteinas_gramos = 13.0
    pan_integral.contiene = [carbohidrato_nutriente, gluten, fibra]
    pan_integral.incompatibleCon = [rest_sin_gluten]
    pan_integral.apropiado_para = [obj_mantenimiento, obj_energia]

    camote = onto.Carbohidrato("Camote")
    camote.calorias = 86
    camote.proteinas_gramos = 1.6
    camote.contiene = [carbohidrato_nutriente, fibra, vitaminas]
    camote.apropiado_para = [obj_ganar_musculo, obj_energia]

    brocoli = onto.Vegetal("Brocoli")
    brocoli.calorias = 34
    brocoli.proteinas_gramos = 2.8
    brocoli.contiene = [fibra, vitaminas, minerales]
    brocoli.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    espinaca = onto.Vegetal("Espinaca")
    espinaca.calorias = 23
    espinaca.proteinas_gramos = 2.9
    espinaca.contiene = [fibra, vitaminas, minerales]
    espinaca.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    zanahoria = onto.Vegetal("Zanahoria")
    zanahoria.calorias = 41
    zanahoria.proteinas_gramos = 0.9
    zanahoria.contiene = [fibra, vitaminas]
    zanahoria.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    tomate = onto.Vegetal("Tomate")
    tomate.calorias = 18
    tomate.proteinas_gramos = 0.9
    tomate.contiene = [vitaminas, minerales]
    tomate.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    lechuga = onto.Vegetal("Lechuga")
    lechuga.calorias = 15
    lechuga.proteinas_gramos = 1.4
    lechuga.contiene = [fibra, vitaminas]
    lechuga.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    manzana = onto.Fruta("Manzana")
    manzana.calorias = 52
    manzana.proteinas_gramos = 0.3
    manzana.contiene = [fibra, vitaminas]
    manzana.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    platano = onto.Fruta("Platano")
    platano.calorias = 89
    platano.proteinas_gramos = 1.1
    platano.contiene = [carbohidrato_nutriente, vitaminas]
    platano.apropiado_para = [obj_energia, obj_ganar_musculo]

    naranja = onto.Fruta("Naranja")
    naranja.calorias = 47
    naranja.proteinas_gramos = 0.9
    naranja.contiene = [vitaminas, fibra]
    naranja.apropiado_para = [obj_mantenimiento, obj_energia]

    fresas = onto.Fruta("Fresas")
    fresas.calorias = 32
    fresas.proteinas_gramos = 0.7
    fresas.contiene = [vitaminas, fibra]
    fresas.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    yogur = onto.Lacteo("Yogur")
    yogur.calorias = 59
    yogur.proteinas_gramos = 10.0
    yogur.contiene = [proteina_nutriente, lactosa, producto_animal]
    yogur.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    yogur.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    queso = onto.Lacteo("Queso")
    queso.calorias = 402
    queso.proteinas_gramos = 25.0
    queso.contiene = [proteina_nutriente, lactosa, producto_animal]
    queso.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    queso.apropiado_para = [obj_ganar_musculo]

    leche_almendra = onto.Lacteo("LecheAlmendra")
    leche_almendra.calorias = 17
    leche_almendra.proteinas_gramos = 0.6
    leche_almendra.contiene = [vitaminas]
    leche_almendra.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    aguacate = onto.Grasa("Aguacate")
    aguacate.calorias = 160
    aguacate.proteinas_gramos = 2.0
    aguacate.contiene = [grasas_saludables, fibra]
    aguacate.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    nueces = onto.Grasa("Nueces")
    nueces.calorias = 654
    nueces.proteinas_gramos = 15.2
    nueces.contiene = [grasas_saludables, proteina_nutriente]
    nueces.apropiado_para = [obj_ganar_musculo, obj_energia]

    aceite_oliva = onto.Grasa("AceiteOliva")
    aceite_oliva.calorias = 884
    aceite_oliva.proteinas_gramos = 0.0
    aceite_oliva.contiene = [grasas_saludables]
    aceite_oliva.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    return onto
