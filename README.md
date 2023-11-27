# ProgettoML_Mulas

il progetto come da richiesta è diviso in tre parti

      # /*Database*/

l'interno è così strutturato

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/1952449e-28b3-4cf5-ae14-5e9e9706d974)

      --- db.py ---

Questo script si occupa di:
- Connessione al Database: Si connette a un database SQLite nel file ./database/db.sqlite/shopping_trends.sqlite.

- Definizione dello Schema della Tabella: Specifica la struttura della tabella shopping_trends con colonne come Customer_ID, Age, Gender, ecc.

- Creazione della Tabella: Crea la tabella nel database se non esiste già.

- Scaricamento del File CSV: Ottiene i dati da un file CSV 

- Lettura e Inserimento dei Dati: Legge i dati dal CSV e li inserisce nella tabella shopping_trends nel database SQLite.

- Conferma delle Modifiche: Applica le modifiche al database.

- Verifica dei Dati: Esegue una query di selezione (SELECT * FROM shopping_trends) e stampa i risultati, permettendo di verificare che i dati siano stati inseriti correttamente.

- Chiusura della Connessione: Chiude la connessione al database SQLite quando l'operazione è completata.

      --- secret.py ---

Questo script permette di connettersi a un database SQLite contenente dati sui trend degli acquisti.

- Connessione al Database: Il codice si connette a un database SQLite situato nel percorso ./db.sqlite/shopping_trends.sqlite.

- Definizione del Modello Pydantic: Viene definito un modello Pydantic chiamato CustomerInput che rappresenta i dati di input del cliente.

- Classe Customer: Viene definita una classe Customer che rappresenta un cliente e contiene i suoi attributi.

      ---:Funzioni per l'Accesso ai Dati:---

- secretget_all(): Restituisce tutti i clienti nel formato di lista di dizionari.

- secretget_by_id(customer_id): Restituisce un cliente specifico in base all'ID nel formato di lista di dizionari.

- secret_delete(customer_id): Elimina un cliente in base all'ID e restituisce un messaggio di conferma.

- create_user(...): Aggiunge un nuovo cliente al database con i dati forniti.

- create_user_in_function(customer_data): Utilizza il modello Pydantic per aggiungere un nuovo cliente.

- secret_update(update_data): Aggiorna i dati di un cliente esistente nel database.

      --- api.py ---

definisce gli Endpoint delle funzioni citate in precedenza

      # /*Statistiche*/

l'interno è così strutturato

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/573f943e-5f17-48dd-a583-04bf89364968)

      ---secre_stat.py---

Questo script è progettato per calcolare diverse statistiche basate sui dati presenti in un database SQLite contenente informazioni sui trend degli acquisti.

- Connessione al Database:
Viene stabilita la connessione a un database SQLite situato nel percorso ../database/db.sqlite/shopping_trends.sqlite.

- Una funzione (apri_connessione_database()) è definita per aprire la connessione al database, utile per evitare l'uso di una singola connessione in ambienti concorrenti.

- Calcolo dell'Età Media:
La funzione calcola_eta_media_da_db() esegue una query per calcolare l'età media degli acquirenti nel database.

- Calcolo della Spesa Media:
La funzione calcola_spesa_media_da_db() calcola la spesa media degli acquirenti nel database, arrotondando il risultato a due cifre decimali.

- Calcolo della Mediana di "Previous Purchases":
La funzione asincrona calcola_mediana_previous_purchases() calcola la mediana dei valori nella colonna "Previous Purchases" del database.

- Calcolo della Distribuzione Percentuale:
La funzione asincrona calcola_distribuzione_percentuale() calcola la distribuzione percentuale della colonna "Frequency of Purchases". Questa funzione include una serie di operazioni di pulizia e manipolazione dei dati per ottenere risultati accurati.

      --- api.py ---

definisce gli Endpoint delle funzioni citate in precedenza

      # /*Classificazione*/

l'interno è così strutturato

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/ea12d380-3850-4039-a4be-e122d2c80e9a)

Questo script Python crea un servizio web utilizzando il framework FastAPI per gestire il caricamento di immagini, utilizzando un modello YOLO (You Only Look Once) per rilevare oggetti nell'immagine.

- Inizializzazione:
app = FastAPI(): Crea un'app FastAPI, che sarà il server web.

- model_path: Percorso del modello YOLO preaddestrato.

- model = YOLO(model_path): Carica il modello YOLO per il rilevamento di oggetti.

- threshold = 0.5: Soglia di confidenza per accettare un rilevamento come valido.

      --- Gestione del Caricamento di Immagini ---
      
- @app.post("/uploadimage/"): Definisce un endpoint (URL) POST per gestire le richieste di caricamento di immagini.

- file: UploadFile = File(...)): Specifica che l'immagine deve essere inclusa come parte della richiesta.

- La funzione create_upload_image viene eseguita quando una richiesta viene inviata a /uploadimage/.

- Analisi dell'Immagine con YOLO:

- L'immagine caricata viene salvata e quindi letta utilizzando OpenCV.

- Il modello YOLO viene utilizzato per rilevare gli oggetti presenti nell'immagine.

- Verifica se l'Oggetto è un Tipo di Abbigliamento:

- Per ogni oggetto rilevato, viene controllato se appartiene alla categoria "clothes" (abbigliamento), confrontando il nome dell'oggetto con una lista specifica di tipi di abbigliamento.

- Salvataggio o Output dell'Immagine:

- Se viene rilevato un oggetto di abbigliamento, l'immagine viene salvata in una cartella denominata "clothes_images".

- Viene restituita una risposta JSON che indica se è stato rilevato un oggetto di abbigliamento e fornisce il percorso dell'immagine elaborata.

      # /*Training*/

- Collego Google Colab al drive

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/948054ec-05d0-47c5-bf60-d675d0b3e363)

- Installo ultralytics

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/c2c12bf8-ad7a-4406-be4d-8588542051cc)

- Train del Modello

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/df99d7b0-8096-4129-9cfb-5646610657fa)

- Formato data.yaml

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/89d44d6b-e521-470d-8273-951a9b5cde87)

- Salvo e importo il Trained Model

![image](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/27b628c8-d3dd-4f74-881c-f424bf56614f)

      # /*Risultati Training*/
- [Risultati Finali]

![results](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/138005c1-74be-4a56-af9d-e650544aa4f6)

- confusion Matrix [Valutazione performance Adam]

![confusion_matrix](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/82e5e70b-5022-41cb-99fb-1965990ed9c9)

- confusion Matrix Normalized [Valor vicino all'1.00]

![confusion_matrix_normalized](https://github.com/Xienaa/ProgettoML_Mulas/assets/132653183/a4077adc-fe04-484f-abe0-17dff08064dd)
