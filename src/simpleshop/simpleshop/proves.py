import os

class Productes():
 
        def __init__(self):      				
    					
                self.longitud = 0
                self.productes = {}
                self.carregararray()


        def getProductes(self):  

                return self.productes


        def getProducte(self, index):  

                return self.productes[index]


        def getProducteID(self, index):  
                return self.productes[index]["id"]

        def getProducteNOM(self, index):  
                return self.productes[index]["nom"]

        def getProducteSTOCK(self, index):  
                return self.productes[index]["quantitat"]

        def getProductePREU(self, index):  
                return self.productes[index]["preu"]


        def getProducteKeys(self):  

                return self.productes.keys()



        def getLongitud(self):  

                return self.longitud	# i+=1 incrementara despres de lassignacio




        def carregararray(self):

                if (os.path.isfile('productes.txt') is True):    
                        f = open('productes.txt', 'r')  

                        i=0	
                        for line in f:

                                producte = {}			
                                dades = line.split("\t")

                                identificador = dades[0]
                                nom = dades[1]
                                quantitat = dades[2]
                                preu = dades[3]
                                

                                preu = preu.replace('\n','')
                                producte = {"id":identificador, "nom":dades[1], "quantitat":quantitat, "preu":preu} 
                                
                                self.productes[identificador] = producte
                                self.longitud=i
				i+=1

                        f.close()						 
	
                else:
                        #self.productes={ID:None} 	
                        pass




	def eliminarproducte(self, ideliminar):
		if (os.path.isfile('productes.txt') is True):    
                      
			contingut=""

			f = open('productes.txt', 'r')  

                        for line in f:

                                dades = line.split("\t")

                                identificador = dades[0]
                                nom = dades[1]
                                quantitat = dades[2]
                                preu = dades[3]
                                
				if str(ideliminar)!=str(identificador):
					contingut += identificador+"\t"+nom+"\t"+quantitat+"\t"+preu

				else:
					pass
                               
                        f.close()	

 			f = open('productes.txt', 'w')  
			f.write(contingut)
			f.close()


			f = open('productes.txt', 'r')  
			i=0
			for line in f:
                                self.longitud=i
				i+=1
			f.close()
 
                        

			self.carregararray()					 
	
                else:	
			pass




        def guardarproducte(self, identrat, nomentrat, quantitatentrat, preuentrat):

                if (os.path.isfile('productes.txt') is True):    
                        f = open('productes.txt', 'a')  

			f.write(identrat+"\t"+nomentrat+"\t"+quantitatentrat+"\t"+preuentrat+"\n") 

                        f.close()						 
	
                else:
                        #self.productes={ID:None} 	
                        pass



        def modificaproducte(self, identrat, nomentrat, quantitatentrat, preuentrat):

		identrat=str(identrat)
		nomentrat=str(nomentrat)
		quantitatentrat=str(quantitatentrat)
		preuentrat=str(preuentrat)

                if (os.path.isfile('productes.txt') is True):  

			self.eliminarproducte(identrat)  

                        self.guardarproducte(identrat, nomentrat, quantitatentrat, preuentrat)						 
	
                else:
                        #self.productes={ID:None} 	
                        pass




