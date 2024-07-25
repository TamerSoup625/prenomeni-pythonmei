"""Libreria per l'estensione linguistica Python, sviluppata da Pythonmei Uniti e riconosciuta ufficialmente dai Prenomeni Uniti

In questo momento la libreria è in via di sviluppo, non sono disponbili funzionalità linguistiche come i gli avverbi, i complementi indiretti, o la costruzione di periodi.
Se questa libreria verrà utilizzata da più persone, potrebbe venire fuori un aggiornamento. Ditemi cosa ne pensate :)

Di norma si accorcia questa libreria con 'p':

import pythonmei as p

# BASI

La lingua Python parte da alcune caratteristiche di base, da cui questa libreria aggiunge delle caratteristiche.

## Come funziona

Python da sola non è una lingua di comunicazione, bisogna partire da un'altra lingua. In questi esempi useremo l'italiano.
Quando si parla in Python, dici a tutti gli effetti del codice Python eseguibile da un computer. In questo caso, spetta a chi stai parlando ad eseguire il codice.
Chiamare la funzione print equivale a dire qualcosa nella lingua base:

Python                      Italiano
print("Ciao, come stai?")   Ciao, come stai?

Se vuoi, dichiara la variabile __lang__ per specificare la lingua che verrà utilizzata. Viene utilizzato lo standard ISO 639-1.

Python		        Italiano
__lang__ = "it" 	Uso l'italiano. {viene detto senza usare l'italiano}

Come ultima funzionalità, la funzione input può essere usata per eseguire codice in base ad una domanda che il ricevitore deve chiedersi mentalmente.

Python                              Italiano
print(input("Quanti anni hai?"))    {I tuoi anni}

Da notare la differenza tra print e input. print equivale a dire qualcosa con la lingua base, mentre con input fai una domanda mentale all'interlocutore, e l'interlocutore non deve rispondere ma invece usare il valore restituito per eseguire il codice.

## Pronomi

I pronomi in certi case possono essere ambigui. L'Accademia Pythonmei consiglia di non usare pronomi e di invece definire un nome come variabile e poi usare la formattazione della stringa.

lui = "Francia Francesco"
print(f"{lui} è il Monarca Ovest dei Prenomeni Uniti.")
print(f"{lui} rappresenta la Nazione dell'Ostigen.")

## Contenitori di dati

Anche se non sarebbe corretto nelle lingue basi, la Pythonmei consiglia di usare le liste o gli insiemi se si hanno più soggetti.

loro = ["Francia Francesco", "Giunta Daniele"]
print(f"{loro} sono i Monarchi dei Prenomeni Uniti. {loro} rappresentano lo stato.")

## Condizioni

Si può usare input per formulare frasi condizionali senza usare il congiuntivo o il condizionale della lingua base. Si consiglia di non usare il casting al tipo bool di Python ma di invece usare gli operatori di confronto.

la = "al supermercato"
print(f"Vai {la} e prendi un cartone di latte.")
if(input("Quando vai {la} ci sono gli avocado? (s/n)") == "s"):
	print("Prendi anche 6 avocado.")

## Espressioni

Invece di usare input, si consiglia di usare le espressioni di Python quando possibile.

print("Quanto fa la radice di 2?")
from math import sqrt
print(sqrt(2), "!", sep="")

# OGGETTI DELLA LIBRERIA

Questa libreria contiene alcuni oggetti che permettono modifiche universali a parti del discorso.
Questi oggetti possono essere modificate con delle funzioni. Nel caso richiedono altre parti del discorso, puoi passare come argomenti delle stringhe o oggetti di Pythonmei.

e_gentile = p.Predicato(p.Verbo("è"), p.Aggettivo("gentile"))

Seguendo gli standard della programmazione funzionale, queste funzioni NON modificano l'oggetto base ma restitusicono un nuovo oggetto con caratteristiche differenti.
Varie parti del discorso partono da una parte del discorso della lingua base. Questa non deve essere per forza una singola parola né deve essere coincidente con ciò che si vuole ottenere. Ciò significa puoi crearlo a partire da un complemento indiretto od ottenere un verbo a partire da un nome:

dorato = p.Aggettivo("fatto d'oro")
frittellare = p.Verbo("frittella")

Puoi anche usare altri oggetti di Pythonmei in questi casi.

Tutti questi oggetti possono essere convertiti in stringa e restituire il loro contenuto con una certa formattazione. Pythonmei Uniti consiglia di NON leggere i contenuti restituiti per comprendere il parlato, ma di invece guardare direttamente il codice.

- Nome:
    Rappresenta un sostantivo. Per creare un oggetto Nome, parti da una stringa rappresentante una parte del discorso della lingua base:

    mela = p.Nome("mela")

    Possibili modifiche:

    # Guarda la sezione Aggettivo per la funzione con_aggettiv
    chiunque = p.Nome("qualcuno").senza_qualit("genere")
    signor_schwa = p.Nome("signore").senza_genere_numero()
    libro_di_gianni = p.Nome("libro").con_appartenenza("Gianni")

- Aggettivo:
    Rappresenta un attributo o un'apposizione. Per creare un oggetto Aggettivo, parti da una stringa rappresentante una parte del discorso della lingua base:

    verde = p.Aggettivo("verde")

    Gli aggettivi possono essere applicati a un nome con la funzione Nome.con_aggettiv:

    mela_verde = p.Nome("mela").con_aggettiv(verde)

    Come gli oggetti Nome, anche gli aggettivi possono essere privati di qualità.

    bella_belle = p.Aggettivo("bella").senza_qualit("numero")
    bell_schwa = p.Aggettivo("bella").senza_genere_numero()

    Gli oggetti Aggettivo possono essere enfatizzati o invertiti. Per incoraggiare creatività con la lingua base, un'enfatizzazione fuori dal range [-1, 1] è considerato informale.
    
    # 0.0 = no enfatizzazione
    # 1.0 = molto
    # Può essere negativo
    molto_blu = p.Aggettivo("blu").enfatizzato(1.0)
    cattivo = p.Aggettivo("buono").invertito()

- Verbo:
    Rappresenta un verbo, che sia verbale o ausiliare. Per creare un oggetto Verbo, parti da una stringa rappresentante una parte del discorso della lingua base:

    essere = p.Verbo("essere")

    Per ora si può modificare solo il tempo di un verbo. Per indicarlo si usa un valore float o due valori float.

    # Minore di 0.0 = Passato
    # Uguale a 0.0 = Presente
    # Maggiore di 0.0 = Futuro
    # A parte 0.0 che indica il presente, la misura è astratta e non indica un momento preciso, ma solo cos'è successo prima e cos'è successo dopo.
    # Rispetto a Aggettivo.enfatizzato, non c'è più un range entro quale è considerato corretto.
    eravamo = p.Verbo("siamo").con_tempo_astratto(-1.0)
    saremo = p.Verbo("siamo").con_tempo_astratto(1.0)
    siamo_in_un_tempo_qualsiasi = p.Verbo("siamo").con_tempo_astratto(-1.0, 1.0)

- Predicato:
    Rappresenta un predicato verbale (solo oggetto Verbo) o un predicato nominale (oggetto Verbo + oggetto Aggettivo).

    corre = p.Predicato("corre")
    e_gentile = p.Predicato("è", "gentile")

- Frase:
    Rappresenta una preposizione. Per creare un oggetto Frase, parti da un Predicato ed opzionalmente da un Nome che rappresenta il soggetto.

    fa_buio = p.Frase(p.Predicato("fa", "buio"))
    mario_mangia = p.Frase(p.Predicato("mangia"))

    Per ora puoi solo aggiungere complementi diretti (rappresentati da un oggetto Nome) ad un oggetto Frase.
    mario_mangia_fungo = mario_mangia.con_oggett("fungo")

# GUARDATE QUESTA COSA PROFONDA

essere_tempo_qualsiasi = p.Verbo("è").con_tempo_astratto(-1, 1)
molto_cattiv = p.Aggettivo("buono").invertito().enfatizzato(1).senza_genere_numero
bb = p.Nome("Fratello").con_aggettiv("Grande")
print(
    p.Frase(
        p.Predicato(essere_tempo_qualsiasi, molto_cattiv),
        soggetto_opzionale=bb
    )
)
"""
from __future__ import annotations
from copy import deepcopy
from warnings import warn
from typing import Optional


def _indice_con_segno_o_vuoto(x: float) -> str:
    if x > 0.0:
        return f"+{x}"
    elif x == 0.0:
        return ""
    return f"{x}"


def converti_lista(l: list, tipo: type) -> list:
    return [x if type(x) == tipo else tipo(x) for x in l]


def converti(x, tipo: type):
    return x if type(x) == tipo else tipo(x)


class InformalWarning(Warning): pass


class Nome:
    base: str | list[str] = None
    aggettivi: list[Aggettivo] = []
    qualita_rimosse: list[Nome] = []
    proprietario: Optional[Nome] = None


    def __init__(self, nome) -> None:
        self.aggettivi = []
        self.qualita_rimosse = []
        if type(nome) == str:
            self.base = nome
            return
        
        try:
            self.base = [str(x) for x in nome]
        except TypeError:
            self.base = str(nome)
    

    def __str__(self) -> str:
        if type(self.base) == str:
            base_stringa = self.base
        else:
            base_stringa = ", ".join(self.base)
        risultato = base_stringa
        if self.proprietario != None:
            risultato = "{{{0}}}'s {{{1}}}".format(str(self.proprietario), risultato)
        if len(self.qualita_rimosse) != 0:
            risultato += " ~w/o~ {0}".format(", ".join(str(x) for x in self.qualita_rimosse))
        if len(self.aggettivi) != 0:
            risultato += " : " + "; ".join(str(x) for x in self.aggettivi)
        return "{{{0}}}".format(risultato)


    def con_aggettiv(self, *aggettivi: Aggettivo) -> Nome:
        nuovo_self = deepcopy(self)
        nuovo_self.aggettivi.extend(converti_lista(aggettivi, Aggettivo))
        return nuovo_self
    

    def senza_qualit(self, *qualita: Nome) -> Nome:
        nuovo_self = deepcopy(self)
        nuovo_self.qualita_rimosse.extend(converti_lista(qualita, Nome))
        return nuovo_self
    

    def senza_genere_numero(self) -> Nome:
        return self.senza_qualit(Nome(["genere", "numero"]))
    

    def con_appartenenza(self, di_chi_cosa: Nome) -> Nome:
        nuovo_self = deepcopy(self)
        nuovo_self.proprietario = di_chi_cosa
        return nuovo_self


class Aggettivo:
    base: str | list[str] = None
    quanto_enfatizzato: float = 0.0
    is_invertito: bool = False
    qualita_rimosse: list[Nome] = []


    def __init__(self, nome) -> None:
        self.qualita_rimosse = []
        if type(nome) == str:
            self.base = nome
            return
        
        try:
            self.base = [str(x) for x in nome]
        except TypeError:
            self.base = str(nome)
    

    def __str__(self) -> str:
        if type(self.base) == str:
            base_stringa = self.base
        else:
            base_stringa = ", ".join(self.base)
        risultato = base_stringa
        risultato = "{{{0}}}".format(risultato)
        parentesi_piu = False
        if len(self.qualita_rimosse) != 0:
            risultato += "~w/o~{0}".format(", ".join(str(x) for x in self.qualita_rimosse))
            parentesi_piu = True
        #risultato = "{{{0}}}".format(base_stringa)
        if self.is_invertito:
            risultato = "!" + risultato
            parentesi_piu = True
        risultato += _indice_con_segno_o_vuoto(self.quanto_enfatizzato)
        if parentesi_piu:
            risultato = "{{{0}}}".format(risultato)
        return risultato


    def enfatizzato(self, quantita: float) -> Aggettivo:
        nuovo_self = deepcopy(self)
        nuovo_self.quanto_enfatizzato += quantita
        if abs(nuovo_self.quanto_enfatizzato) > 1:
            warn("Usare un'enfatizzazione fuori dal range [-1, 1] è considerato informale. Prova ad usare altre parole del linguaggio base.", InformalWarning)
        return nuovo_self


    def invertito(self) -> Aggettivo:
        nuovo_self = deepcopy(self)
        nuovo_self.is_invertito = not self.is_invertito
        return nuovo_self
    

    def senza_qualit(self, *qualita: Nome) -> Aggettivo:
        nuovo_self = self
        nuovo_self.qualita_rimosse.extend(converti_lista(qualita, Nome))
        return nuovo_self
    

    def senza_genere_numero(self) -> Aggettivo:
        return self.senza_qualit("genere", "numero")


class Verbo:
    base: str | list[str] = None
    inizio_astratto: Optional[float] = None
    fine_astratta: Optional[float] = None


    def __init__(self, verbo) -> None:
        if type(verbo) == str:
            self.base = verbo
            return
                
        try:
            self.base = [str(x) for x in verbo]
        except TypeError:
            self.base = str(verbo)
    

    def __str__(self) -> str:
        if type(self.base) == str:
            base_stringa = self.base
        else:
            base_stringa = ", ".join(self.base)
        risultato = base_stringa
        risultato = "{{{0}}}".format(risultato)
        if [self.inizio_astratto, self.fine_astratta].count(None) != 2:
            risultato += f" time [{self.inizio_astratto}, {self.fine_astratta}]"
        return "{{{0}}}".format(risultato)


    def con_tempo_astratto(self, *inizio_fine: Optional[float]) -> Verbo:
        nuovo_self = deepcopy(self)
        assert(len(inizio_fine) in [1, 2])
        nuovo_self.inizio_astratto = inizio_fine[0]
        nuovo_self.fine_astratta = inizio_fine[0 if len(inizio_fine) == 1 else 1]
        return nuovo_self


class Predicato:
    verbo: Verbo = None
    attributo: Optional[Aggettivo] = None


    def __init__(self, verbo: Verbo, attributo_opzionale: Optional[Aggettivo] = None) -> None:
        self.verbo = converti(verbo, Verbo)
        if attributo_opzionale != None:
            self.attributo = converti(attributo_opzionale, Aggettivo)
    

    def __str__(self) -> str:
        if self.attributo == None:
            return str(self.verbo)
        return "{{{0} -> {1}}}".format(str(self.verbo), str(self.attributo))


class Frase:
    predicato: Predicato = None
    soggetto: Optional[Nome] = None
    oggetto: Optional[Nome] = None


    def __init__(self, predicato: Predicato, soggetto_opzionale: Optional[Nome] = None) -> None:
        self.predicato = converti(predicato, Predicato)
        if soggetto_opzionale != None:
            self.soggetto = converti(soggetto_opzionale, Nome)


    def __str__(self) -> str:
        risultato = ">>> "
        if self.soggetto != None:
            risultato += f"{str(self.soggetto)} "
        risultato += str(self.predicato)
        if self.oggetto != None:
            risultato += f" {str(self.oggetto)}"
        return risultato
    

    def con_oggett(self, chi_cosa: Nome) -> Frase:
        nuovo_self = deepcopy(self)
        nuovo_self.oggetto = converti(chi_cosa, Nome)
        return nuovo_self