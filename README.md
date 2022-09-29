# bip_test
Per la risoluzione del problema ho utilizzato l'algoritmo di **kadane** che permette di 
trovare la porzione di array che contiene la somma maggiore.

```console
foo@bar:~$ python unit_test.py
```

Per test personali modificare la riga 51 di [kadane](/kadane.py) scrivendo l'array desiderato,
per eseguire:

```console
foo@bar:~$ python kadane.py
```

L'algoritmo consiste nell'utilizzare due variabili per tenere traccia del massimo raggiunto
fino a quel momento (**max_so_far**) e una che tiene traccia della somma fino 
all'elemento corrente (**max_ending_here**).

Quando **max_ending_here** e' minore dell'elemento corrente si aggiorna il punto di partenza **new_positive_start** della nuova sotto lista e **max_ending_here** all'elemento corrente.

Se **max_so_far** e' minore di **max_ending_here** allora 
si aggiorna **max_so_far** a **max_ending_here**, **start_index** prende il valore di **new_positive_start**, che simboleggia l'inizio dell'ultima sotto lista massima, e **end_index** punta all'elemento corrente.

Al termine del programma ritorna la porzione di array tra
**start_index**: **end_index**+1 e **max_so_far** che e' il massimo trovato.



