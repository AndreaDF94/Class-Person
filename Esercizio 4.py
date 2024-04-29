# Esercizio 4
# Creare una classa denominata PERSON con le seguenti proprietà: nome,cognome,nazionalità e una funzione chiamta SALUTO.
# Crea un'altra classe chiamata ITALIANO con le seguenti proprietà:lingua principale, che afferma che la nazionalità
# sarà l'italiano e ha una funzione chiamata saluto che mostra sullo schermo un saluto nella lingua della classe.
# Successivamente create un programma che:
# Richieda all'utente i dati necessari per riempier un oggetto nella classe italiano.
# Crea un metodo che riceva i dati forniti dall'utente e crea un istanza della classe italiana con i dati ricevuti.
# Visualizza i dati di un oggetto sullo schermo chiamando la funzione.

class Person: # è una classe che rappresenta una persona con tre attributi: nome,cognome e nazionalità.
    def __init__(self, nome,cognome,nazionalità):
        self.nome = nome
        self.cognome = cognome
        self.nazionalità = nazionalità
    def saluto(self):
        print("Ciao,sono", self.nome , self.cognome)   

class Italian(Person): # è una classe che eredità dalla classe Person due attributi aggiuntivi: lingua_pricipale e nazionalità
                       # Per entrambe le classi ho utilizzato il metodoto__init__.Questo metodoto mi serve per inizializzare gli attributi
                       # dell'istanza con i valori passati come argomenti.
                       # Infine entrabe le classi hanno il metodo saluto che stampa un messaggio di saluto.
    def __init__(self, nome, cognome,):
        super().__init__(nome, cognome, "Italiana") # Utilizzo la funzione super nel metodo__init__ della classe Italian per chiamare
                                                    # metodo__init__ della classe genitore Person.
                                                    # IN questo modo posso inizializzare gli attributi della classe Person e Italian , aggiungendo
                                                    # anche i nuovi attributi specifici della classe Italian.  
        self.lingua_principale = "italiano" 
    def saluto(self):
        print("Ciao , sono",self.nome, self.cognome," e parlo italiano") 

def main(): # La funzione main è il punto d'ingresso del programma.,ovvero richiederà all'utente di inserire il nome e cognome tramite funzione(input)
            # Utilizzerà i dati iseriti dall'utente per creare un istanza nella clase Italian
            # Stamperà i dettagli dell'oggetto creato(nome,cognome,nazionalità,lingua_principale.)
            # Infine chiamerà il metodo saluto sull'oggetto creato per mostrare un saluto specifico in italiano.
    nome = input("Inserisci il nome: ")  
    cognome = input("Inserisci il tuo cognome")  
    persona_italiana = Italian(nome,cognome)    
    print("\nDati dell'oggetto Italian creato: ")   
    print("Nome: ", persona_italiana.nome) 
    print("Cognome:",persona_italiana.cognome)
    print("Nazionalità: ",persona_italiana.nazionalità)
    print("Lingua principale: ", persona_italiana.lingua_principale)
    
    persona_italiana.saluto()

if __name__ == "__main__": # Questo mi assicura che il codice all'interno venga eseguito direttamene come uno script. E non importato in un modulocome un altro script.
    main()    
        
   