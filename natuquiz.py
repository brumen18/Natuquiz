opcion=""
contador=int(0)
puntos=int(0)
    #ahora vamos a guardar las respuestas correctas, para imprimirlas en pantalla si el usuario se equivoca.
respcorrectas=["Y la respuesta correcta era...\n¡La C! El corazón posee cuatro válvulas que le permiten bombear la sangre de manera adecuada en un solo sentido. Estas válvulas son: Mitral, tricúspide, pulmonar y aórtica.", ""]
respcorrectas.append("Me temo que no.\nEn las flores se encuentran los órganos reproductores de las plantas. De hecho, éstas pueden ser unisexuales o ermafroditas.")
respcorrectas.append("Respuesta incorrecta: Aunque a ciencia cierta el origen preciso de las aves sigue siendo un misterio, se da por sentado que se encuentra estrechamente relacionado con los reptiles prehistóricos como el velociraptor, una especie de terópodo.")
respcorrectas.append("Nop, esos no eran...\nTanto las ballenas como los delfines pertenecen al orden de los cetáceos, lo que significa que poseen plasenta y son de sangre caliente, dan a luz en lugar de poner huevos, y producen leche para alimentar a sus crías. Además poseen pulmones en lugar de bránqueas, por lo que respiran aire.")
respcorrectas.append("¡Incorrecto! La evaporación es el primer proceso que inicia el ciclo hidrológico. En éste, el agua de la superficie terrestre pasa a la admósfera, donde se condensa formando pequeñas gotas que al fundirse forman nubes. Luego éstas caen por su peso dando paso a la presipitación. Una vez en la tierra el agua sigue diversos cursos que también forman parte del ciclo, como la infiltración o la solidificación.")
respcorrectas.append("¡Te equivocaste! Las mujeres ovulan unas 400 veces a lo largo de su vida. Durante cada ciclo solo se libera un óvulo, aunque en ocasiones pueden expulsarse dos o más al mismo tiempo que, si son fecundados, permiten concebir gemelos.")
respcorrectas.append("¡Falso!\nEl cerebro humano adulto puede pesar entre 1200 y 1400 gramos, y posee una cantidad aproximada de 100.000 neuronas y una cantidad aún mayor de sinapsis que permiten la conexión interneuronal.\nEstúdiatelo, quizás te crecen unas cuantas más -broma-.")
respcorrectas.append("Incorrecto. Al nacer los bebés poseen aproximadamente 300 huesos que con el tiempo se van fusionando y endureciendo, para formar el esqueleto de una persona adulta, el cual consta de 206 huesos.")
respcorrectas.append("¡No! El caballito de mar o hipocampo es el único animal cuyo macho posee una bolsa cerrada cimilar a un útero, en el que se desarrollan las crías tras una gestación de 14 o 28 días según la especie,.\nMenos mal que no somos los seres humanos, porque imagínate...")
respcorrectas.append("Falso. Los cloroplastos son los orgánulos de las células vegetales en los cuales se realiza la fotosíntesis, para lo cual contienen la clorofila.")
respcorrectas.append("Me temo que te equivocaste...\nLa clavícula y el homóplato son los dos huesos que articulados entre sí junto con el tórax sostienen el brazo.")
respcorrectas.append("¡No! La gastritis consiste en un conjunto de trastornos ccaracterizados por la inflamación del revestimiento o mucosa del estómago. Puede producirse por infecciones, consumo execivo de alcohol y ciertos medicamentos.\nYa sabes, ¡deja de ir a tantas fiestas!")
respcorrectas.append("¡Incorrecto! En muchas ocasiones las hembras de esta especie utilizan las relaciones sexuales, incluso homoeróticas, para apasiguar los ánimos del grupo y restaurar la paz.\nHabrá que probar ese método nosotros, a lo mejor funciona...")
respcorrectas.append("Incorrecto. De acuerdo al Informe de Evaluación Global sobre biodiversidad y servicios ecosistémicos de 2019 del IPBES, más de 5000 animales están en peligro de extinsión y más de 35000 en peligro crítico, siendo el oso polar, el oso panda, el tigre de montaña, el rinoceronte, el gorila de montaña, el tigre de Sumatra, el delfín de agua dulce, las ballenas y tortugas marinas, solo algunos de los que encabezan la lista.")
respcorrectas.append("¡Te has equivocado! La malacología es la ciencia que estudia los moluscos, mientras que la conquiliología, por su parte, estudia los moluscos con concha.")
respcorrectas.append("No, eso no es... \n El Ácido Desoxirribonucleico (ADN) es una proteína compleja que se encuentra en el núcleo de las células y es el principal constituyente del material genético de los seres vivos.")
respcorrectas.append("Mala suerte. El nervio óctico es el segundo de los pares craneales. Se trata de un tracto de fibras con aproximadamente 1,2 millones de axones, rodeados por vainas meníngeas, que transporta las sensaciones visuales al sistema nervioso central.")
respcorrectas.append("No, eso no era... \n La cualidad llamativa de este lagarto de México es que puede llorar sangre. Lo hace para protegerse de sus depredadores, pues la sangre que expulsa a chorros por sus ojos posee sustancias tóxicas que resultan, cuando menos, desagradables para los depredadores.")
respcorrectas.append("¡Falso! Los organismos del reino animal son multicelulares, pues están conformados por muchas células. La diferencia entre autótrofos y heterótrofos es que los primeros pueden producir su propio alimento utilizando luz (fotosíntesis) o energía química (quimiosíntesis) y los heterótrofos no pueden sintetizar su propio alimento, por lo que ingieren otros organismos, como plantas y animales.")
respcorrectas.append("¡Mentira! La camada es el conjunto de crías que tienen en un solo parto los animales mamíferos.")
respcorrectas.append("No. La medusa melena de león (Cyanea capillata) puede llegar a tener un sombrero de 2,3 metros de diámetro y tentáculos de hasta 36 metros de longitud.\n¡Qué peligro!")
respcorrectas.append("La respuesta correcta era... un banco de peces.\nSin embargo, en muchas ocasiones los cardúmenes pueden estar conformados por más de un banco de peces, es decir, por distintas especies que naden juntos.")
respcorrectas.append("Te equivocaste. La sinecología estudia las relaciones entre comunidades biológicas, es decir, medios ambientales individuales y las especies que los conforman. Incluye organismos de los distintos reinos.")
respcorrectas.append("¡Mentira! fue Carlos Linneo!\nEn 1751 Lineo publicó su obra más influyente, 'Filosofía botánica', en la que afirmaba que era posible crear un sistema natural de clasificación a partir de la creación divina, original e inmutable, de todas las especies. Era lo que hoy conocemos como taxonomía.")
respcorrectas.append("Incorrecto. Los roedores: Chinchillas, ratas, perritos de la pradera, cobayas, ardillas, conejos, capivaras, hámsters... son muchísimas.\n¡Qué ganas de adoptar alguno!")
respcorrectas.append("¡Falso! era tundra. El permafrost es la parte profunda del suelo de las regiones frías, que se halla permanentemente helada.")
respcorrectas.append("Mala suerte. Los dientes de los hamsters crecen 	un promedio de 2 a 4 milímetros a la semana durante toda su vida. Por esta razón los veterinarios recomiendan mantener a su alcance juguetes o alimentos que puedan roer para así limarlos, y evitarles problemas de salud.")
respcorrectas.append("Nop, eso no era. Entre 4 y 5 años, aunque hay algunos que han vivido hasta 8 años.\nTambién quiero adoptar uno de esos.")
respcorrectas.append("¡No, por Dios! Los animales de sangre fría son los insectos, peces, anfibios, arácnidos y reptiles. Por lo tanto, al ser la salamandra un amfibio posee sangre fría.")
respcorrectas.append("No quiero ser duro contigo pero esa opción no era...\nLo llaman el pájaro venenoso y junto con el Ifrita kowaldi son los únicos pájaros venenosos conocidos.")
#funcion juega, que contiene el contenido principal del juego.
def juega():
    #lo primero que haremos es guardar en una lista todas las preguntas que existen.
    #usamos el append para que sea mas cómodo visualmente.
    preguntas=["¿Cuáles de las siguientes opciones corresponden a válvulas del corazón?", "¿Qué parte de una planta representan las flores?", "¿De dónde se cree que provienen las aves?"]
    preguntas.append("¿Cuáles de los siguientes animales marinos son mamíferos?")
    preguntas.append("¿Cuáles de los siguientes procesos corresponden al ciclo del agua?")
    preguntas.append("Según los médicos, la mujer puede ovular naturalmente una cantidad limitada de veces a lo largo de su vida. ¿Cuál de las siguientes cifras es la que más se aproxima?")
    preguntas.append("¿Cuál es el número aproximado de neuronas que posee el cerebro humano?")
    preguntas.append("¿La siguiente afirmación es verdadera o falsa? Los bebés nacen con una cantidad de huesos mayor a la que posee una persona adulta.")
    preguntas.append("¿En cuál de los siguientes animales encontramos que el macho es quien se encarga de llevar a las crías en su interior durante la gestación?")
    preguntas.append("¿Qué contienen los cloroplastos de las células vegetales?")
    preguntas.append("¿Cuáles de los siguientes dos huesos se hallan en el hombro?")
    preguntas.append("¿Cuál de las siguientes enfermedades afecta el sistema digestivo?")
    preguntas.append("Los bonobos pertenecen a la familia de los simios. ¿Cómo manejan ellos normalmente un conflicto?")
    preguntas.append("¿Cuáles de los siguientes grupos de animales se encuentran actualmente en peligro de extinsión?")
    preguntas.append("¿Qué es la malacología?")
    preguntas.append("¿Qué significan las siglas 'ADN'?")
    preguntas.append("Los pares craneales son 12 pares de nervios que pasan por orificios del cráneo y van desde el encéfalo hasta diferentes partes del cuerpo, transmitiendo información de los sentidos como el gusto o el olfato.\nAnte esto, ¿Qué par craneal es el nervio óptico?")
    preguntas.append("Responde si la siguiente afirmación es verdadera o falsa: El 'Phrynosoma cornutum' (también conocido como lagarto de cuernos) puede disparar sus espinas en caso de peligro.")
    preguntas.append("¿De qué tipo son todos los organismos del reino Animalia?")
    preguntas.append("¿Cómo se denomina a un grupo de crías de perro?")
    preguntas.append("¿Cuál es la especie de medusa más grande del mundo?")
    preguntas.append("¿Qué es un cardumen?")
    preguntas.append("Responde si la siguiente afirmación es verdadera o falsa: la sinecología es la ciencia que estudia las relaciones entre las comunidades biológicas y los ecosistemas de la Tierra.")
    preguntas.append("¿Por quién fue ideado el sistema de clasificación taxonómica actual?")
    preguntas.append("¿Qué orden de mamíferos tiene el mayor número de especies?")
    preguntas.append("¿Qué bioma o paisaje bioclimático se caracteriza por tener una capa de permafrost?")
    preguntas.append("¿Cuál de los siguientes animales tiene incisivos que continúan creciendo durante toda su vida?")
    preguntas.append("¿Cuánto puede vivir un erizo?")
    preguntas.append("¿La salamandra es un animal de sangre caliente?")
    preguntas.append("¿Qué tiene de especial el ave conocida como pitohuí?")
    #ahora importamos un math para sacar un número aleatóreo.
    print("¡OK, empecemos! allá va la primer pregunta.")
    jugar="jugar"
    import random
    pregunta=random.randint(0, len(preguntas)-1)
    while jugar=="jugar":
        if contador==2:
            #imprimimos en pantalla la pregunta que consiguió.
            print("¡Fin del juego! te has equivocado 3 veces.")
            jugar=""
        else:
            print(preguntas[pregunta])
        #y llamamos a la función respuesta.
            respuesta(pregunta)
            borrarpregunta=preguntas[pregunta]
            preguntas.remove(borrarpregunta)
            pregunta=random.randint(0, len(preguntas)-1)
#función respuesta:
def respuesta(npregunta):
    global puntos
    global contador
    import random
    if npregunta==0:
        print("A: Mitral, tricúspide, píloro.")
        print("B: pulmonar, aórtica, Cardias.")
        print("C: Tricúspide, pulmonar, mitral.")
        ropcion=input("Tu respuesta: ")
        if ropcion.upper()=="C":
            print("¡Sí! felicidades.")
            print("¡Vamos a la siguiente.")
            puntos=int(puntos+random.randint(0, 1000))
        else:
            contador=contador+1
            puntos=int(puntos-random.randint(0, 1000))
            global respcorrectas
            print(respcorrectas[npregunta])
while opcion.upper()!="SALIR":
    print("¡BIENVENIDO A NATUQUIZ!")
    print("¿Qué tanto conoces de tu planeta y los seres que lo habitan?")
    print("Si deseas saber cómo jugar, teclea 'ayuda'. De lo contrario, teclea 'jugar' para empezar.")
    opcion=input("¿Cuál es tu opción?")
    if opcion.upper()=="AYUDA":
        print("¡Bienvenido!")
        print("Este es un juego en el que tendrás que ir respondiendo preguntas de biología, a fin de conseguir la mayor cantidad de puntos.")
        print("Por cada respuesta correcta que des, se te dará una cantidad aleatórea de puntos, y por cada respuesta incorrecta, se te restarán.")
        print("¡Pero eso sí!")
        print("Solo puedes fallar 3 veces. Si superas ese límite, el juego terminará.")
        print("Tu objetivo es llegar al final del juego, respondiendo todas las preguntas correctamente.")
        print("Por ahora, no puedes hacer nada con los puntos, pero en un futuro próximo implementaremos una modalidad en donde podrás subirlos a un sitio web.")
        print("¡Y así demostrarles a todos que eres el mejor!")
        print("Durante el juego, te voy a presentar una pregunta con 3 opciones. Para responder, solo presiona la tecla asociada a dicha respuesta.")
        print("Por ejemplo: ")
        print("¿Qué es un perro?")
        print("A: un animal.")
        print("B: un bicho.")
        print("C: no sé.")
        print("Para marcar la a, que es la respuesta correcta, solo deberás escribir a.")
        print("Por último, si en algún momento decides salir del juego, teclea 'salir'.")
        print("Pero recuerda que tu progreso no se guardará.")
        print("Esto es todo.")
        print("¿Te atreves a demostrar lo culto que eres? ¡Ven y juega conmigo!")
    elif opcion.upper()=="JUGAR":
        juega()
    elif opcion.upper()=="SALIR":
        salir=""
    else:
        print("¡Esa no es una opción válida! asegúrate, por favor, de haber escrito el comando bien y sin los apóstrofes. Por ejemplo, pon ayuda en vez de 'ayuda'.")