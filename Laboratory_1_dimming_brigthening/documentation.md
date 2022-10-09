**<h1 style="color:darkslategray;">Laboratorium 1 - ściemnianie / rozjaśnianie</h1>**

**<h2 style="color:darkslategray;">Wstęp</h2>**

**Obraz cyfrowy** jest obrazem złożonym z pikseli(najmniejszych adresowalnych elementow obrazu), który może być reprezentowany jako funkcja w dwuwymiarowym układzie współrzędnych określająca natężenie skali szarości. 

Celem laboratorium było poddanie kolejnych pikseli obrazu przekształceniom punktowym, do których zaliczamy: 

- **Progowanie (*thresholding*)** - dla analizowanego obrazu wyznaczany jest próg jasności. Jeżeli intensywność piksela jest większa niż dany próg, to jest zastępowana wartością oznaczającą kolor biały, jeśli jest mniejsza - kolorem białym.
- **Negatyw**
- **Ściemnianie i rozjaśnianie obrazu**


**<h2 style="color:darkslategray;">Wykonanie laboratorium</h2>**

Wczytany obraz poddano operacjom ściemniania oraz rozjaśniania. Do łatwego aplikowania zmian utworzono prosty interfejs utworzony w języku Python z wykorzystaniem biblioteki Tkinter. Za pomocą suwaka można modyfikować wartość progu binaryzacji.

Do wizualizacji danych wykorzystano bibliotekę Matplotlib oraz OpenCV. Wykorzystano cztery funkcje: **dimming/brightening** do przyciemniania oraz rozjaśniania i **threshold/reverse_threshold** do znajdywania progu binaryzacji. Dwie pierwsze funkcje zmieniają wszystkie elementy których wartość jest mniejsza/większa od wybranej, a dwie kolejne zmieniają wszytskie elementy których wartość nie jest równa zadanej.

<div align="center">
  <img src="https://github.com/Pyother/discrete_modeling/blob/9a86ccf2d415dcdc055588c3969ec3cc7a79ffef/Laboratory_1_dimming_brigthening/resources/screen_results.png">
</div>
<div align="center"><em>Rys.1 Obraz otrzymany dla wyznaczonego progu binaryzacji. Dzięki takiemu rozwiązaniu łatwo rozróżnić wodę od lądu stałego.</em></div>

**<h2 style="color:darkslategray;">Wnioski</h2>**

Na podstawie obserwacji wyników napisanego programu możemy stwierdzić, że wartość progu binaryzacji dla obrazu z zajęć wynosi **217**.
