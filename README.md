
# Testy funkcji matematycznych w Pythonie

To repozytorium zawiera przykładowe testy jednostkowe dla kilku funkcji matematycznych w Pythonie. Funkcje te obejmują:
- Dodawanie liczb
- Sprawdzanie parzystości
- Konwersja temperatury z Celsjusza na Fahrenheita
- Obliczanie silni
- Sprawdzanie, czy liczba jest liczbą pierwszą

## Technologie

- Python 3.x
- Biblioteka `unittest` (do testów jednostkowych)

## Instalacja

1. Sklonuj repozytorium na swoje lokalne urządzenie:
   ```bash
   git clone https://github.com/TwojaNazwaUzytkownika/nazwa-repozytorium.git
   ```
2. Wejdź do katalogu projektu:
   ```bash
   cd nazwa-repozytorium
   ```

3. Upewnij się, że masz zainstalowanego Pythona w wersji 3.x. Możesz sprawdzić wersję Pythona poleceniem:
   ```bash
   python --version
   ```

## Jak uruchomić testy

1. Uruchom testy jednostkowe, wykonując poniższe polecenie w terminalu:
   ```bash
   python -m unittest test.py
   ```
   (gdzie `test.py` to nazwa pliku zawierającego kod testów, jeśli używasz innej nazwy pliku, zastąp ją odpowiednią nazwą).

2. Testy jednostkowe zostaną uruchomione i wyświetlone zostaną wyniki, które informują, czy testy zakończyły się sukcesem, czy wystąpiły błędy.

## Testowane funkcje

### 1. Funkcja `add_numbers(a, b)`
Funkcja dodaje dwie liczby.

**Testy:**
- Dodawanie liczb dodatnich
- Dodawanie liczby dodatniej i ujemnej
- Dodawanie liczb ujemnych
- Dodawanie liczby do zera

### 2. Funkcja `is_even(n)`
Funkcja sprawdza, czy liczba jest liczbą parzystą.

**Testy:**
- Testowanie liczb parzystych
- Testowanie liczb nieparzystych
- Testowanie liczby zero

### 3. Funkcja `celsius_to_fahrenheit(celsius)`
Funkcja konwertuje temperaturę z Celsjusza na Fahrenheita.

**Testy:**
- Standardowe temperatury
- Temperatury ujemne
- Bardzo wysokie temperatury

### 4. Funkcja `factorial(n)`
Funkcja oblicza silnię liczby.

**Testy:**
- Silnia dla małych liczb
- Silnia dla większych liczb
- Testowanie błędów dla liczb ujemnych
- Testowanie wydajności dla dużych liczb

### 5. Funkcja `is_prime(n)`
Funkcja sprawdza, czy liczba jest liczbą pierwszą.

**Testy:**
- Testowanie liczb pierwszych
- Testowanie liczb niepierwszych
- Testowanie liczb mniejszych niż 2
- Testowanie dużej liczby pierwszej

## Contributing

Jeśli chcesz przyczynić się do rozwoju projektu, zapraszam do zgłaszania problemów (Issues) lub tworzenia Pull Requestów.

1. Forkuj repozytorium.
2. Stwórz nową gałąź (`git checkout -b feature-name`).
3. Zrób zmiany i stwórz commit (`git commit -am 'Add new feature'`).
4. Wypchnij zmiany do swojego repozytorium (`git push origin feature-name`).
5. Otwórz Pull Request.

## Licencja

Ten projekt jest licencjonowany na zasadach [MIT License](LICENSE).
