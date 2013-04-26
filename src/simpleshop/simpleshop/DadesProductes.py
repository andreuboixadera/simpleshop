import os

here = os.path.dirname(os.path.abspath(__file__))

class Productes():
 
        def __init__(self):      				
    					
                self.longitud = 0
		self.longitudComandes = 0
                self.productes = {}
                self.comandes = {}
                self.carregararray()
                self.carregaLlistaCommandes()

        def getProductes(self):  

                return self.productes

        def getProducte(self, index):  

                return self.productes[index]


        def getComandes(self, index):  

                return self.comandes

        def getComanda(self, index):  

                return self.comandes[index]


        def getProducteID(self, index):  
                return self.productes[index]["id"]

        def getProducteNOM(self, index):  
                return self.productes[index]["nom"]

        def getProducteSTOCK(self, index):  
                return self.productes[index]["quantitat"]

        def getProductePREU(self, index):  
                return self.productes[index]["preu"]



        def getComandesFILA(self, index):  
                return self.comandes[index]["fila"]




        def getComandesKeys(self):  

                return self.comandes.keys()


        def getProducteKeys(self):  

                return self.productes.keys()



        def getLongitud(self):  

                return self.longitud	# i+=1 incrementara despres de lassignacio

	def getLongitudComandes(self):  

		return self.longitudComandes


        def carregararray(self):

                if (os.path.isfile(here+'/productes.txt') is True):    
                        f = open(here+'/productes.txt', 'r')  

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
                        #print "no carregat"
                        #self.productes={ID:None} 	
                        pass



	def carregaCommanda(self):

                if (os.path.isfile(here+'/id-comanda.txt') is True):    
                	f = open(here+'/id-comanda.txt', 'r')  
                        #print "id carregat"
                        
			
			idComanda = f.readline()

                        f.close()
			return idComanda						 
	
                else:
                        #print "no carregat"
                        #self.productes={ID:None} 	
                	pass



	def eliminarproducte(self, ideliminar):
		if (os.path.isfile(here+'/productes.txt') is True):    
                      
			contingut=""

			f = open(here+'/productes.txt', 'r')  

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

 			f = open(here+'/productes.txt', 'w')  
			f.write(contingut)
			f.close()


			f = open(here+'/productes.txt', 'r')  
			i=0
			for line in f:
                                self.longitud=i
				i+=1
			f.close()
 
                        

			self.carregararray()					 
	
                else:	
			pass




        def guardarproducte(self, identrat, nomentrat, quantitatentrat, preuentrat):

                if (os.path.isfile(here+'/productes.txt') is True):    
                        f = open(here+'/productes.txt', 'a')  

			f.write(identrat+"\t"+nomentrat+"\t"+quantitatentrat+"\t"+preuentrat+"\n") 

                        f.close()						 
	
                else:
                        #self.productes={ID:None} 	
                        pass


	def seguentcomanda(self, idcomanda):

                	f = open(here+'/id-comanda.txt', 'w')  
			idcomanda = int(idcomanda)+1
			f.write(str(idcomanda))
                        f.close()


        def guardarcomanda(self, idcomanda, idproducte, nomproducte, quantitatproducte, preuunitari):

                if (os.path.isfile(here+'/comandes.txt') is True):    
                        f = open(here+'/comandes.txt', 'a')  
			f.write("Comanda="+idcomanda+"\tIdProducte="+idproducte+"\tNomProducte="+nomproducte+"\tQuantitatProducte="+quantitatproducte+"\tPreuProducte="+preuunitari+"\n") 
                        f.close()						 

                else:
                        #self.productes={ID:None} 	
                        pass



        def modificaproducte(self, identrat, nomentrat, quantitatentrat, preuentrat):

		identrat=str(identrat)
		nomentrat=str(nomentrat)
		quantitatentrat=str(quantitatentrat)
		preuentrat=str(preuentrat)

                if (os.path.isfile(here+'/productes.txt') is True):  

			self.eliminarproducte(identrat)  

                        self.guardarproducte(identrat, nomentrat, quantitatentrat, preuentrat)						 
	
                else:
                        #self.productes={ID:None} 	
                        pass


	def carregaLlistaCommandes(self):

                if (os.path.isfile(here+'/comandes.txt') is True):    
                	f = open(here+'/comandes.txt', 'r')  
                        #print "comandes carregades"
                        i=0	
                        for line in f:

                                comandes = {}			
                                dades = line

                                producte = {"fila":dades} 
                                
                                self.comandes[i] = producte
                                self.longitudComandes=i
				i+=1

                        f.close()						 
	
                else:
                        #print "comandes no carregat"
                        #self.productes={ID:None} 	
                        pass


	def getLlistaComandes(self):
		if (os.path.isfile(here+'/comandes.txt') is True):    
                	f = open(here+'/comandes.txt', 'r')  
                        #print "comandes carregades"
                        i=0	

			comandesTotal = ""

                        for line in f:

                                comandesTotal = comandesTotal + line + "\n" 			

			return comandesTotal
                        f.close()						 
	
                else:
                        return "No hi han productes"
                        #self.productes={ID:None} 	
                        pass

