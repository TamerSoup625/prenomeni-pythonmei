Questo è il file README di __Pythonmei__, libreria per l'estensione linguistica Python, sviluppata da Pythonmei Uniti e riconosciuta ufficialmente dai Prenomeni Uniti

In questo momento la libreria è in via di sviluppo, non sono disponbili funzionalità linguistiche come i gli avverbi, i complementi indiretti, o la costruzione di periodi.
Se questa libreria verrà utilizzata da più persone, potrebbe venire fuori un aggiornamento. Ditemi cosa ne pensate :)

Di norma si accorcia questa libreria con 'p':
```python
import pythonmei as p
```
# BASI

La lingua Python parte da alcune caratteristiche di base, da cui questa libreria aggiunge delle caratteristiche.

## Come funziona

Python da sola non è una lingua di comunicazione, bisogna partire da un'altra lingua. In questi esempi useremo l'italiano.
Quando si parla in Python, dici a tutti gli effetti del codice Python eseguibile da un computer. In questo caso, spetta a chi stai parlando ad eseguire il codice.
Chiamare la funzione print equivale a dire qualcosa nella lingua base:

|Python|Italiano|
|-|-|
|`print("Ciao, come stai?")`|Ciao, come stai?|

Se vuoi, dichiara la variabile `__lang__` per specificare la lingua che verrà utilizzata. Viene utilizzato lo standard ISO 639-1.

|Python|Italiano|
|-|-|
|`__lang__ = "it"`|Uso l'italiano. {viene detto senza usare l'italiano}|

Come ultima funzionalità, la funzione input può essere usata per eseguire codice in base ad una domanda che il ricevitore deve chiedersi mentalmente.

|Python|Italiano|
|-|-|
|`print(input("Quanti anni hai?"))`|{I tuoi anni}|

Da notare la differenza tra print e input. print equivale a dire qualcosa con la lingua base, mentre con input fai una domanda mentale all'interlocutore, e l'interlocutore non deve rispondere ma invece usare il valore restituito per eseguire il codice.

## Pronomi

I pronomi in certi case possono essere ambigui. L'Accademia Pythonmei consiglia di non usare pronomi e di invece definire un nome come variabile e poi usare la formattazione della stringa.
```python
lui = "Francia Francesco"
print(f"{lui} è il Monarca Ovest dei Prenomeni Uniti.")
print(f"{lui} rappresenta la Nazione dell'Ostigen.")
```
## Contenitori di dati

Anche se non sarebbe corretto nelle lingue basi, la Pythonmei consiglia di usare le liste o gli insiemi se si hanno più soggetti.
```python
loro = ["Francia Francesco", "Giunta Daniele"]
print(f"{loro} sono i Monarchi dei Prenomeni Uniti. {loro} rappresentano lo stato.")
```
## Condizioni

Si può usare input per formulare frasi condizionali senza usare il congiuntivo o il condizionale della lingua base. Si consiglia di non usare il casting al tipo bool di Python ma di invece usare gli operatori di confronto.
```python
la = "al supermercato"
print(f"Vai {la} e prendi un cartone di latte.")
if(input("Quando vai {la} ci sono gli avocado? (s/n)") == "s"):
	print("Prendi anche 6 avocado.")
```
## Espressioni

Invece di usare input, si consiglia di usare le espressioni di Python quando possibile.
```python
print("Quanto fa la radice di 2?")
from math import sqrt
print(sqrt(2), "!", sep="")
```
# OGGETTI DELLA LIBRERIA

Questa libreria contiene alcuni oggetti che permettono modifiche universali a parti del discorso.
Questi oggetti possono essere modificate con delle funzioni. Nel caso richiedono altre parti del discorso, puoi passare come argomenti delle stringhe o oggetti di Pythonmei.
```python
e_gentile = p.Predicato(p.Verbo("è"), p.Aggettivo("gentile"))
```
Seguendo gli standard della programmazione funzionale, queste funzioni NON modificano l'oggetto base ma restitusicono un nuovo oggetto con caratteristiche differenti.
Varie parti del discorso partono da una parte del discorso della lingua base. Questa non deve essere per forza una singola parola né deve essere coincidente con ciò che si vuole ottenere. Ciò significa puoi crearlo a partire da un complemento indiretto od ottenere un verbo a partire da un nome:
```python
dorato = p.Aggettivo("fatto d'oro")
frittellare = p.Verbo("frittella")
```
Puoi anche usare altri oggetti di Pythonmei in questi casi.

Tutti questi oggetti possono essere convertiti in stringa e restituire il loro contenuto con una certa formattazione. Pythonmei Uniti consiglia di NON leggere i contenuti restituiti per comprendere il parlato, ma di invece guardare direttamente il codice.

## Nome
Rappresenta un sostantivo. Per creare un oggetto Nome, parti da una stringa rappresentante una parte del discorso della lingua base:
```python
mela = p.Nome("mela")
```
Possibili modifiche:
```python
# Guarda la sezione Aggettivo per la funzione con_aggettiv
chiunque = p.Nome("qualcuno").senza_qualit("genere")
signor_schwa = p.Nome("signore").senza_genere_numero()
libro_di_gianni = p.Nome("libro").con_appartenenza("Gianni")
```

## Aggettivo
Rappresenta un attributo o un'apposizione. Per creare un oggetto Aggettivo, parti da una stringa rappresentante una parte del discorso della lingua base:
```python
verde = p.Aggettivo("verde")
```
Gli aggettivi possono essere applicati a un nome con la funzione Nome.con_aggettiv:
```python
mela_verde = p.Nome("mela").con_aggettiv(verde)
```
Come gli oggetti Nome, anche gli aggettivi possono essere privati di qualità.
```python
bella_belle = p.Aggettivo("bella").senza_qualit("numero")
bell_schwa = p.Aggettivo("bella").senza_genere_numero()
```
Gli oggetti Aggettivo possono essere enfatizzati o invertiti. Per incoraggiare creatività con la lingua base, un'enfatizzazione fuori dal range [-1, 1] è considerato informale.
```python
# 0.0 = no enfatizzazione
# 1.0 = molto
# Può essere negativo
molto_blu = p.Aggettivo("blu").enfatizzato(1.0)
cattivo = p.Aggettivo("buono").invertito()
```

## Verbo
Rappresenta un verbo, che sia verbale o ausiliare. Per creare un oggetto Verbo, parti da una stringa rappresentante una parte del discorso della lingua base:
```python
essere = p.Verbo("essere")
```
Per ora si può modificare solo il tempo di un verbo. Per indicarlo si usa un valore float o due valori float.
```python
# Minore di 0.0 = Passato
# Uguale a 0.0 = Presente
# Maggiore di 0.0 = Futuro
# A parte 0.0 che indica il presente, la misura è astratta e non indica un momento preciso, ma solo cos'è successo prima e cos'è successo dopo.
# Rispetto a Aggettivo.enfatizzato, non c'è più un range entro quale è considerato corretto.
eravamo = p.Verbo("siamo").con_tempo_astratto(-1.0)
saremo = p.Verbo("siamo").con_tempo_astratto(1.0)
siamo_in_un_tempo_qualsiasi = p.Verbo("siamo").con_tempo_astratto(-1.0, 1.0)
```

## Predicato
Rappresenta un predicato verbale (solo oggetto Verbo) o un predicato nominale (oggetto Verbo + oggetto Aggettivo).
```python
corre = p.Predicato("corre")
e_gentile = p.Predicato("è", "gentile")
```

## Frase
Rappresenta una preposizione. Per creare un oggetto Frase, parti da un Predicato ed opzionalmente da un Nome che rappresenta il soggetto.
```python
fa_buio = p.Frase(p.Predicato("fa", "buio"))
mario_mangia = p.Frase(p.Predicato("mangia"))
```
Per ora puoi solo aggiungere complementi diretti (rappresentati da un oggetto Nome) ad un oggetto Frase.
```python
mario_mangia_fungo = mario_mangia.con_oggett("fungo")
```

# ???

```python
essere_tempo_qualsiasi = p.Verbo("è").con_tempo_astratto(-1, 1)
molto_cattiv = p.Aggettivo("buono").invertito().enfatizzato(1).senza_genere_numero
bb = p.Nome("Fratello").con_aggettiv("Grande")
print(
    p.Frase(
        p.Predicato(essere_tempo_qualsiasi, molto_cattiv),
        soggetto_opzionale=bb
    )
)
```