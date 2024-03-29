from tkinter import *
from tkinter import messagebox
import random

#Muestra poco a poco la plabra si se va adivinando las letras
def mostrar(pal,m):

	completo = True
	texto = ''
	global l

	for i in pal:

		#Si la letra está, se pone en lugar de "_"
		if(i in m):

			texto += i

		#Si todavía no se acierta, se muestra "_"
		else:

			texto += "_"
			completo = False

		texto += " "

	l.config(text=texto)
	
	return completo

#Se dibuja al hombre ahorcado conforme se va perdiendo
def error(err):

	global canvasr

	if err == 1:

		canvasr.create_oval(322,85, 377,130, width=7)#CABEZA

	elif err == 2:
		
		canvasr.create_line(350,130, 350,300, width=7)#CUERPO

	elif err == 3:
		
		canvasr.create_line(300,198, 350,148, width=7)#BRAZO Izq

	elif err == 4:
		
		canvasr.create_line(400,198, 350,148, width=7)#BRAZO Der

	elif err == 5:
		
		canvasr.create_line(300,348, 350,298, width=7)#PIERNA Izq

	elif err == 6:
		
		canvasr.create_line(350,298, 400,348, width=7)#PIERNA Der

#Se evalúa si la letra ya se encuentra, acierta en la palabra o se equivoca
def evaluar(*args):

	global inp
	global inpt
	
	resp = str(inp.get())
	inp.set("")

	global errores
	global puntos 
	global completo
	global muestra
	global palabra
	global canvasr
	global root
	
	continuar = True
		
	if not(resp.isnumeric() or resp.isnumeric()):

		if resp in muestra:
			
			messagebox.showwarning(message=f"¡La letra ya se encuentra!",title="Precaución")

		else:

			if len(resp) == 1:

					if (resp.upper()) in palabra:

						muestra.append(resp)
						puntos += 1

					else:

						errores += 1

			else:

				if resp.upper() == palabra:

					lista = []
					
					for letra in palabra:
					
						lista.append(letra)
					
					mostrar(palabra,lista)
					puntos = (puntos + len(palabra))
					messagebox.showinfo(message=f"¡Palabra Correcta!\nPalabra: {palabra}\nPuntuaje: {puntos*100}",title="GAME OVER")
					continuar = messagebox.askyesno('GAME OVER', '¿Desea jugar de nuevo?')

					if continuar:
					
						l.config(text="")
						canvasr.delete("all")
						inpt.destroy()
						game()

					else:

						root.destroy()
						pass
					

				else:

					for e in range(1,6):
						
						error(e)

					errores = 6
			
			if 	continuar:

				error(errores)
				completo = mostrar(palabra,muestra)

			if errores == 6:

				messagebox.showinfo(message=f"¡Ahorcado!\nPalabra: {palabra}\nPuntuaje: {puntos*100}",title="GAME OVER")
				continuar = messagebox.askyesno('GAME OVER', '¿Desea jugar de nuevo?')

				if continuar:
						
					l.config(text="")
					canvasr.delete("all")
					inpt.destroy()
					game()

				else:

					root.destroy()
					pass
				
		if completo:
			
			messagebox.showinfo(message=f"Palabra Completada.\nPalabra: {palabra}\nPuntuaje: {puntos*100}",title="GAME OVER")
			continuar = messagebox.askyesno('GAME OVER', '¿Desea jugar de nuevo?')

			if continuar:
					
				l.config(text="")
				canvasr.delete("all")
				inpt.destroy()
				game()

			else:

				root.destroy()
				pass
	
	else:

		messagebox.showerror(message=f"No se admiten números en este juego. Por favor ingrese sólo letras.",title="Error")

#El cuerpo del juego en general
def game():

	global l
	global muestra
	global palabra
	global canvasr
	global root
	global inp
	global inpt
	global errores
	global puntos 
	global completo
	global canvasr

	#El dibujo del inicio del juego
	canvasr = Canvas(root,width=700,height=500)
	canvasr.place(x=5,y=5)
	canvasr.create_line(10,10, 10,700, width=7,fill='#825637')#PALO (X1,Y1,X2,Y2)
	canvasr.create_line(8,10, 350,10, width=7,fill='#825637')#PALO 2
	canvasr.create_line(350,7, 350,85, width=7,fill='#D19469')#CUERDA

	l = Label(root,text='',fg='#000',bg='#DDD',font=('Helvetica', 45, 'bold'))
	l.place(x=25,y=530)

	#Todas las palabras que están en el juego
	palabras = ['HUMANIDAD', 'HUMANO', 'PERSONA', 'GENTE', 'HOMBRE', 'MUJER', 'NIÑO', 'ADOLESCENTE', 'ADULTO', 'ANCIANO', 'SEÑOR', 'CABALLERO', 'DAMA', 'CUERPO', 'PIERNA', 'RODILLA', 'CABEZA', 'CARA', 'BOCA', 'LABIO', 'DIENTE', 'NARIZ', 'BARBA', 'BIGOTE', 'CABELLO', 'OREJA', 'CEREBRO', 'BRAZO', 'CODO', 'HOMBRO', 'MANO', 'MUÑECA', 'PALMA', 'DEDO', 'CUELLO', 'MENTE', 'ALMA', 'ESPALDA', 'SANGRE', 'CARNE', 'PIEL', 'HUESO', 'RESFRIADO', 'GRIPE', 'SALUD', 'ENFERMEDAD', 'FAMILIA', 'AMIGO', 'PAREJA', 'ESPOSO', 'MATRIMONIO', 'AMOR', 'PADRE', 'MADRE', 'HERMANO', 'ABUELO', 'NIETO', 'PRIMO', 'SOBRINO', 'CRIATURA', 'ESPECIE', 'VIDA', 'NACIMIENTO', 'MUERTE', 'NATURALEZA', 'CAMPO', 'BOSQUE', 'SELVA', 'DESIERTO', 'COSTA', 'PLAYA', 'LAGUNA', 'MONTAÑA', 'IMALES', 'ANIMAL', 'PERRO', 'GATO', 'VACA', 'CERDO', 'CABALLO', 'YEGUA', 'OVEJA', 'MONO', 'TIGRE', 'CONEJO', 'CIERVO', 'RANA', 'JIRAFA', 'ELEFANTE', 'GALLINA', 'CUERVO', 'PESCADO', 'LANGOSTA', 'SARDINA', 'CALAMAR', 'PULPO', 'CANGREJO', 'INSECTO', 'BICHO', 'MARIPOSA', 'POLILLA', 'SALTAMONTES', 'ARAÑA', 'MOSCA', 'MOSQUITO', 'CUCARACHA', 'CARACOL', 'BABOSA', 'LOMBRIZ', 'MARISCO', 'MOLUSCO', 'LAGARTO', 'SERPIENTE', 'COCODRILO', 'ALIMENTO', 'COMIDA', 'BEBIDA', 'VEGETAL', 'PLANTA', 'PASTO', 'FLOR', 'FRUTA', 'SEMILLA', 'HONGO', 'CIRUELA', 'PINO', 'NUEZ', 'ALMENDRA', 'CASTAÑA', 'ARROZ', 'AVENA', 'CEBADA', 'TRIGO', 'VERDURA', 'PAPAS', 'ZANAHORIA', 'MANZANA', 'DORADO', 'PERA', 'DURAZNO', 'TOMATE', 'SOPA', 'TIEMPO', 'CALENDARIO', 'EDAD', 'FECHA', 'INSTANTE', 'MOMENTO', 'SEGUNDO', 'MINUTO', 'SEMANA', 'AÑO', 'SIGLO', 'MILENIO', 'AYER', 'MAÑANA', 'AMANECER', 'TARDE', 'ANOCHECER', 'NOCHE', 'LUNES', 'MARTES', 'JUEVES', 'VIERNES', 'DOMINGO', 'AMBIENTE', 'ESPACIO', 'ENTORNO', 'SUPERFICIE', 'VOLUMEN', 'MUNDO', 'PLANETA', 'LUNA', 'ESTRELLA', 'GALAXIA', 'UNIVERSO', 'CLIMA', 'LLUVIA', 'NIEVE', 'VIENTO', 'TRUENO', 'TORMENTA', 'CIELO', 'ESTE', 'OESTE', 'NORTE', 'DERECHA', 'IZQUIERDA', 'DIAGONAL', 'EXTERIOR', 'INTERIOR', 'ATERIALES', 'CALOR', 'AGUA', 'HIELO', 'VAPOR', 'FUEGO', 'AIRE', 'TIERRA', 'PISO', 'SUELO', 'METAL', 'HIERRO', 'PLATA', 'PLOMO', 'PESO', 'METRO', 'LITRO', 'GRAMO', 'CANTIDAD', 'MEDIDA', 'SOCIEDAD', 'COMUNIDAD', 'EMPRESA', 'EQUIPO', 'AUTORIDAD', 'CARGO', 'CAMPAÑA', 'CLUB', 'CONTINENTE', 'EUROPA', 'ASIA', 'ESTADO', 'PROVINCIA', 'DEPARTAMENTO', 'MUNICIPIO', 'DEMOCRACIA', 'DICTADURA', 'PRESIDENTE', 'BOMBEROS', 'CAPITAL', 'CIUDAD', 'PUEBLO', 'LIBERTAD', 'DERECHO', 'PERMISO', 'ESCRITORIO', 'SILLA', 'MESA', 'CAMA', 'DORMITORIO', 'OFICINA', 'VENTANA', 'HOGAR', 'EDIFICIO', 'ESCALERA', 'PANTALLA', 'COMPUTADORA', 'ELECTRICIDAD', 'CORRIENTE', 'BOLSILLO', 'RELOJ', 'CLAVO', 'CAMISA', 'ZAPATO', 'ABRIGO', 'FALDA', 'CORBATA', 'CARRO', 'AMBULANCIA', 'BICICLETA', 'ALFABETO', 'NOTICIA', 'TEXTO', 'DICCIONARIO', 'COLOR', 'BLANCO', 'NEGRO', 'GRIS', 'ROJO', 'NARANJA', 'AMARILLO', 'VERDE', 'CELESTE', 'AZUL', 'VIOLETA', 'CULTURA', 'ENTRETENIMIENTO', 'ARTE', 'CINE', 'DIBUJO', 'PINTURA', 'UNIVERSIDAD', 'ESTUDIO', 'DEPORTE', 'CARRERA', 'RESPUESTA', 'PREGUNTA', 'VELOCIDAD', 'MOVIMIENTO', 'CRECIMIENTO', 'AUMENTO', 'CONTENIDO', 'OBJETO', 'PALABRA', 'NOMBRE', 'SECRETO', 'FORMALIDAD', 'PRESENTE', 'PASADO', 'FUTURO', 'ORIGEN', 'DESTINO', 'CONFLICTO', 'GUERRA', 'BUENO', 'SUPERIOR', 'INFERIOR', 'CENTRAL', 'LATERAL', 'FRONTAL', 'CORRECTO', 'INCORRECTO', 'GRANDE', 'PEQUEÑO', 'SOLEDAD', 'LENGUAJE', 'AMISTAD', 'FURIA', 'ANSIEDAD', 'ABURRIMIENTO', 'MIEDO', 'FELICIDAD','NUCLEAR','GRAVEDAD']

	#Se elije una al azar
	palabra = palabras[random.randint(0,len(palabras)-1)]
	cont = 0
	muestra = []

	for i in palabra:

		if (random.randint(0,1)) == 1:

			muestra.append(i)
			cont += 1

		if (cont < (len(palabra)//2)):

			break

	if cont == 0:

		muestra.append(palabra[random.randint(0,len(palabra)-1)])

	mostrar(palabra,muestra)

	errores = 0
	puntos = 0
	completo = False

	inp = StringVar()
	inpt = Entry(textvar=inp,font=('Helvetica', 30, 'bold'))
	inpt.place(x=720,y=100,width=350,height=80)
	btn = Button(root,text='Enviar',fg='#000',bg='#439C0C',font=('Helvetica', 30, 'bold'),command=evaluar)
	btn.place(x=800,y=270)

	inpt.focus()
	root.bind("<Return>",evaluar)


root = Tk()
root.title('Juego - Ahorcado')
root.configure(background='#DDD') 
root.geometry('1100x650')

game()

root.mainloop()