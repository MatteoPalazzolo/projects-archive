## Intro
- fatto con Domenico Giubellini in 3° liceo (A.S. 2020/2021)
- proposto dal prof di informatica per gestire le entrate e le uscite degli alunni nel centro estivo dell'Aldo Moro nel estate del 2020

## Idea
- creare un sistema composto da un server che si interfacciava col DB e da diversi client che leggevano QR code e comunicavano al server eventuali entrate o uscite degli studenti
- ad ogni studente era stato assegnato ed inviato per mail un proprio QR code per identificarsi

## Progetto
articolato in 3 parti:
- un server TCP scritto in python
- un client TCP con interfaccia grafica (Tkinter) fatto interamente in python
- un tool per inviare le mail a tutti gli studenti con il proprio QR code

## Problemi
- si tratta di un progetto abbastanza confusionario
- per il momento non è utilizzabile per buona parte a causa della mancanza dello schema del DB di MySQL