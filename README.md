# Zastosowania Uczenia Maszynowego
Projekt zaliczeniowy na przedmiot Zastosowania Uczenia Maszynowego
 ## Zespół, opis zadania i cel projektu
 ### Zespół
Michał Brodacki, s32038
Mikołaj Cieślak, S32422
Paweł de Mehlem-Barabaś, s32200
Konrad Dusza, S21516 
### Cel projektu
Celem naszego projektu, jest stworzenie sieci neuronowej zdolnej do wykrycia stronniczości politycznej na podstawie treści tweeta.
 ## Zbiór danych
"PoliticalTweets" to zbiór danych zawierający około 190 000 tweetów amerykańskich polityków, oznaczonych według przynależności partyjnej (Demokraci lub Republikanie) oraz z etykietami sentymentu. Zawiera dane takie jak treść tweeta, identyfikator, użytkownik, data publikacji i partia polityczna. Zbiór ten jest dostępny na platformie [Hugging Face](https://huggingface.co/datasets/Jacobvs/PoliticalTweets/viewer)
 ## Etapy projektu
 
  ### 1. Zebranie i Przygotowanie danych, Inżynieria Cech
- Dane zostały pobrane z [Hugging Face](https://huggingface.co/datasets/Jacobvs/PoliticalTweets/viewer) za pomocą bibliioteki datasets.
- Wartość partii została zakodowana (encoded) cyfrowo, ze zmiennej tekstowej
- Na tekstach tweet'ów zostały wykonane następujące operacje w celu przygotowania ich dla modelu:
* Usunięcie linków z tweetów
* Usunięcie tzw. stopwords oraz znaków specjalnych takich jak często używana w tweetach "Małpa" 
* Usunięto niewnoszące informacji kolumny
* Wykonano lemanizację
* Wykonano Tokenizację
* Dla lepszej reprezentacji słów w sposób wektorowy użyliśmy wektorów osadzania słów (embeddingów), a dokładnie zbiór stworzony przez Stanford University [**Glove**](https://nlp.stanford.edu/data)
  ### 2. Model Referencyjny
 - Prosta sieć neuronowa typu Feed Forward, zaweirająca 5 warstw w tym warstwę wspomnianych wyżej Embeddingów.

  ### 3. Model docelowy 
 - Oparty o architekturę transformera

  ### 4. Ewaluacja
- Na modelu referencyjnym osiągneliśmy wartość Dokładności równą 78%, co jest dobrym prekursorem, pobija wybranie jednej grupy w każdej okazji o ok. 27%, ale samo w sobie jest dalekie od wyniku jaki chcielibyśmy osiągnąć.
- 
## Podsumowanie i Wnioski

 ## Dashboard z wynikami